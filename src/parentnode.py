from htmlnode import HTMLNode



class ParentNode(HTMLNode):

    def __init__(self,tag:str,children:list["HTMLNode"],value:str |None = None,  props: dict | None= None):
        super().__init__(tag,value,children,props)
    

    def to_html(self):
        if self.tag is None:
          raise ValueError("Tag must be given")
        if self.children is None:
            raise ValueError("Must have children")
        
        output = f"<{self.tag}>"

        for child in self.children:
            output += child.to_html()
        output +=f"</{self.tag}>"
        return output
    


            

