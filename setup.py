from setuptools import find_packages , setup 
from typing import List



def get_requirements()->List[str]:
    """
    this function will return the list of requirements from requirement.txt
    
    """
    requirements_list: List[str] = []

    with open("requirements.txt") as f:
        for line in f:
            requirement = line.strip()
            if requirement and not requirement.startswith("#"):
                requirements_list.append(requirement)


    return requirements_list

setup(
    name="sensor",
    version = "0.0.1",
    author="ayhanoruc",
    author_email="ayhan.orc.2554@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements() # list of requirements
)