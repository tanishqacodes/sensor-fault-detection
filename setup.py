from setuptools import find_packages, setup
from typing import List
'''
    This function will return list of requirements
'''
def get_requirements()->List[str]:
    requirement_list : List[str]= []

    '''
    Assignment 1 : write a code to read requirements.txt file and append each requiremnets in requirements_list variable.
    '''
    return requirement_list
setup(

    name="sensor",
    version="0.0.1",
    author="tanishqa",
    author_email="tanishqasharma797@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements(),#["pymongo==4.2.0"],
)

