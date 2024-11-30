import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    try:
        st.title('Credit Card Validator and Analyzer')
        uploaded_file = st.file_uploader('Upload the credit card', type=['png', 'jpg', 'jpeg'])

        if uploaded_file is not None:
            fileName = uploaded_file.name
            st.write(f"Processing file: {fileName}")
        # Sending to blob storage, using function in services.blob_service paste
            blob_url = upload_blob(uploaded_file, fileName)
            if blob_url:
                st.write(f'File {fileName} successfully uploaded :)')
                st.image(blob_url, caption='File that was sent', use_container_width=True)
                # Sending the card for analysis and verification, using function in services.credit_card_service paste
                credit_card_info = analyze_credit_card(blob_url)
                show_image_and_validation(blob_url, credit_card_info)
            else:
                st.write(f'It was not possible to upload the file {fileName} :(')
    except Exception as e:
        st.error(f'Error during file processing: {str(e)}')


def show_image_and_validation(blob_url, credit_card_info):
  try:
    if credit_card_info and credit_card_info['card_holder_name']:
        st.markdown(f'<h1 style="color: green;">Valid credit card</h1>', unsafe_allow_html=True)
        st.write('Credit card information:')
        st.write(f'Card holder name: {credit_card_info["card_holder_name"]}')
        st.write(f'Card number: {credit_card_info["card_number"]}')
        st.write(f'Issuing bank: {credit_card_info["issuing_bank"]}')
        st.write(f'Expiration date: {credit_card_info["expiration_date"]}')
        st.write(f'Card verification value: {credit_card_info["card_verification_value"]}')
    else:
        st.markdown(f'<h1 style="color: red;">Invalid credit card</h1>', unsafe_allow_html=True)
        st.write('Invalid card, please check the credit card information.')
  except Exception as e:
    st.error(f'Error displaying results: {str(e)}')



if __name__ == "__main__":
    try:
        configure_interface()
    except Exception as e:
        st.error(f'Application error: {str(e)}')