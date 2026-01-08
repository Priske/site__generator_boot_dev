import unittest
from main import text_node_to_html_node
from textnode import TextNode, TextType


class TestText(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_only(self):
       
       with self.assertRaises(Exception):
           node = TextNode("text")

    def test_wrong_text_type(self):
        with self.assertRaises(Exception):
           node = TextNode("text",TextType.WRONG)

   