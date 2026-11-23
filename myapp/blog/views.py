import logging

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

from .models import Post, AboutUs, Category
from .forms import (
    ContactForm,
    ForgotPasswordForm,
    RegisterForm,
    LoginForm,
    RestPasswordForm,
    PostForm,
)


# Display public blog posts and handle search
def index(request):
    title = "Latest post"

    search_query = request.GET.get("q", "").strip()
    all_posts = Post.objects.all().order_by("-created_at")

    if search_query:
        all_posts = all_posts.filter(
            title__icontains=search_query
        )

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/index.html",
        {
            "blog_title": title,
            "page_obj": page_obj,
            "search_query": search_query,
        },
    )


def detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(
            category=post.category
        ).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")

    return render(
        request,
        "blog/detail.html",
        {
            "post": post,
            "related_post": related_posts,
        },
    )


def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))


def new_url_view(request):
    return HttpResponse("This is the new URL")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        logger = logging.getLogger("TESTING")

        if form.is_valid():
            logger.debug(
                f"POST Data is {form.cleaned_data['name']} "
                f"{form.cleaned_data['email']} "
                f"{form.cleaned_data['message']}"
            )

            success_message = "Your email has been send!"

            return render(
                request,
                "blog/contact.html",
                {
                    "form": form,
                    "success_message": success_message,
                },
            )

        logger.debug("Form validation failure")

        return render(
            request,
            "blog/contact.html",
            {
                "form": form,
                "name": name,
                "email": email,
                "message": message,
            },
        )

    return render(request, "blog/contact.html")


def about(request):
    about_content = AboutUs.objects.first()

    if about_content is None or not about_content.content:
        about_content = "Default contant goes here"
    else:
        about_content = about_content.content

    return render(
        request,
        "blog/about.html",
        {"about_content": about_content},
    )


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            messages.success(
                request,
                "Registration Successfull. You can login",
            )
            return redirect("blog:login")

    return render(request, "blog/register.html", {"form": form})


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                username=username,
                password=password,
            )

            if user is not None:
                auth_login(request, user)
                return redirect("blog:dashboard")

            messages.error(request, "Invalid username or password")

    return render(request, "blog/login.html", {"form": form})


@login_required
def dashboard(request):
    blog_title = "My Posts"

    all_posts = Post.objects.filter(
        user=request.user
    ).order_by("-created_at")

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/dashboard.html",
        {
            "blog_title": blog_title,
            "page_obj": page_obj,
        },
    )


def logout(request):
    auth_logout(request)
    return redirect("blog:index")


def forgot_password(request):
    form = ForgotPasswordForm()

    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.filter(email=email).first()

            if user is not None:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                current_site = get_current_site(request)
                domain = current_site.domain

                subject = "Reset password requested"

                message = render_to_string(
                    "blog/reset_password_email.html",
                    {
                        "domain": domain,
                        "uid": uid,
                        "token": token,
                    },
                )

                send_mail(
                    subject,
                    message,
                    "rohithkumarm111104@gmail.com",
                    [email],
                )

            messages.success(
                request,
                "If an account exists for that email, a reset link has been sent.",
            )

    return render(
        request,
        "blog/forgot_password.html",
        {"form": form},
    )


def reset_password(request, uidb64, token):
    form = RestPasswordForm()

    if request.method == "POST":
        form = RestPasswordForm(request.POST)

        if form.is_valid():
            new_password = form.cleaned_data["new_password"]

            try:
                uid = urlsafe_base64_decode(uidb64)
                user = User.objects.get(pk=uid)

            except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
            ):
                user = None

            if (
                user is not None
                and default_token_generator.check_token(user, token)
            ):
                user.set_password(new_password)
                user.save()

                messages.success(
                    request,
                    "Your password has been reset successfully!",
                )
                return redirect("blog:login")

            messages.error(
                request,
                "The password reset link is invalid",
            )

    return render(
        request,
        "blog/reset_password.html",
        {"form": form},
    )


@login_required
def new_post(request):
    categories = Category.objects.all()
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect("blog:dashboard")

    return render(
        request,
        "blog/new_post.html",
        {
            "categories": categories,
            "form": form,
        },
    )


@login_required
def edit_post(request, post_id):
    categories = Category.objects.all()
    post = get_object_or_404(
        Post,
        id=post_id,
        user=request.user,
    )

    if request.method == "POST":
        form = PostForm(
            request.POST,
            request.FILES,
            instance=post,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your Post Updated successfully!",
            )
            return redirect("blog:dashboard")
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "blog/edit_post.html",
        {
            "categories": categories,
            "post": post,
            "form": form,
        },
    )


@login_required
@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        user=request.user,
    )
    post.delete()

    messages.success(request, "Post deleted successfully!")
    return redirect("blog:dashboard")