import os
import re
import tkinter as tk
from tkinter import filedialog, simpledialog

def parse_markdown_structure(markdown_content):
    lines = markdown_content.split('\n')
    structure = []
    current_path = []
    
    for line in lines:
        match = re.match(r'^(#+)\s(.+)$', line)
        if match:
            level = len(match.group(1))
            title = match.group(2)
            
            while len(current_path) >= level:
                current_path.pop()
            
            current_path.append(title)
            structure.append(('/'.join(current_path), 'folder'))
        elif line.strip().startswith('- '):
            file_name = line.strip()[2:]
            structure.append(('/'.join(current_path + [file_name]), 'file'))
    
    return structure

def create_structure(base_path, structure):
    for item, item_type in structure:
        full_path = os.path.join(base_path, item)
        if item_type == 'folder':
            os.makedirs(full_path, exist_ok=True)
            print(f"Creada carpeta: {full_path}")
        elif item_type == 'file':
            open(full_path, 'a').close()
            print(f"Creado archivo: {full_path}")

def select_markdown_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    return file_path

def get_project_name():
    root = tk.Tk()
    root.withdraw()
    project_name = simpledialog.askstring("Nombre del Proyecto", "Ingrese el nombre del proyecto:")
    return project_name

def main():
    markdown_file = select_markdown_file()
    if not markdown_file:
        print("No se seleccionó ningún archivo.")
        return

    project_name = get_project_name()
    if not project_name:
        print("No se proporcionó un nombre de proyecto.")
        return

    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    structure = parse_markdown_structure(markdown_content)
    
    base_folder = os.path.dirname(markdown_file)
    project_folder = os.path.join(base_folder, project_name)
    
    os.makedirs(project_folder, exist_ok=True)
    create_structure(project_folder, structure)
    
    print(f"Estructura creada en: {project_folder}")

if __name__ == "__main__":
    main()