import click
import mimetypes
import base64
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import unquote

# Function to embed images in the HTML content
def make_html_images_inline(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for img in soup.find_all('img'):
        img_src = unquote(img.attrs['src'])

        if not img_src.startswith('http'):
            with open(img_src, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
        else:
            encoded_string = base64.b64encode(requests.get(img_src).content)
        print(f"img_src : {img_src}")
        mimetype = mimetypes.guess_type(img_src)[0]
        print(f"mimetype : {mimetype}")
        # img_b64 = base64.b64encode(requests.get(img_src).content)
        img.attrs['src'] = \
            "data:%s;base64,%s" % (mimetype, encoded_string.decode('utf-8'))
    return str(soup)


@click.command(name="html-img-embedder", help="Generate HTML slides from Marp Markdown and embed images.")
@click.argument('input_html', type=click.Path(exists=True))
@click.argument('output_html_file', type=click.Path())
def main(input_html, output_html_file):
    
    print(f"pwd : {os.getcwd()}")
    print(f"context : {os.listdir()}")
    print(f"input_html : {input_html}")
    print(f"output_html_file : {output_html_file}")
    # extract cwd in a _inital_cwd variable
    _initial_cwd = os.getcwd()
    # extract base path from input_html and chenge the woking dir
    base_path = os.path.dirname(input_html)
    # if base_path is relative path then make it absolute
    if not os.path.isabs(base_path):
        base_path = os.path.abspath(base_path)
    
    
    # Read the generated HTML file
    with open(input_html, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # if _inital_cwd is not same as base_path change the working
    #  directory to base_path
    if _initial_cwd != base_path:
        os.chdir(base_path)
        print(f"Changed working directory to {base_path}")
    else:
        print(f"Working directory is already {base_path}")

    # Embed images in the HTML content
    updated_html = make_html_images_inline(html_content)
    # change cwd to initial working directory
    os.chdir(_initial_cwd)
    
    
    # Write the updated HTML content back to the file
    with open(output_html_file, 'w', encoding='utf-8') as file:
        file.write(updated_html)

    print(f"Slides generated and images embedded in {output_html_file}")

if __name__ == '__main__':
    main()
