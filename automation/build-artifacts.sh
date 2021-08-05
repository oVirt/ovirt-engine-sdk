#!/bin/bash -xe

# Test build sdk
export JAVA_HOME=/usr/lib/jvm/java-11

mvn package -B
