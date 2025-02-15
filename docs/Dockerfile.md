## Dockerfile Changes

### Summary

The Dockerfile has been updated to switch to the `root` user to install `git` and then switch back to the `vscode` user. This ensures that the `vscode` user does not encounter permission issues when updating package lists and installing software.

### Changes

1. Added a command to switch to the `root` user before installing `git`.
2. Added a command to switch back to the `vscode` user after installing `git`.

### Code

```dockerfile
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
