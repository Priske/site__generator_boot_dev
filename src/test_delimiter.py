
import unittest
from textnode import TextNode,TextType
from main import split_nodes_delimiter


class TestDelimiter(unittest.TestCase):
    def test_split_code_single(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        assert result == [
        TextNode("This is ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" text", TextType.TEXT),
    ]

    def test_no_delimiter(self):
        node = TextNode("Just normal text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        assert result == [node]

    def test_non_text_node_unchanged(self):
        node = TextNode("bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        assert result == [node]

    def test_multiple_code_blocks(self):
        node = TextNode("Use `this` and `that`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        assert result == [
        TextNode("Use ", TextType.TEXT),
        TextNode("this", TextType.CODE),
        TextNode(" and ", TextType.TEXT),
        TextNode("that", TextType.CODE),
        ]

    def test_bold_text(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        assert result == [
        TextNode("This is ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text", TextType.TEXT),
        ]

    def test_chained_delimiters(self):
        node = TextNode("**bold** and `code`", TextType.TEXT)

        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

        assert nodes == [
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        ]
    def test_unmatched_delimiter_raises(self):
        node = TextNode("This is `broken", TextType.TEXT)

        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_empty_code_block(self):
        node = TextNode("``", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        assert result == []
