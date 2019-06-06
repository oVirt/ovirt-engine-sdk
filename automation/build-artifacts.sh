#!/usr/bin/bash -xe
export PYTHON=python2

if [[ $(rpm --eval "%{fedora}") -gt 29 ]] ; then
export PYTHON=python3
fi
if [[ $(rpm --eval "%{rhel}") -gt 7 ]] ; then
export PYTHON=python3
fi

${PYTHON} automation/build.py
