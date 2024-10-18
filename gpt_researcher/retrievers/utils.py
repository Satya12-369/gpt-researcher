import importlib.util
import os


def check_pkg(pkg: str) -> None:
    if not importlib.util.find_spec(pkg):
        pkg_kebab = pkg.replace("_", "-")
        raise ImportError(
            f"Unable to import {pkg_kebab}. Please install with "
            f"`pip install -U {pkg_kebab}`"
        )

# Get a list of all retriever names to be used as validators for supported retrievers
def get_all_retriever_names() -> list:
    current_dir = os.path.dirname(__file__)

    all_items = os.listdir(current_dir)
    
    # Filter out only the directories, excluding __pycache__
    directories = [item for item in all_items if os.path.isdir(os.path.join(current_dir, item))]
    
    return directories
