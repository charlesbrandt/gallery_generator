#!/bin/bash

export ROOT=/c/public/gallery_generator
launch.py -c $ROOT core
launch.py -c $ROOT todo

echo "Other common options:
launch.py -c $ROOT code
"

