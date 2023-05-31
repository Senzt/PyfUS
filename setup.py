# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:55:02 2023

@author: Senzt
"""

from setuptools import setup, find_packages

setup(
    name="PyfUS",
    version="0.1",
    packages=find_packages(),
    author="Waradon Senzt Phokhinanan",
    author_email="waradonai@gmail.com",
    description="A brief description of your package",
    long_description="A longer description of your package",
    url="https://github.com/Senzt/PyfUS",
    install_requires=[
        "numpy",  # for example, if your package depends on numpy
    ],
)