# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

RUN apt-get clean && \
    apt-get update && \
    apt-get install -y \
                       vim \
                       git \
                       python3 \
                       python3-pip \
                       python3-dev \
                       build-essential

# Install Python packages
RUN pip install --upgrade pip setuptools wheel
RUN pip3 install --no-cache-dir build twine biopython pytest

# Copy the entrypoint file into the Docker image
COPY entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Define the entrypoint script that should be run
ENTRYPOINT ["/entrypoint.sh"]