import os
import shutil
import sys
from textnode import TextType, TextNode
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

def main() -> None:

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print(basepath)

    here = os.path.dirname(os.path.abspath(__file__))
    print(here)
    print(os.getcwd())
    dir_path_static = "./static"
    dir_path_content = "./content"
    dir_path_docs = "./docs"
    template = "template.html"

    print("public folder exists?")

    if os.path.exists(dir_path_docs):
        print("it's there")
        print(f"about to delete: {os.path.abspath(dir_path_docs)}")
        print("Deleting public directory...")
        shutil.rmtree(dir_path_docs)
    else:
        print("nope")
        
    print("Creating public directory...")
    os.mkdir(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template, dir_path_docs, basepath)

if __name__ == "__main__":
    main()
