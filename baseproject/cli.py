from importlib.resources import files
from pathlib import Path
import shutil
from django.core.management.utils import get_random_secret_key

def create_project(name):
    template_dir = files("baseproject").joinpath("template")

    shutil.copytree(template_dir, name)

    # Create .env
    env_path = files(name, ".env")
    with open(env_path, "w") as f:
        f.write(f"DJANGO_SECRET_KEY={get_random_secret_key()}\n")
        f.write(f"OAUTH_GOOGLE_CLIENT_ID=google id\n")
        f.write(f"OAUTH_GOOGLE_SECRET=google secret key\n")
        f.write(f"OAUTH_FACEBOOK_CLIENT_ID=facebook id\n")
        f.write(f"OAUTH_FACEBOOK_SECRET=facebook secret key\n")
        f.write(f"EMAIL_HOST_USER=example@gmail.com\n")
        f.write(f"EMAIL_HOST_PASSWORD=**** **** **** ***\n")

    if not Path(template_dir).exists():
        raise FileNotFoundError(f"Template folder not found at {template_dir}")

    shutil.copytree(str(template_dir), name)

    print(f"Project '{name}' created successfully.")

    