#!/bin/bash

SCRIPT_PATH=$(realpath "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")

cd "$SCRIPT_DIR" || exit 1

for dockerfile in "$SCRIPT_DIR"/*.dockerfile; do
    image_tag="reoc:$(basename "$dockerfile" .dockerfile)"
    
    echo "Removing image: $image_tag"
    docker rmi "$image_tag" --force
done
