FROM quay.io/ovirt/buildcontainer:el9stream

ARG USERNAME=build
ENV USERNAME=$USERNAME

RUN dnf install -y \
    git \
    maven-openjdk21 \
    maven-local-openjdk21 \
    gcc \
    libxml2-devel \
    gnupg \
    python3 \
    python3-devel \
    python3-pip \
    && dnf clean all

RUN python3 -m pip install --upgrade pip \
    && pip3 install flake8 wheel

# Set default User
USER $USERNAME