import json
import os
from jinja2 import Environment, FileSystemLoader

def main():
    print("Loading data from data/resume.json...")
    with open('data/resume.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("Setting up Jinja2 environment...")
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')

    print("Rendering HTML...")
    rendered_html = template.render(resume=data)

    print("Writing output to index.html...")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)
        
    print("Build successful! Open index.html to view your portfolio.")

if __name__ == "__main__":
    main()
