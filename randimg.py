#!/usr/bin/env python
import os
import random

_image_extentions = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".tiff",
    ".webp"
}

def _get_files(path):
    l = []
    for root, dirs, files in os.walk(path):
        # This is a very long line, please don't beat me
        l.extend([os.path.join(root, file) for file in files if any(file.endswith(ext) for ext in _image_extentions)])
    return l

def get(path):
    files = _get_files(path)
    i = random.randint(0, len(files) - 1)
    return files[i]

version = '0.1'
