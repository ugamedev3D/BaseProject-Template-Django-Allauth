# Django Base Project Template

A reusable, production-ready Django starter template designed for rapid development.
Includes preconfigured authentication, social login (Google & Facebook), and clean environment-based settings.

---

## Features

* ✅ Preconfigured Django project structure
* ✅ Environment-based settings (`.env`) for development
* ✅ Auto-generated `SECRET_KEY` per project for development
* ✅ Integrated authentication system
* ✅ Social login via Google & Facebook
* ✅ Customs Setting setup by By [Vitor Freitas](https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html)
* ✅ CLI tool to generate new projects (like `django-admin startproject`)
---

## Installation

Install directly from Git:

```bash
pip install git+https://github.com/ugamedev3D/Base-Project-Template-Django-Allauth.git
```

---

## Usage

Create a new project:

```bash
django-base myproject
```

Then:

```bash
cd myproject
python manage.py migrate
python manage.py runserver
```

---

## Environment Configuration

Each project includes a `.env` file:

```env
DJANGO_SECRET_KEY=your-generated-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Notes:

* `SECRET_KEY` is automatically generated
* Never commit `.env` to Git
* Use environment variables in production

---

## Authentication System

This template includes:

* Django authentication
* Email login support
* Social authentication via **Google** and **Facebook**

Powered by: django-allauth

---

## Social Login Setup

### 1. Google OAuth Setup

Go to: [Google Cloud Console](https://console.cloud.google.com?utm_source=chatgpt.com)

#### Steps:

1. Create a new project
2. Enable **OAuth consent screen**
3. Add scopes:

   * email
   * profile
4. Create **OAuth Client ID**
5. Add redirect URI:

```text
http://127.0.0.1:8000/user/account/google/login/callback/
```

#### Add to `.env`:

```env
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_SECRET=your-secret
```

---

### 2. Facebook Login Setup

Go to: [Meta for Developers](https://developers.facebook.com?utm_source=chatgpt.com)

#### Steps:

1. Create an app
2. Add **Facebook Login** product
3. Configure OAuth redirect URI:

```text
http://127.0.0.1:8000/user/accounts/facebook/login/callback/
```

4. Get:

   * App ID
   * App Secret

#### Add to `.env`:

```env
FACEBOOK_APP_ID=your-app-id
FACEBOOK_SECRET=your-secret
```

---

## Django Settings Highlights

### Dynamic SECRET_KEY

```python
from django.core.management.utils import get_random_secret_key
import os

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
```

---

### Installed Apps

```python
INSTALLED_APPS = [
    "apps.user",

    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
]
```

---

### Authentication Backends

```python
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
```

---

---

## Migrations

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Development Tips

* Use `.env` for all secrets
* Keep settings modular (`base.py`, `development.py`, `production.py`)
* Enable logging early
* Use SQLite for development, PostgreSQL for production

---

## Project Structure

```
myproject/
├── .env
├── manage.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
```

---

## Why This Template?

This base project eliminates repetitive setup and enforces:

* Secure defaults
* Scalable architecture
* Fast onboarding for new projects

---

## Future Improvements

* Docker support
* CI/CD integration
* Prebuilt API modules
* Role-based auth system

---

## License

MIT License

---

## Author

Jamal Blaquera

---

## Support

If this project helps you, consider giving it a star on GitHub.
