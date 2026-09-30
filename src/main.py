import os
import shutil
from textnode import TextType, TextNode
from copystatic import copy_files_recursive

def main() -> None:
    new_node = TextNode("This is some anchor text", TextType.LINK, "https://wikipedia.org")
    print(new_node)
    here = os.path.dirname(os.path.abspath(__file__))
    print(here)
    print(os.getcwd())
    dir_path_public = "./public"
    if os.path.exists(dir_path_public):
        print("it's there")
        print(f"about to delete: {os.path.abspath(dir_path_public)}")
        shutil.rmtree("./public")
    else:
        print("nope")
    os.mkdir("./public")
    copy_files_recursive("static", "public")

if __name__ == "__main__":
    main()
