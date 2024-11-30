import os
import azure.storage.blob
import streamlit as st
from configurations.Config import Config
from azure.storage.blob import BlobServiceClient

# Using container in Azure Storage Account to storage files
def upload_blob(file, file_name):
    try:
        st.write("Uploading...")
        blob_service_client = BlobServiceClient.from_connection_string(Config.azure_storage_connection_string)
        blob_client = blob_service_client.get_blob_client(container=Config.container_name, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    
    except Exception as ex:
        st.error(f"Detailed upload error: {str(ex)}")
        st.write(f"Error: {type(ex)}")
        return None