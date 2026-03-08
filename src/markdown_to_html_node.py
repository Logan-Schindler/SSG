import re

from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextType, TextNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    # split markdown to blocks
    blocks = markdown_to_blocks(markdown)
    list_block_htmlnodes = []
    for block in blocks:
        # find BlockType
        block_type = block_to_block_type(block)
        # Create HTMLNode
        block_htmlnode = block_to_htmlnode(block_type, block)
        list_block_htmlnodes.append(block_htmlnode)
    # Add blocks as children to parent node and return
    return ParentNode('div', list_block_htmlnodes, None)

def block_to_htmlnode(block_type, block):
    # Steps: 
    # 1. remove block markdown
    # 2. create list of children (leaf nodes)
    # 3. Create ParentNode
    no_block_markdown = remove_block_markdown(block_type, block)
    list_children = text_to_children(block_type, no_block_markdown)
    if block_type == BlockType.paragraph:
        htmlnode = ParentNode('p', list_children, None)
    elif block_type == BlockType.heading:
        htmlnode = ParentNode(f'h{find_hash_count(block)}', list_children, None)
    elif block_type == BlockType.quote:
        htmlnode = ParentNode('blockquote', list_children, None) 
    elif block_type == BlockType.unordered_list:
        htmlnode = ParentNode('ul', list_children, None) 
    elif block_type == BlockType.ordered_list:
        htmlnode = ParentNode('ol', list_children, None) 
    else:
        htmlnode = ParentNode('pre', list_children, None) 
    return htmlnode

def find_hash_count(block):
    hash_count = 0
    for char in block:
        if char == '#':
            hash_count += 1
        else: 
            return hash_count

def remove_block_markdown(block_type, markdown):
    split_block_markdown = markdown.split('\n')
    if block_type == BlockType.paragraph:
        return markdown.replace('\n', ' ')
    elif block_type == BlockType.heading:
        return markdown[(find_hash_count(markdown)+1):]
    elif block_type == BlockType.quote:
        for index in range(0,len(split_block_markdown)):
            split_block_markdown[index] = split_block_markdown[1:]
        return '\n'.join(split_block_markdown)
    elif block_type == BlockType.unordered_list:
        for index in range(0,len(split_block_markdown)):
            split_block_markdown[index] = re.match(r'^- ', '', split_block_markdown[index])
        return '\n'.join(split_block_markdown)
    elif block_type == BlockType.ordered_list:
        for index in range(0,len(split_block_markdown)):
            split_block_markdown[index] = re.match(r'^[0-9]+. ', '', split_block_markdown[index])
        return '\n'.join(split_block_markdown)
    else:
        return markdown[4:-3]

def text_to_children(block_type, markdown):
    if block_type == BlockType.code:
        return [ParentNode('code', [text_node_to_html_node(TextNode(markdown, TextType.text))], None)]
    # markdown to textnodes
    # textnode to htmlnodes
    textnodes = text_to_textnodes(markdown)
    child_nodes = []
    for textnode in textnodes:
        child_nodes.append(text_node_to_html_node(textnode))
    return child_nodes
