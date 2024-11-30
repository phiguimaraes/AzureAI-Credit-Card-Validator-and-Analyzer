from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from configurations.Config import Config
import streamlit as st

# Using IA in Azure Document Intelligence to verify and analyze credit cards

def analyze_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.doc_intelligence_key)
        document_client = DocumentIntelligenceClient(Config.endpoint, credential)

        card_info = document_client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))
    
        result = card_info.result()

        for document in result.documents:
            fields = document.get('fields',[])

            return {
                'card_holder_name': fields.get('CardHolderName', {}).get('content'),
                'card_number': fields.get('CardNumber', {}).get('content'),
                'issuing_bank': fields.get('IssuingBank', {}).get('content'),
                'expiration_date': fields.get('ExpirationDate', {}).get('content'),
                'card_verification_value': fields.get('CardVerificationValue', {}).get('content')
            }


    except Exception as e:
        st.error(f"Detailed analysis error: {str(e)}")
        return None