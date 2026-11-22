# 📝 Django Blog Platform

A full-featured blog application built with Django 6.1, featuring user authentication, RESTful API, rich content management, and a modern responsive UI powered by Bootstrap 5.

![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14-092E20?style=for-the-badge&logo=django&logoColor=white)

---

## 🌟 Features

### Core Blogging Functionality
- **Post Management**: Create, read, update, and delete blog posts with rich text content
- **Categories**: Organize posts with categories (Sports, Technology, Science, Art, Food)
- **Image Upload**: Support for post thumbnails with automatic fallback images
- **Slug-based URLs**: SEO-friendly URLs using auto-generated slugs from post titles
- **Pagination**: Built-in pagination for post listings (5 posts per page)

### User Authentication & Authorization
- **Registration**: User registration with email validation and password confirmation
- **Login/Logout**: Secure session-based authentication
- **Password Reset**: Email-based password reset flow with token validation
- **Dashboard**: Personal dashboard showing user's own posts
- **Ownership Protection**: Users can only edit/delete their own posts

### RESTful API (Django REST Framework)
- **Post Endpoints**: Full CRUD API for posts with search and filtering
- **Category Endpoints**: List and retrieve categories
- **Permissions**: `IsAuthenticatedOrReadOnly` + `IsOwnerOrReadOnly` for post operations
- **Search**: Full-text search across post titles and content
- **Filtering**: Filter posts by category
- **Pagination**: Standard DRF pagination (5 items per page)

### Frontend & UX
- **Responsive Design**: Mobile-first approach with Bootstrap 5.3
- **Bootstrap Icons**: Beautiful iconography throughout
- **Clean Layout**: Sticky footer, semantic HTML structure
- **Form Validation**: Client-side and server-side validation with user-friendly error messages
- **Custom 404 Page**: Branded error handling

### Admin & Management
- **Django Admin**: Full admin interface for content management
- **Management Commands**: Populate categories and sample posts via CLI
- **Logging**: Configured console logging for debugging

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| **Framework** | Django 6.1 |
| **API** | Django REST Framework 3.14 |
| **Database** | MySQL 8.0 |
| **Frontend** | Bootstrap 5.3, Bootstrap Icons 1.11 |
| **Auth** | Django Auth System (Session-based) |
| **Email** | SMTP (Mailtrap for development) |
| **Static/Media** | Django Staticfiles + Media handling |

---

## 📁 Project Structure

```
myapp/
├── manage.py
├── myapp/                 # Project settings
│   ├── __init__.py
│   ├── settings.py        # Main configuration
│   ├── urls.py            # Root URL routing
│   ├── wsgi.py
│   ├── asgi.py
│   ├── views.py           # Custom 404 handler
│   └── middleware.py      # Custom authentication middleware
├── blog/                  # Main blog application
│   ├── models.py          # Post, Category, AboutUs models
│   ├── views.py           # Traditional Django views
│   ├── api_views.py       # DRF API views
│   ├── serializers.py     # DRF serializers
│   ├── permissions.py     # Custom DRF permissions
│   ├── forms.py           # Django forms
│   ├── urls.py            # Blog URL patterns
│   ├── api_urls.py        # API URL patterns
│   ├── admin.py           # Admin configuration
│   ├── apps.py
│   ├── management/
│   │   └── commands/
│   │       ├── populate_categories.py
│   │       └── populate_posts.py
│   ├── migrations/
│   ├── templates/blog/    # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── detail.html
│   │   ├── dashboard.html
│   │   ├── new_post.html
│   │   ├── edit_post.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── contact.html
│   │   ├── about.html
│   │   ├── forgot_password.html
│   │   ├── reset_password.html
│   │   └── includes/
│   │       ├── header.html
│   │       ├── footer.html
│   │       └── errors.html
│   └── static/blog/
│       └── style.css
├── media/                 # User uploads
│   └── posts/images/
├── templates/             # Project-level templates
│   └── 404.html
├── db.sqlite3             # SQLite fallback (dev)
└── env/                   # Virtual environment
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- MySQL 8.0+ (or use SQLite for development)
- pip / virtualenv

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-blog.git
   cd django-blog
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   # or
   env\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework mysqlclient pillow
   ```
   Or create a `requirements.txt`:
   ```txt
   Django==6.1
   djangorestframework==3.14
   mysqlclient==2.2
   pillow==10.0
   ```
   Then: `pip install -r requirements.txt`

4. **Configure Database**
   
   **MySQL (Production/Development):**
   - Create a database named `blog`
   - Update `myapp/settings.py` with your credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'blog',
           'USER': 'your_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306'
       }
   }
   ```
   
   **SQLite (Quick Start):**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

5. **Configure Email (Development)**
   ```python
   # settings.py - Use Mailtrap or console backend
   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   # Or for Mailtrap:
   EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your_user'
   EMAIL_HOST_PASSWORD = 'your_password'
   ```

6. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Populate Sample Data (Optional)**
   ```bash
   python manage.py populate_categories
   python manage.py populate_posts
   ```

9. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

10. **Run Development Server**
    ```bash
    python manage.py runserver
    ```
    Visit: http://127.0.0.1:8000/

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000/api/
```

### Endpoints

#### Posts
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/posts/` | List all posts (paginated, searchable, filterable) |
| `POST` | `/posts/` | Create a new post (auth required) |
| `GET` | `/posts/{slug}/` | Retrieve a single post |
| `PUT/PATCH` | `/posts/{slug}/` | Update a post (owner only) |
| `DELETE` | `/posts/{slug}/` | Delete a post (owner only) |

**Query Parameters:**
- `search` - Search in title and content
- `category` - Filter by category ID

#### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/categories/` | List all categories |
| `GET` | `/categories/{id}/` | Retrieve a category |

### Authentication
- **Read operations**: Public access
- **Write operations**: Require authentication (Session or Token)
- **Ownership**: Users can only modify their own posts

### Example Requests

**List posts with search:**
```bash
curl "http://localhost:8000/api/posts/?search=django&category=2"
```

**Create a post:**
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: your_csrf_token" \
  -d '{"title": "My Post", "content": "Content here", "category": 1}'
```

---

## 🎨 Customization

### Theming
Modify `blog/static/blog/style.css` for custom styles. The base template includes CSS custom properties for easy theming.

### Adding Categories
```bash
python manage.py shell
# Or use the management command
python manage.py populate_categories
```

### Email Templates
Customize password reset emails in `blog/templates/blog/reset_password_email.html`

---

## 🔒 Security Notes

> ⚠️ **Important**: Before deploying to production:

1. **Change `SECRET_KEY`** - Generate a new one:
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

2. **Set `DEBUG = False`**

3. **Configure `ALLOWED_HOSTS`** properly

4. **Use environment variables** for sensitive settings:
   ```python
   import os
   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
   DATABASES['default']['PASSWORD'] = os.environ.get('DB_PASSWORD')
   ```

5. **Enable HTTPS** and secure cookies:
   ```python
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

6. **Remove hardcoded credentials** from `settings.py`

---

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📦 Deployment

### Production Checklist
- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` from environment
- [ ] Database credentials from environment
- [ ] `ALLOWED_HOSTS` configured
- [ ] Static files collected (`collectstatic`)
- [ ] Media files served by web server (nginx/Apache)
- [ ] HTTPS enabled
- [ ] Email backend configured for production
- [ ] Logging configured for production

### Docker (Example)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Rohith Kumar**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: rohithkumarm111104@gmail.com

---

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
- [Django REST Framework](https://www.django-rest-framework.org/) - Web APIs made easy
- [Bootstrap](https://getbootstrap.com/) - The most popular HTML, CSS, and JS library
- [Bootstrap Icons](https://icons.getbootstrap.com/) - Free, high quality, open source icon library
- [Mailtrap](https://mailtrap.io/) - Email testing for developers

---

⭐ **Star this repo if you found it helpful!**