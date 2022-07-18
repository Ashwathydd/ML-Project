from setuptools import find_packages, setup
from typing import List


#DEclaring Variable for setup functions
PROJECT_NAME="housing_predictor"
VERSION="0.0.3"
AUTHOR="Ashwathi"
DESCRIPTION="This is a first FSDS Nov batch Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """Description:This Function is going to return list of requirement mention is requirements.txt file


    Returns: This function is going to return a list which contains name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()    
)





