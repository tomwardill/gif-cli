#!/usr/bin/env python3

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='gif-cli',
    version='0.0.3',
    author='Tom Wardill',
    author_email='tom@howrandom.net',
    url="https://github.com/tomwardill/gif-cli",
    license='LICENSE',
    description='CLI tool to search for gifs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "requests",
    ],
    setup_requires=[
        "flake8"
    ],
    entry_points={
        'console_scripts': [
            'gif-cli = gifcli.gifcli:run'
        ]
    },
    packages=setuptools.find_packages(),
)
