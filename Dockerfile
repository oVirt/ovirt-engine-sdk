FROM mcr.microsoft.com/devcontainers/java:11

RUN apt-get update && apt-get install -y \
    git \
    maven \
    gcc \
    libxml2-dev \
    gnupg \
    python3 \
    python3-dev \
    python3-pip \
    && apt-get clean

RUN python3 -m pip install --upgrade pip \
    && pip3 install flake8 nose wheel