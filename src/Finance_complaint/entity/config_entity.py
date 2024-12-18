from dataclasses import dataclass
import os 
import datetime
from exception import FinaceException


#data ingection constances
DATA_INGESTION_DIR= "data_ingestion"
DATA_INGESTION_DOWNLOADED_DATA_DIR = 'download_files' 
DATA_INGESTION_FILE_NAME = 'finance_complaint'
DATA_INGESTION_FEATURE_STORE_DIR = 'feature_store'
DATA_INGESTION_FAILED_DIR = 'failed_downloaded_files'
DATA_INGESTION_FEATURE_METADATA_FILE_NAME = 'meta_yaml'
DATA_INGESTION_MIN_START_DATA = '2020-01-01'
DATA_INGESTION_DATA_SOURCE_URL =f"https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"\
                             f"?data_recevide_max<=<todate>&date_received_min=<fromdate>"\
                             f"&field=all&formate=json"
                            
                       
#training pipline config
@dataclass
class TriningPiplineconfig:
    pipeline_name:str= 'artifact'
    TIMESTAMP = datetime.now().strptime("%Y-%m-%d")
    artifact_dir:str = os.path.join(pipeline_name,TIMESTAMP)
class DataIngestionConfig:
    def __init__(self,training_pipline_config:TriningPiplineconfig,
                 from_data = DATA_INGESTION_MIN_START_DATA,
                 to_data = None):
     try:
        self.from_date= from_data
        min_start_date = datetime.strptime(DATA_INGESTION_MIN_START_DATA,"%Y-%m-%d")
        from_data_obj = datetime.strptime(from_data,"%Y-%m-%d")
        if from_data_obj < min_start_date :
            self.from_date = DATA_INGESTION_MIN_START_DATA
        if to_data is None:
            self.to_date = datetime.now().strftime("%Y-%m-%d")   

        data_ingestion_master_dir = os.path.join(os.path.dirname(os.path.dirname(training_pipline_config.artifact_dir),DATA_INGESTION_DIR))
        self.data_ingestion_dir = os.path.join(data_ingestion_master_dir,TIMESTAMP)
        self.metadata_file_path = os.path.join(data_ingestion_master_dir,DATA_INGESTION_FEATURE_METADATA_FILE_NAME)     

        data_ingestion_metadata = data_ingestion_metadata(metadata_file_path = self.metadata_file_path)
        if data_ingestion_metadata.is_metadata_file_present:
            metadata_info = data_ingestion_metadata.get_metadata_info()
            self.from_date = metadata_info.to_date

        self.download_dir = os.path.join(self.data_ingestion_dir,DATA_INGESTION_DOWNLOADED_DATA_DIR)
        self.file_name = DATA_INGESTION_FILE_NAME
        self.feature_store_dir = os.path.join(data_ingestion_master_dir,DATA_INGESTION_FEATURE_STORE_DIR)
     except Exception as e:
        raise FinaceException
