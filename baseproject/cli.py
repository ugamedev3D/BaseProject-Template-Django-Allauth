import argparse
import os
import shutil
from django.core.management.utils import get_random_secret_key

def create_project():
    parser = argparse.ArgumentParser(description="Create Django base project")
    parser.add_argument("name", help="Project name")

    args = parser.parse_args()
    name = args.name

    template_dir = os.path.join(os.path.dirname(__file__), "template")
    shutil.copytree(template_dir, name)

    # Generate .env with unique SECRET_KEY
    env_path = os.path.join(name, ".env")
    with open(env_path, "w") as f:
        f.write(f"DJANGO_SECRET_KEY={get_random_secret_key()}\n")

    print(f"Project '{name}' created successfully.")