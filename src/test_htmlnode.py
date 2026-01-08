import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr_self(self):
        txtnode={}
        href= {"href": "https://www.google.com","target": "_blank",}
        htmlnode = HTMLNode("<p>","gestest",[txtnode],href )
        print(htmlnode)

    def test_empty_all_none(self):
        htmlnode = HTMLNode()
        assert htmlnode.props_to_html() == ""
        assert htmlnode.tag == None
        assert htmlnode.children == None
        assert htmlnode.value == None
        assert htmlnode.props == None
    
    def test_props_to_html_with_props(self):
        node = HTMLNode(
        tag="a",
        props={"href": "https://www.google.com", "target": "_blank"},
         )
        result = node.props_to_html()
        assert ' href="https://www.google.com"' in result
        assert ' target="_blank"' in result


