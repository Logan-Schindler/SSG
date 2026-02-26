from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("no value")

        if self.tag is None:
            return self.value

        attrs = ""
        if self.props:
            for key, value in self.props.items():
                attrs += f' {key}="{value}"'

        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"tag={self.tag} value={self.value} props={self.props_to_html}"
