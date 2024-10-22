from setuptools import find_packages, setup,find_namespace_packages
from typing import List

PROJECT_NAME = "Finane_complaint"
VERSION = "0.0.1"
AUTHOR = 'mohammed Shameem'
DESCRIPTION = "Finacial complaint management"
REQUIRMENT_FILE_NAME = 'requirements.txt'


HYPHEN_E_= "-e ."

def get_requirements_list(file_path=REQUIRMENT_FILE_NAME) ->List[str]:


    with open(file_path) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list= [requirements_name.replace("\n",'') for requirements_name in requirement_list]



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)