import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    endpoint= os.getenv('endpoint')
    doc_intelligence_key= os.getenv('doc_intelligence_key')
    azure_storage_connection_string= os.getenv('azure_storage_connection_string')
    container_name= os.getenv('container_name')