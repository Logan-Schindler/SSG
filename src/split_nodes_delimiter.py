from textnode import TextNode, TextType

# return new list of nodes, where any "text" type nodes are multiple nodes based text_type input
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for node in old_nodes:
        if node.text_type != TextType.text:
            output.append(node)
        else:
            split_node = node.text.split(delimiter)
            if len(split_node) % 2 == 0:
                raise ValueError("No closing Delimiter")
            else:
                for i in range(0,len(split_node)):
                    if i % 2 == 0:
                        output.append(TextNode(split_node[i],TextType.text))
                    else:
                        output.append(TextNode(split_node[i],text_type))
    return output

