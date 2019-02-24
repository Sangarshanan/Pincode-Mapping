import setuptools
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geopincoder",
    version="1.0.1",
    author="Sangarshanan",
    author_email="sangarshanan1998@gmail.com",
    description="Convert LatLongs to Pincode ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sangarshanan/Pincode-Mapping",
    packages=find_packages(exclude=('tests',)),
    package_data={
      'geopincoder': ['data/delhi.csv','data/blore.pkl','data/chennai.pkl','data/mumbai.pkl','data/ahmedabad.pkl','data/kolkatta.pkl','data/hyderabad.pkl','data/delhitree.sav'],

   }

)
