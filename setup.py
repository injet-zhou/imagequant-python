#!/usr/bin/env python


import os

from setuptools import setup, find_packages


long_description = ""
if os.path.isfile("README.rst"):
    long_description = open("README.rst", "r").read()


setup(
    name="imagequant",
    version="0.0.0",
    description="Image Quantization Library",
    url="https://github.com/wanadev/imagequant-python",
    license="BSD-3-Clause",
    long_description=long_description,
    keywords="image libimagequant pngquant cffi",
    author="Wanadev",
    author_email="contact@wanadev.fr",
    maintainer="Fabien LOISON",
    packages=find_packages(),
    setup_requires=[
        "cffi>=1.0.0",
    ],
    install_requires=[
        "cffi>=1.0.0",
    ],
    extras_require={
        "dev": [
            "nox",
            "flake8",
            "black",
            "pytest",
        ]
    },
    cffi_modules=[
        "imagequant/libimagequant_build.py:ffibuilder",
    ],
)