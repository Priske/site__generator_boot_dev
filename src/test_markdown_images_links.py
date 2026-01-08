import unittest
from textnode import TextNode,TextType
from main import extract_markdown_images,extract_markdown_links,split_nodes_image,split_nodes_link


class TestMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        text = "![one](1.png) and ![two](2.jpg)"
        assert extract_markdown_images(text) == [("one", "1.png"),("two", "2.jpg"),]

    def test_extract_no_images(self):
        text = "No images here"
        assert extract_markdown_images(text) == []
    
    def test_mixed_links_and_images(self):
        text = "![img](img.png) and [link](site.com)"
        assert extract_markdown_links(text) == [("link", "site.com")]

    def test_links_and_images_together(self):
        text = "![img](a.png) [link](b.com) ![img2](c.png)"
        assert extract_markdown_images(text) == [("img", "a.png"),("img2", "c.png"),]
        assert extract_markdown_links(text) == [("link", "b.com"),]

    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                            [
                            TextNode("This is text with an ", TextType.TEXT),
                            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                            TextNode(" and another ", TextType.TEXT),
                            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                            ],new_nodes,
        )
    def test_split_nodes_image_multiple(self):
        node = TextNode("![a](1.png) and ![b](2.png)", TextType.TEXT)
        result = split_nodes_image([node])

        assert result == [
        TextNode("a", TextType.IMAGE, "1.png"),
        TextNode(" and ", TextType.TEXT),
        TextNode("b", TextType.IMAGE, "2.png"),
        ]
    def test_split_nodes_image_none(self):
        node = TextNode("Just text", TextType.TEXT)
        result = split_nodes_image([node])

        assert result == [node]
    
    def test_split_nodes_image_non_text(self):
        node = TextNode("bold", TextType.BOLD)
        result = split_nodes_image([node])

        assert result == [node]
        
    def test_split_nodes_link_single(self):
        node = TextNode("Visit [site](https://a.com) now", TextType.TEXT)
        result = split_nodes_link([node])

        assert result == [
            TextNode("Visit ", TextType.TEXT),
            TextNode("site", TextType.LINK, "https://a.com"),
            TextNode(" now", TextType.TEXT),
        ]

    def test_split_nodes_link_multiple(self):
        node = TextNode("[a](1.com) and [b](2.com)", TextType.TEXT)
        result = split_nodes_link([node])

        assert result == [
            TextNode("a", TextType.LINK, "1.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("b", TextType.LINK, "2.com"),
        ]
    def test_split_nodes_link_ignores_images(self):
        node = TextNode("![img](img.png)", TextType.TEXT)
        result = split_nodes_link([node])

        assert result == [node]