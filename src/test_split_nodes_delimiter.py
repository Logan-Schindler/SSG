import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_code_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code_text)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("code block", TextType.code_text),
                TextNode(" word", TextType.text),
            ]
        )

    def test_bold_text_split_nodes_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold_text)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bold", TextType.bold_text),
                TextNode(" word", TextType.text),
            ]
        )

    def test_italic_text_split_nodes_delimiter(self):
        node = TextNode("This is text with a _italic_ word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "_", TextType.italic_text)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("italic", TextType.italic_text),
                TextNode(" word", TextType.text),
            ]
        )

    def test_delimiter_at_start_split_nodes_delimiter(self):
        node = TextNode("`This` is text with a code block", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code_text)
        self.assertEqual(
            new_nodes,
            [
                TextNode("", TextType.text),
                TextNode("This", TextType.code_text),
                TextNode(" is text with a code block", TextType.text),
            ]
        )

    def test_delimiter_at_end_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block`", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code_text)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("code block", TextType.code_text),
                TextNode("", TextType.text),
            ]
        )

    def test_two_delimiters(self):
        node = TextNode("`This` is text with a `code block`", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code_text)
        self.assertEqual(
            new_nodes,
            [
                TextNode("", TextType.text),
                TextNode("This", TextType.code_text),
                TextNode(" is text with a ", TextType.text),
                TextNode("code block", TextType.code_text),
                TextNode("", TextType.text),
            ]
        )


if __name__ == "__main__":
    unittest.main()