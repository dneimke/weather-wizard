FROM python:3.9-slim

# Add the vscode user
RUN useradd -ms /bin/bash vscode

# Switch to the root user to install git
USER root

# Install git
RUN apt-get update && apt-get install -y git

# Switch back to the vscode user
USER vscode

# Set the working directory
WORKDIR /home/vscode
