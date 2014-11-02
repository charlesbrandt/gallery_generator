#!/bin/bash

export ROOT=/c/gallery_generator
python /c/mindstream/mindstream/launch.py -c $ROOT core
python /c/mindstream/mindstream/launch.py -c $ROOT todo

echo "Other common options:
python /c/mindstream/mindstream/launch.py -c $ROOT code
"

