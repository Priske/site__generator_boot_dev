from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self,tag:str,value:str, props: dict | None= None):
        super().__init__(tag,value,None,props)
    

    def to_html(self):
        if self.value == None:
          raise ValueError()
        if self.tag == None:
            return self.value
        
        if self.props:
            output=f"<{self.tag}"
            for key, value in self.props.items():
                output += f' {key}="{value}"'
            output += f">{self.value}</{self.tag}>" 
            return output  
        else:
         
            return f"<{self.tag}>{self.value}</{self.tag}>"   

    def __repr__(self):
        return (
            f"Tag: {self.tag}\n"
            f"Value: {self.value}\n"
            f"Props: {self.props}\n"
    )   
    
    