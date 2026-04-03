import shutil
import os
from pathlib import Path
import argparse

def create_project():
    parser = argparse.ArgumentParser(
        description="Create a new Django project from the base template."
    )
    parser.add_argument(
        "project_name",
        type=str,
        help="The name of your new Django project folder."
    )
    parser.add_argument(
        "--destination",
        type=str,
        default=".",
        help="The destination folder (default: current directory)."
    )
    args = parser.parse_args()

    project_name = args.project_name
    destination = Path(args.destination).resolve() / project_name

    if destination.exists():
        print(f"Error: Destination {destination} already exists!")
        return

    # Locate the template folder inside the package
    package_dir = Path(__file__).parent
    template_dir = package_dir / "template"

    if not template_dir.exists():
        print(f"Error: Template folder not found at {template_dir}")
        return

    # Copy template to destination
    shutil.copytree(template_dir, destination)
    print(f"Project '{project_name}' created at {destination}")
    print("Your templates and static files have been included.")

if __name__ == "__main__":
    create_project()