import streamlit as st
from chatbot_utils import generate_response
from db_utils import fetch_extracted_text


# Streamlit app
st.title("OCR-Based Chatbot")

# Fetch the OCR text
ocr_text = fetch_extracted_text()

if ocr_text:
    st.markdown("**Context from OCR Data:**")
    st.text_area("OCR Context", ocr_text, height=400, disabled=True)

    # User input
    user_query = st.text_input("Ask a question:")

    if user_query:
        with st.spinner("Generating response..."):
            # Generate chatbot response
            response = generate_response(user_query, ocr_text)
        st.markdown("**Chatbot Response:**")
        st.write(response)
else:
    st.error("No OCR data found in the database.")
