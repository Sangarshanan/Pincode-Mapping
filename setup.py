import setuptools
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pincodicem",
    version="0.0.1",
    author="Sangarshanan",
    author_email="sangarshanan1998@gmail.com",
    description="Convert LatLongs to Pincode ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sangarshanan/Pincodicem",
    packages=find_packages(exclude=('tests',)),

)
