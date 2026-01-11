from textnode import TextNode, TextType
from copystatic import remove_dir,copy_dir
from gencontent import extract_title,generate_page, generate_pages_recursive
import sys

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    remove_dir("./docs")
    copy_dir("./static","./docs")
    generate_pages_recursive(
        "./content",
        "./template.html",
        "./docs",
        basepath,
        )


main()

