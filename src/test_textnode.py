import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold_text)
        node2 = TextNode("This is a text node", TextType.bold_text)
        self.assertEqual(node, node2)
    
    def test_eq_link(self):
        node = TextNode("This is a text node", TextType.link, "testlink")
        node2 = TextNode("This is a text node", TextType.link, "testlink")
        self.assertEqual(node, node2)

    def test_eq_image(self):
        node = TextNode("This is a text node", TextType.image, "testlink")
        node2 = TextNode("This is a text node", TextType.image, "testlink")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.image, "testlink")
        node2 = TextNode("This is a text node", TextType.link, "testlink")
        self.assertNotEqual(node,node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()