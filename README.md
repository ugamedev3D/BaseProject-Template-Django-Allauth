# django-base

A reusable Django base project template with built-in support for Google and Facebook OAuth (via `django-allauth`), modular settings, HTMX, Whitenoise, and Django Compressor — scaffolded with a single CLI command.

---

## ✨ Features

- Google & Facebook OAuth via `django-allauth`
- Modular Django settings (`base.py`, split by environment)
- HTMX middleware pre-configured
- Django Compressor for static file bundling
- Whitenoise for static file serving (production-ready)
- Auto-generated `.env` file on project creation
- Pre-built `apps/user` and `apps/pages` apps included

---

## 📦 Requirements

- Python 3.10+
- pip

---

## 🚀 Installation

### 1. Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 2. Install the package

```bash
pip install django-baseproject
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/ugamedev3D/BaseProject-Template-Django-Allauth.git
```

### 3. Create a new project

```bash
django-base myproject
```

This will:
- Scaffold a new Django project from the base template into a `myproject/` folder
- Auto-generate a `.env` file with a random `DJANGO_SECRET_KEY` and placeholder OAuth credentials

### 4. Navigate into your project

```bash
cd myproject
```

### 5. Install project dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure your `.env` file

Open the generated `.env` file and fill in your credentials:

```env
DJANGO_SECRET_KEY=your-generated-secret-key
OAUTH_GOOGLE_CLIENT_ID=your-google-client-id
OAUTH_GOOGLE_SECRET=your-google-secret
OAUTH_FACEBOOK_CLIENT_ID=your-facebook-client-id
OAUTH_FACEBOOK_SECRET=your-facebook-secret
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

### 7. Apply migrations and run the server

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 🔑 Setting Up OAuth

### Google

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project and enable the **Google Identity** API
3. Under **Credentials**, create an **OAuth 2.0 Client ID**
4. Set the redirect URI to: `http://127.0.0.1:8000/user/accounts/google/login/callback/`
5. Copy the Client ID and Secret into your `.env`

### Facebook

1. Go to [Meta for Developers](https://developers.facebook.com/)
2. Create a new app and add the **Facebook Login** product
3. Set the redirect URI to: `http://127.0.0.1:8000/user/accounts/facebook/login/callback/`
4. Copy the App ID and Secret into your `.env`

### Gmail App Password

1. Go to your [Google Account](https://myaccount.google.com/)
2. Navigate to **Security** and enable **2-Step Verification** (required)
3. Go back to **Security** and click **App passwords**
4. Under "Select app", choose **Mail** — under "Select device", choose **Other** and name it (e.g. `Django`)
5. Click **Generate** and copy the 16-character password
6. Add your credentials to `.env`:

```env
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=xxxx xxxx xxxx xxxx
```

> ⚠️ App Passwords are only available when 2-Step Verification is enabled. If you don't see the option, make sure it's turned on first.

---

## 📁 Project Structure

```
myproject/
├── apps/
│   ├── user/               # User app (authentication)
│   └── pages/              # Pages app
├── core/
│   ├── settings/
│   │   ├── base.py         # Base Django settings
│   │   ├── development.py  # Development-specific settings
│   │   ├── production.py   # Production-specific settings
│   │   └── allauth.py      # django-allauth configuration
│   ├── urls.py
│   └── wsgi.py
├── static/                 # Project-level static files
├── staticfiles/            # collectstatic output (auto-generated)
├── templates/              # Base HTML templates
├── manage.py
└── .env                    # Auto-generated environment variables
```

---

## ⚙️ Settings Overview

The base settings (`core/settings/base.py`) include:

- **Installed apps:** `apps.user`, `apps.pages`, `compressor`, `django_htmx`, and all standard Django apps
- **Middleware:** Whitenoise and HTMX middleware pre-configured
- **Static files:** Served via Whitenoise with `CompressedManifestStaticFilesStorage` in production
- **Templates:** Loaded from the project-level `templates/` directory
- **Static finders:** Includes `CompressorFinder` for Django Compressor

> ⚠️ Run `python manage.py collectstatic` before deploying to production — Whitenoise's `CompressedManifestStaticFilesStorage` requires it.

---

## 🛠 Dependencies

| Package | Purpose |
|---|---|
| `django` | Web framework |
| `django-allauth` | Google & Facebook OAuth |
| `django-environ` | `.env` file support |
| `django-htmx` | HTMX middleware integration |
| `django-livereload` | Live reload in development |
| `django-compressor` | Static file compression & bundling |
| `whitenoise` | Static file serving |
| `pillow` | Image processing |
| `requests` | HTTP requests |

---

## 👤 Author

**Jamal Blaquera** — [ugamedev08@gmail.com](mailto:ugamedev08@gmail.com)
