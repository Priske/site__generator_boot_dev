from textnode import TextNode, TextType
from copystatic import remove_dir,copy_dir
from gencontent import extract_title,generate_page


def main():
    #remove_dir("./public")
    #copy_dir("./static","./public")
    generate_page("content/index.md",
                  "template.html",
                  "public/index.html")

main()

