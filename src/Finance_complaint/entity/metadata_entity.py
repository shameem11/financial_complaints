from src.Finance_complaint.exception import FinaceException
from src.Finance_complaint.logger import logging
import os 
import sys
from src.Finance_complaint.utils import read_yaml,write_ymal

from collections import namedtuple


DataIngestionMetadataInfo = namedtuple('DataIngestionMetadataInfo',["from_date",'to_date','data_file_path'])



class DataIngestionMetaData:

    def __init__(self,metadata_file_path):
        self.metadata_file_path = metadata_file_path


    @property
    def is_metadata_file_present(self)->bool:
        return os.path.exists(self.metadata_file_path)
    
    def write_meta_info(self,from_date:str,to_data :str,data_file_path:str):
        try:
            metadata_info = DataIngestionMetadataInfo(
                from_date = from_date,
                to_data = to_data,
                data_file_path=data_file_path
            )
            write_ymal(file_path=self.metadata_file_path,data=metadata_info._asdict())

        except Exception as e :
            raise FinaceException(e,sys)
        

    def get_metadata_info(self) -> DataIngestionMetadataInfo:
        try:
            if not self.is_metadata_file_present:
               raise Exception('No metadata file available')
           
            metadata = read_yaml(self.metadata_file_path)
            metadata_info = DataIngestionMetadataInfo(**(metadata))
            logging.info(metadata)
           
            return metadata_info
       
        except Exception as e:
           raise FinaceException(e,sys)

