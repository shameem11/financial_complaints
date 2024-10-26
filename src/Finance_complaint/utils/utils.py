import sys
import yaml 
import os 
from src.Finance_complaint.exception import FinaceException


#create ymal file file ath:str,data :dict 


def write_yaml(file_path:str,data:dict =None):
    try:
        os.mkdir(os.path.dirname(file_path),exit_ok = True)
        with open(file_path,'w') as yaml_file:
         if data is not None:
          yaml.dump(data,yaml_file)
    except Exception as e:
        raise FinaceException(e,Sys)
    

def read_yaml(file_path:str)-> dict:
   
 try:
      with open(file_path,'rb') as yaml_file:
         return yaml.safe_load(yaml_file)
      
 except Exception as e:
      raise FinaceException(e,sys) from e 