import re

from textnode import TextNode, TextType

# return new list of nodes, where any "text" type nodes are multiple nodes based text_type input
def split_nodes_link(old_nodes):
    output = []
    for node in old_nodes:
        if node.text_type != TextType.text:
            output.append(node)
        else: 
            text = node.text
            # Extract link
            tuple_links = []
            matches = re.findall(r"(?<!!)\[.*?\]\(.*?\)", text)
            for match in matches: 
                tuple_links.append((re.findall(r"\[.*?\]",match)[0][1:-1], re.findall(r"\(.*?\)",match)[0][1:-1]))
            # replace link with delimiter and split
            for match in matches:
                text = text.replace(match, "|")
            split_text = text.split("|")
            for i in range(0, len(split_text)):
                if i == 0:
                    output.append(TextNode(split_text[i],TextType.text))
                else:
                    output.append(TextNode(tuple_links[i-1][0],TextType.link, tuple_links[i-1][1]))                
                    output.append(TextNode(split_text[i],TextType.text))
    return output

def split_nodes_image(old_nodes):
    output = []
    for node in old_nodes:
        if node.text_type != TextType.text:
            output.append(node)
        else:
            text = node.text
            # Extract link
            tuple_links = []
            matches = re.findall(r"!\[.*?\]\(.*?\)", text)
            for match in matches: 
                tuple_links.append((re.findall(r"\[.*?\]",match)[0][1:-1], re.findall(r"\(.*?\)",match)[0][1:-1]))
            # replace link with delimiter and split
            for match in matches:
                text = text.replace(match, "|")
            split_text = text.split("|")
            for i in range(0, len(split_text)):
                if i == 0:
                    output.append(TextNode(split_text[i],TextType.text))
                else:
                    output.append(TextNode(tuple_links[i-1][0],TextType.image, tuple_links[i-1][1]))                
                    output.append(TextNode(split_text[i],TextType.text))
    return output