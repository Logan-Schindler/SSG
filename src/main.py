import os
import shutil
import sys

from textnode import TextNode
from pathlib import Path
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def copy_directory_to_dest(src, dest):
    # clear dest
    if not os.path.exists(dest):
        print('Destination does not exist')
        return
    shutil.rmtree(dest)
    os.mkdir(dest)
    copy_files_in_directory(src, dest)
    

def copy_files_in_directory(src, dest):
    files = os.listdir(src)
    for file in files:
        old_path = os.path.join(src, file)
        new_path = os.path.join(dest, file)
        if os.path.isfile(old_path):
            # print(f'Add file: {new_path}')
            shutil.copy(old_path, dest)
        else:
            # print(f'Add directory: {new_path}')
            os.mkdir(new_path)
            copy_files_in_directory(old_path, new_path)
    return

def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        from_markdown = f.read()
    with open(template_path, 'r') as f:
        template_html = f.read()
    content_html = markdown_to_html_node(from_markdown).to_html()
    content_title = extract_title(from_markdown)
    template_html = template_html.replace('{{ Title }}', content_title)
    template_html = template_html.replace('{{ Content }}', content_html)
    template_html = template_html.replace('href="/',f'href="{basepath}')
    template_html = template_html.replace('src="/',f'src"={basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(template_html)

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        old_path = os.path.join(dir_path_content, file)
        new_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(old_path):
            # print(f'Add file: {new_path}')
            new_path_html = os.path.join(dest_dir_path, 'index.html')
            generate_page(basepath, old_path, template_path, new_path_html) 
        else:
            # print(f'Add directory: {new_path}')
            os.mkdir(new_path)
            generate_pages_recursive(basepath, old_path, template_path, new_path)

def main(): 
    basepath = sys.argv[0] if len(sys.argv) > 0 else '/'  
    copy_directory_to_dest('/home/lschindler/projects/github.com/bootdev/SSG/static','/home/lschindler/projects/github.com/bootdev/SSG/docs')
    # generate_page('/home/lschindler/projects/github.com/bootdev/SSG/content/index.md','/home/lschindler/projects/github.com/bootdev/SSG/template.html','/home/lschindler/projects/github.com/bootdev/SSG/public/index.html')
    generate_pages_recursive(basepath, '/home/lschindler/projects/github.com/bootdev/SSG/content','/home/lschindler/projects/github.com/bootdev/SSG/template.html','/home/lschindler/projects/github.com/bootdev/SSG/docs')

main()