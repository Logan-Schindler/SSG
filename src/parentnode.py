from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag")
        if self.children is None:
            raise ValueError("no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        attrs = ""
        if self.props:
            for key, value in self.props.items():
                attrs += f' {key}="{value}"'
        
        return f"<{self.tag}{attrs}>{children_html}</{self.tag}>"
        
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props = ""
        for key in self.props:
            props += f" {key}=\"{self.props[key]}\""
        return props

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"tag={self.tag} value={self.value} children={self.children} props={self.props_to_html}"
