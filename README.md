# HTML Image Embedder

This application converts a web page with external images to one with embedded images. It reads an HTML file, fetches the external images, converts them to base64, and embeds them directly into the HTML file.

## How to Use

### Clone the Repository and  Run with `uv`

ensure that the image file are located correctly wrt the input html file. Use following command to invoke the application.

```sh
git clone <repository-url>
cd html-img-embedder
uv run html-img-embedder.py <input_markdown_file> <output_html_file>
```

### Run with Docker

#### PowerShell

```sh
docker run  --rm -v ${PWD}/mnt:/home/uv-example-user/src/mnt  htmlimgembedder:latest uv run html_img_embedder.py ./mnt/Slides_01.html ./mnt/build/Slides_01.html
```


