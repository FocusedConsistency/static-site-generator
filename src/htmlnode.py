class HTMLNode:
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None = None, 
        children: list["HTMLNode"] | None = None, 
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        if self.props is None or self.props == "":
            return ""
        
        result = []
        for k, v in self.props.items():
            result.append(f' {k}="{v}"')
        
        return "".join(result)
    

    def __repr__(self) -> str:
        return f"tag: {self.tag}\n value: {self.value}\n children: {self.children}\n props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(
        self, 
        tag: str | None, 
        value: str, 
        props: dict[str, str] | None = None    
    ):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"tag: {self.tag}\n value: {self.value}\n props: {self.props}"

class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list["HTMLNode"],
        props: dict[str, str] | None = None
    ):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ERROR: tag is not found")
        
        if self.children is None:
            raise ValueError("ERROR: children not found")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
