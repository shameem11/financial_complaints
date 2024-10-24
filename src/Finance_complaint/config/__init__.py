import pymongo
import os 
import certifi
from Finance_complaint.constants.constant import env_var

ca = certifi.where()
mongo_clinet = pymongo.MongoClient(env_var.mongo_db_uri,tlsCAFile=ca)