from block_markdown import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].lstrip().rstrip()
    raise Exception("No level 1 heading")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        index_md = f.read()

    with open(template_path) as f:
        template_html = f.read()

    content = markdown_to_html_node(index_md).to_html()
    title = extract_title(index_md)
    text = template_html.replace("{{ Title }}", title).replace("{{ Content }}", content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(text)

    
