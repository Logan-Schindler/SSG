import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", 'hello world', None, None)
        node2 = HTMLNode("p", 'hello world', None, None)
        self.assertEqual(node, node2)

    def test_props_None_check(self):
        node = HTMLNode("p", "Hello world", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html(self):
        node = HTMLNode("p", "hello world", None, {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_not_eq(self):
        node = HTMLNode("a", 'hello world', None, None)
        node2 = HTMLNode("p", 'hello world', None, None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()