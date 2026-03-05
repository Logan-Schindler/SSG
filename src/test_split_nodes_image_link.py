import unittest

from textnode import TextNode, TextType
from split_nodes_image_link import split_nodes_link, split_nodes_image


class TestSplitNodesImageLink(unittest.TestCase):
    def test_split_nodes_link(self):
        text = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.text)
        output = split_nodes_link([text])
        self.assertEqual(
            output, 
            [
                TextNode("This is text with a link ", TextType.text), 
                TextNode("to boot dev", TextType.link, "https://www.boot.dev"), 
                TextNode(" and ", TextType.text), 
                TextNode("to youtube", TextType.link, "https://www.youtube.com/@bootdotdev"), 
                TextNode("", TextType.text)
            ]
        )   
    
    def test_split_nodes_image(self):
        text = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.text)
        output = split_nodes_image([text])
        self.assertEqual(
            output, 
            [
                TextNode("This is text with an ", TextType.text),
                TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.text),
                TextNode("second image", TextType.image, "https://i.imgur.com/3elNhQu.png"),
                TextNode("",TextType.text)
            ]
        )

    

if __name__ == "__main__":
    unittest.main()