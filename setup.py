#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monitor-fs",
    version="0.0.1",
    author="Alexander Mahabir",
    author_email="alex.mahabir@gmail.com",
    description="This is a small utility for monitoring write events to SQS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alex4u2nv/monitor-fs.git",
    scripts=['bin/monitor-fs'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['argparse', 'watchdog', 'boto3', 'daemons']
)
