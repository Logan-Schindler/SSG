import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", 'hello world', None)
        node2 = LeafNode("p", 'hello world', None)
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_not_eq(self):
        node = LeafNode("a", 'hello world', None)
        node2 = LeafNode("p", 'hello world', None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()