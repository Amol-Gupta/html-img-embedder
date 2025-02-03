# Use an official Python runtime as a parent image
FROM ghcr.io/astral-sh/uv:debian-slim

ENV USER=uv-example-user \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_DIR=/home/uv-example-user/src

ENV PYTHONPATH=$APP_DIR
# Set the working directory in the container
WORKDIR $APP_DIR

# Copy the current directory contents into the container at 
ADD ./html_img_embedder.py $APP_DIR/html_img_embedder.py
ADD ./pyproject.toml $APP_DIR/pyproject.toml
ADD ./uv.lock $APP_DIR/uv.lock
ADD ./README.md $APP_DIR/README.md
ADD ./.python-version $APP_DIR/.python-version
ADD ./.gitignore $APP_DIR/.gitignore



# Install any needed packages specified in requirements
RUN uv sync
RUN uv build
RUN uv pip install -e .
