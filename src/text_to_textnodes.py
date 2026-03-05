from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image_link import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    text_nodes = split_nodes_delimiter([TextNode(text, TextType.text)], '**', TextType.bold_text)
    text_nodes = split_nodes_delimiter(text_nodes, '_', TextType.italic_text)
    text_nodes = split_nodes_delimiter(text_nodes, '`', TextType.code_text)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes