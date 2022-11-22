from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Check whether a number is Prime or Not'
LONG_DESCRIPTION = 'A package that allows us to check whether the given number is Prime or not'

# Setting up
setup(
    name="Check Prime",
    version=VERSION,
    author="D Sai Aravind Kasyap",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages()
)
