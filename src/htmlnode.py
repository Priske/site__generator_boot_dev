
class HTMLNode():
    def __init__(self,tag:str |None = None,value:str|None = None,children: list["HTMLNode"] | None = None,props: dict | None= None):
        self.tag = tag
        self.value=value
        self.children = children
        self.props =props

    def  to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " "+" ".join(f'{k}="{v}"' for k, v in self.props.items())
    def __repr__(self):

        return (
            f"Tag: {self.tag}\n"
            f"Value: {self.value}\n"
            f"Children: {self.children}\n"
            f"Props: {self.props}\n"
    )   
