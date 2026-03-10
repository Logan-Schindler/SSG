def extract_title(markdown):
    split_markdown = markdown.split('\n')
    for line in split_markdown:
        if line[0] == '#' and line[1] == ' ':
            return line[2:].strip()
    raise ValueError("missing header")