def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(lambda x: str(x.strip()), blocks))
    for block in blocks:
        if block == "":
            blocks.remove("")
    return blocks