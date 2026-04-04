import os
import shutil
from django.core.management.utils import get_random_secret_key

def create_project(name):
    template_dir = os.path.join(os.path.dirname(__file__), "template")

    shutil.copytree(template_dir, name)

    # Create .env
    env_path = os.path.join(name, ".env")
    with open(env_path, "w") as f:
        f.write(f"DJANGO_SECRET_KEY={get_random_secret_key()}\n")

    print(f"Project '{name}' created successfully.")