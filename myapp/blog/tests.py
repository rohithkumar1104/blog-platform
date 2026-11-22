from django.test import TestCase
from django.urls import reverse

from .models import Category, Post

class PostListAPITests(TestCase):
    def test_posts_endpoint_returns_serialized_posts(self):
        category = Category.objects.create(name="Technology")
        post = Post.objects.create(
            title="Learning DRF",
            content="Our first API post.",
            category=category,
        )

        response = self.client.get(reverse("api:post-list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["title"], post.title)
        self.assertEqual(response.json()[0]["category_name"], category.name)
