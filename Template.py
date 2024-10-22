
import os 
import logging 

#loging string 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


Project_name = "Finance_complaint"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/ml/__init__.py",
    f"src/{Project_name}/data_access/__init__.py",
    f"src/{Project_name}/config/__init__.py",
    f"src/{Project_name}/config/configuration.py",
    f"src/{Project_name}/pipeline/__init__.py",
    f"src/{Project_name}/entity/__init__.py",
    f"src/{Project_name}/constants/__init__.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]


for filepath in list_of_files:
    filedir,filenames=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f :
            pass
        logging.info(f"creating file:{filepath}")

    else:
        logging.info(f"{filenames} is already exists ")