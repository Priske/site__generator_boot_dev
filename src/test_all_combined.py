import unittest
from textnode import TextNode,TextType
from main import extract_markdown_images,extract_markdown_links,split_nodes_image,split_nodes_link,text_to_textnodes


class TestAllCombined(unittest.TestCase):

    def test_text_to_textnodes_full(self):
        text = (
         "This is **text** with an _italic_ word and a `code block` "
         "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
         "and a [link](https://boot.dev)"
        )

        nodes = text_to_textnodes(text)

        assert nodes == [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
    ]
        
    def test_text_to_textnodes_plain(self):
        text = "Just normal text"
        nodes = text_to_textnodes(text)

        assert nodes == [TextNode(text, TextType.TEXT)]

    def test_text_to_textnodes_formatting_only(self):
        text = "**bold** _italic_ `code`"
        nodes = text_to_textnodes(text)

        assert nodes == [
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]

    def test_text_to_textnodes_media(self):
        text = "![img](a.png) [link](b.com)"
        nodes = text_to_textnodes(text)

        assert nodes == [
            TextNode("img", TextType.IMAGE, "a.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("link", TextType.LINK, "b.com"),
        ]   

