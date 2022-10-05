#! /bin/bash

function page(){
    echo "Making Page"
    python3 ./src/pagebuilder.py
    echo "Made Page"
}

function cv(){
    echo "Making CV"
    python3 ./src/cvbuilder.py
    echo "Made CV"
}

cv
page

