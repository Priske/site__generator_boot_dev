from textnode import TextNode, TextType
from copystatic import remove_dir,copy_dir
from gencontent import extract_title,generate_page, generate_pages_recursive


def main():

    #generate_page("content/index.md",
    #              "template.html",
    #              "public/index.html")
    generate_pages_recursive("content",
                  "template.html",
                  "public")


main()

