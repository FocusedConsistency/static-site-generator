import os
import shutil
from textnode import TextType, TextNode
from copystatic import copy_files_recursive
from gencontent import generate_page

def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    print(here)
    print(os.getcwd())
    dir_path_static = "./static"
    dir_path_public = "./public"
    print("public folder exists?")

    if os.path.exists(dir_path_public):
        print("it's there")
        print(f"about to delete: {os.path.abspath(dir_path_public)}")
        print("Deleting public directory...")
        shutil.rmtree(dir_path_public)
    else:
        print("nope")
    print("Creating public directory...")
    os.mkdir(dir_path_public)
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
