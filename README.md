# 📝 Django Blog Platform

A full-featured blog application built with Django 6.1, featuring user authentication, a RESTful API, rich content management, a Django admin panel, and a modern responsive UI powered by Bootstrap 5. Deployed on Render with a hosted MySQL database and Cloudinary image storage.

🔗 **Live site:** [https://blog-platform-kc5y.onrender.com](https://blog-platform-kc5y.onrender.com/)

> ℹ️ The site runs on Render's free plan, so it may take up to a minute to wake up on the first visit after a period of inactivity.

![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.18-092E20?style=for-the-badge&logo=django&logoColor=white)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Media-Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)

---

## 🌟 Features

### Core Blogging Functionality

- **Post Management**: Create, read, update, and delete blog posts with rich text content
- **Categories**: Organize posts with categories (Sports, Technology, Science, Art, Food)
- **Image Upload**: Post thumbnails stored on Cloudinary, with automatic fallback images
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

- **Django Admin Panel**: Full admin interface at `/admin/` for managing posts, categories, About Us content and users
- **Management Commands**: Populate categories and sample posts via CLI
- **Logging**: Configured console logging for debugging

---

## 🛠 Tech Stack

| Layer             | Technology                                                                        |
| ----------------- | --------------------------------------------------------------------------------- |
| **Framework**     | Django 6.1                                                                        |
| **API**           | Django REST Framework 3.18                                                        |
| **Database**      | MySQL 8.0, hosted on [Enzonic Databases](https://databases.enzonic.com/dashboard) |
| **Media Storage** | [Cloudinary](https://console.cloudinary.com) (via `django-cloudinary-storage`)    |
| **Hosting**       | [Render](https://render.com) (Gunicorn)                                           |
| **Frontend**      | Bootstrap 5.3, Bootstrap Icons 1.11                                               |
| **Auth**          | Django Auth System (Session-based)                                                |
| **Email**         | SMTP (Mailtrap for development)                                                   |
| **Admin**         | Django Admin                                                                      |

---

## 📁 Project Structure

```
myapp/
├── manage.py
├── myapp/                 # Project settings
│   ├── __init__.py
│   ├── settings.py        # Main configuration (reads environment variables)
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
├── media/                 # Local uploads (production uses Cloudinary)
│   └── posts/images/
├── templates/             # Project-level templates
│   └── 404.html
└── requirements.txt
```

---

## 🚀 Getting Started (Local Development)

### Prerequisites

- Python 3.11+
- MySQL 8.0+ (or use SQLite for quick local development)
- pip / virtualenv

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/rohithkumar1104/blog-platform.git
   cd blog-platform
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
   pip install -r requirements.txt
   ```

   Main packages: `Django`, `djangorestframework`, `mysqlclient`, `pillow`, `gunicorn`, `cloudinary`, `django-cloudinary-storage`.

4. **Configure the database**

   `settings.py` reads its database settings from environment variables and falls back to a local MySQL database named `blog` (user `root`, host `localhost`). Either create that database, or set the `DB_*` variables (see [Environment Variables](#-environment-variables)).

   > Note: `settings.py` sets `ssl_mode` to `REQUIRED` for the MySQL connection, which the hosted database needs. If your local MySQL has no SSL enabled, remove the `OPTIONS` block from `DATABASES` for local development.

   **SQLite (quick start):**

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

5. **Configure email (development)**

   ```python
   # settings.py - use the console backend to print emails in the terminal
   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   ```

   Or set the `EMAIL_*` environment variables to use Mailtrap or another SMTP provider.

6. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser (for the admin panel)**

   ```bash
   python manage.py createsuperuser
   ```

8. **Populate sample data (optional)**

   ```bash
   python manage.py populate_categories
   python manage.py populate_posts
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   Visit: http://127.0.0.1:8000/

---

## 🔑 Environment Variables

All sensitive and deployment-specific settings are read from environment variables. Never commit real values to the repository.

| Variable                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `DJANGO_SECRET_KEY`                                                                                         | Django secret key                                                                                           |
| `DEBUG`                                                                                                     | `True` for local development, `False` in production                                                         |
| `ALLOWED_HOSTS`                                                                                             | Comma-separated hostnames, e.g. `blog-platform-kc5y.onrender.com`                                           |
| `CSRF_TRUSTED_ORIGINS`                                                                                      | Comma-separated origins, e.g. `https://blog-platform-kc5y.onrender.com`                                     |
| `DB_NAME`                                                                                                   | Database name                                                                                               |
| `DB_USER`                                                                                                   | Database user (see the Enzonic note below)                                                                  |
| `DB_PASSWORD`                                                                                               | Database password                                                                                           |
| `DB_HOST`                                                                                                   | Database host from the Enzonic dashboard                                                                    |
| `DB_PORT`                                                                                                   | Database port (`3306`)                                                                                      |
| `CLOUDINARY_CLOUD_NAME`                                                                                     | Cloud name from the Cloudinary console                                                                      |
| `CLOUDINARY_API_KEY`                                                                                        | Cloudinary API key                                                                                          |
| `CLOUDINARY_API_SECRET`                                                                                     | Cloudinary API secret                                                                                       |
| `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL` | SMTP settings for password-reset emails                                                                     |
| `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD`                          | Used once to create the admin user on a host without shell access (remove the password variable afterwards) |

---

## ☁️ Deployment

The site is deployed on **Render** (web service), with the MySQL database on **Enzonic Databases** and image uploads on **Cloudinary**.

### 1. Database (Enzonic Databases)

1. Create a MySQL database in the [Enzonic dashboard](https://databases.enzonic.com/dashboard).
2. Copy the host, port, database name and user from the dashboard.
3. Set `DB_USER` to `<user>.<host label>`, where the host label is the first part of the host. For example, for host `mydb-ab12c1.db.enzonic.com` and user `app`, the username is `app.mydb-ab12c1`. Enzonic uses this to route the connection.

### 2. Media storage (Cloudinary)

1. Sign in to the [Cloudinary console](https://console.cloudinary.com).
2. Copy the cloud name, API key and API secret into the `CLOUDINARY_*` variables.

### 3. Web service (Render)

1. Push the project to GitHub and create a new **Web Service** on Render from the repository.
2. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:**
     ```
     python manage.py migrate && gunicorn myapp.wsgi:application
     ```
3. Add all the variables from the [Environment Variables](#-environment-variables) table under **Environment**.
4. Deploy. Render redeploys automatically on every push to `main`.

### 4. Django admin panel

The admin panel is available at `/admin/` (for example `https://blog-platform-kc5y.onrender.com/admin/`). To create the first admin user on Render's free plan (which has no shell), set the three `DJANGO_SUPERUSER_*` variables and use this Start Command once:

```
python manage.py migrate && (python manage.py createsuperuser --noinput || true) && gunicorn myapp.wsgi:application
```

After the admin user exists, delete `DJANGO_SUPERUSER_PASSWORD` from the environment.

### Moving local data to the hosted database

```bash
# Locally: export the blog data
python manage.py dumpdata blog --indent 2 --output posts.json

# On the host: load it once (temporarily add to the Start Command, then remove it)
python manage.py loaddata posts.json
```

Posts are linked to users, so make sure the user ids in the file match users that exist in the hosted database.

### Production checklist

- [x] `DEBUG = False`
- [x] `SECRET_KEY` from environment
- [x] Database credentials from environment
- [x] `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` configured
- [x] Media files stored on Cloudinary
- [ ] Static file serving configured for production (e.g. WhiteNoise)
- [ ] Email backend configured for production
- [ ] Logging configured for production

---

## 📚 API Documentation

### Base URL

```
https://blog-platform-kc5y.onrender.com/api/
```

For local development: `http://localhost:8000/api/`

### Endpoints

#### Posts

| Method      | Endpoint         | Description                                        |
| ----------- | ---------------- | -------------------------------------------------- |
| `GET`       | `/posts/`        | List all posts (paginated, searchable, filterable) |
| `POST`      | `/posts/`        | Create a new post (auth required)                  |
| `GET`       | `/posts/{slug}/` | Retrieve a single post                             |
| `PUT/PATCH` | `/posts/{slug}/` | Update a post (owner only)                         |
| `DELETE`    | `/posts/{slug}/` | Delete a post (owner only)                         |

**Query Parameters:**

- `search` - Search in title and content
- `category` - Filter by category ID

#### Categories

| Method | Endpoint            | Description         |
| ------ | ------------------- | ------------------- |
| `GET`  | `/categories/`      | List all categories |
| `GET`  | `/categories/{id}/` | Retrieve a category |

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

Use the Django admin panel at `/admin/`, or run:

```bash
python manage.py populate_categories
```

### Email Templates

Customize password reset emails in `blog/templates/blog/reset_password_email.html`

---

## 🔒 Security Notes

- Secrets (`DJANGO_SECRET_KEY`, database password, Cloudinary keys, email credentials) are read from environment variables and must never be committed to the repository.
- Set `DEBUG = False` in production.
- Keep `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` limited to your own domain.
- If a password or key is ever exposed, reset it right away and update the matching environment variable.
- Consider enabling secure cookies and HTTPS redirects:
  ```python
  SECURE_SSL_REDIRECT = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True
  ```

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

- GitHub: [@rohithkumar1104](https://github.com/rohithkumar1104)
- Email: rohithkumarm111104@gmail.com

---

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
- [Django REST Framework](https://www.django-rest-framework.org/) - Web APIs made easy
- [Bootstrap](https://getbootstrap.com/) - The most popular HTML, CSS, and JS library
- [Bootstrap Icons](https://icons.getbootstrap.com/) - Free, high quality, open source icon library
- [Render](https://render.com) - Cloud hosting for the web service
- [Enzonic Databases](https://databases.enzonic.com/dashboard) - Hosted MySQL database
- [Cloudinary](https://cloudinary.com) - Image and media storage
- [Mailtrap](https://mailtrap.io/) - Email testing for developers

---

⭐ **Star this repo if you found it helpful!**
