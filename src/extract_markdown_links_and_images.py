import re

def extract_markdown_links(text):
    tuple_links = []
    matches = re.findall(r"(?<!!)\[.*?\]\(.*?\)", text)
    for match in matches: 
        tuple_links.append((re.findall(r"\[.*?\]",match)[0][1:-1], re.findall(r"\(.*?\)",match)[0][1:-1]))
    return tuple_links

def extract_markdown_images(text):
    tuple_links = []
    matches = re.findall(r"!\[.*?\]\(.*?\)", text)
    for match in matches: 
        tuple_links.append((re.findall(r"\[.*?\]",match)[0][1:-1], re.findall(r"\(.*?\)",match)[0][1:-1]))
    return tuple_links
