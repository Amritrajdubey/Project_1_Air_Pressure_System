from setuptools import find_packages,setup

from typing import List

Requirement_File_Name = "requirements.txt"
Hypen_e_dot = "-e ."

def get_requirements() -> List[str]:
    
    with open(Requirement_File_Name) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [ requirement_name.replace("\n","") for requirement_name in requirement_list]

    if Hypen_e_dot in requirement_list:
        requirement_list.remove(Hypen_e_dot)
        return requirement_list

setup(
    name='Sensor',
    version ='0.0.1',
    author='Amrit Raj',
    author_email='amrit224raj@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)