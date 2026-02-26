from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    text = "text"
    bold_text = "**Bold text**"
    italic_text = "_Italic_"
    code_text = "`Code text`"
    link = "[anchor text](url)"
    image = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.text:
        return LeafNode(None, text_node.text, None)
    elif text_node.text_type == TextType.bold_text:
        return LeafNode("b", text_node.text, None)
    elif text_node.text_type == TextType.italic_text:
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == TextType.code_text:
        return LeafNode("code", text_node.text, None)
    elif text_node.text_type == TextType.link:
        return LeafNode("a", text_node.text, {"href":text_node.url})
    elif text_node.text_type == TextType.image:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    else: 
        raise ValueError("Not TextType")
        
    
