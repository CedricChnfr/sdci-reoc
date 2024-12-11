#!/bin/bash

for dockerfile in *.dockerfile; do
    image_tag="reoc:$(basename "$dockerfile" .dockerfile)"
    
    echo "Building image: $image_tag from $dockerfile"
    docker build -t "$image_tag" -f "$dockerfile" .
done
