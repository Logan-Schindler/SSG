import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestExtractMardownLinksAndImages(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output = text_to_textnodes(text)
        self.assertEqual(output, 
            [
                TextNode("This is ", TextType.text),
                TextNode("text", TextType.bold_text),
                TextNode(" with an ", TextType.text),
                TextNode("italic", TextType.italic_text),
                TextNode(" word and a ", TextType.text),
                TextNode("code block", TextType.code_text),
                TextNode(" and an ", TextType.text),
                TextNode("obi wan image", TextType.image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.text),
                TextNode("link", TextType.link, "https://boot.dev"),
                TextNode("", TextType.text)
            ]
        )   
    
    

if __name__ == "__main__":
    unittest.main()