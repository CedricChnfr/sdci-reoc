#!/bin/bash

for dockerfile in *.dockerfile; do
    image_tag="reoc:$(basename "$dockerfile" .dockerfile)"
    
    echo "Removing image: $image_tag"
    docker rmi "$image_tag" --force
done
