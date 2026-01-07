import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq_texttype(self):
        node3 =TextNode("This is a text node", TextType.ITALIC)
        node4 =TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node3,node4)
    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 =TextNode("This a grocery list", TextType.BOLD)
        self.assertNotEqual(node,node2)
    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD,"www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD,"www.google.com")
        self.assertNotEqual(node,node2)
        




if __name__ == "__main__":
    unittest.main()