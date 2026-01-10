from markdown_blocks import markdown_to_blocks,markdown_to_html_node
import os

def extract_title(markdown):
    blocks =markdown_to_blocks(markdown)
    
    for block in blocks:
         b = block.strip()
         if b.startswith("# "):
              b= b[2:]
              return b.strip()

    raise Exception("No header (h1) found in markdown")

def generate_page(from_path, template_path, dest_path):
     
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    data_from= ""
    data_template=""
    with open(from_path, encoding="utf-8") as content:
            read_data = content.read()
            data_from = read_data
    with open(template_path, encoding="utf-8") as content:
            read_data = content.read()
            data_template = read_data

    nodes=markdown_to_html_node(data_from).to_html()
    title= extract_title(data_from)
    
    data_template=data_template.replace("{{ Title }}", title)
    data_template=data_template.replace("{{ Content }}", nodes)

    dir_path = os.path.dirname(dest_path)
    if  dir_path != "":
        os.makedirs(dir_path, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(data_template)

    