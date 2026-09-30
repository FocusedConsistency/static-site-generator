from block_markdown import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].lstrip().rstrip()
    raise Exception("No level 1 heading")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        index_md = f.read()

    with open(template_path) as f:
        template_html = f.read()

    content = markdown_to_html_node(index_md).to_html()
    title = extract_title(index_md)
    text = template_html.replace("{{ Title }}", title).replace("{{ Content }}", content)
    text = text.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(text)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for name in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, name)

        if os.path.isfile(path):
            dest_file_path = os.path.join(dest_dir_path, f"{name[:-3]}.html")
            generate_page(path, template_path, dest_file_path, basepath)
        else:
            dest_dir_path_folder = os.path.join(dest_dir_path, name)
            if not os.path.exists(dest_dir_path_folder):
                os.mkdir(dest_dir_path_folder)
            generate_pages_recursive(path, template_path, dest_dir_path_folder, basepath)
    
