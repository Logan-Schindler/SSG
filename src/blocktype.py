import re

from enum import Enum

class BlockType(Enum):
    paragraph = 'text'
    heading = '###### text'
    code = '```\ntext```'
    quote = '>text\n>text'
    unordered_list = '- text\n- text'
    ordered_list = '1. text\n2. text'

def block_to_block_type(block_markdown):
    # heading
    re_heading = re.match(r'^#{1,6} ', block_markdown)
    if re_heading is not None:
        return BlockType.heading
    # code
    re_code_block = re.match(r'^```\n[\s\S]*?```', block_markdown)
    if re_code_block is not None:
        return BlockType.code
    # split by line
    split_block_markdown = block_markdown.split('\n')
    # quote
    quote_check = True
    for line in split_block_markdown:
        if line[0] != '>':
            quote_check = False
    if quote_check:
        return BlockType.quote
    # unordered list
    unordered_list_check = True
    for line in split_block_markdown:
        re_unorderedlist = re.match(r'^- ', line)
        if re_unorderedlist is None:
            unordered_list_check = False
    if unordered_list_check:
        return BlockType.unordered_list
    # ordered list
    ordered_list_check = True
    for line in split_block_markdown:
        re_orderedlist = re.match(r'^[0-9]+. ', line)
        if re_orderedlist is None:
            ordered_list_check = False
    if ordered_list_check:
        return BlockType.ordered_list
    # paragraph
    return BlockType.paragraph

