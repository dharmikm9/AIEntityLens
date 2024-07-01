import streamlit as st
import pandas as pd

from utils.components import a_example
from nlp.ner_api import extract_entities_by_category, call_ner_api

col1, col2 = st.columns([.9,.1])
with col1:
    st.title("Named Entity Extraction", anchor=False)
with col2:
    if st.button("Back Home"):
        st.switch_page("./1_🕵️_Home.py")


input_text = st.text_area("Use the example below or input your own text in English (maximum of 1,000 characters)",
                          max_chars=1000, value=a_example, height=180)
if st.button('Analyze'):
    if len(input_text) > 1000:
        st.error('Please enter a text in English of maximum 1,000 characters')
    else:
        with st.spinner('Processing...'):
            extracted_ner_obj = call_ner_api(input_text)

        if extracted_ner_obj is None:
            st.error('Failed to retrieve entities. There was an issue processing your request. Please try again later.')
        else:
            st.subheader(f'Extracted Entities:', anchor=False)
            # Person
            st.subheader(f'Person:', anchor=False, divider="grey")
            person_entities = extract_entities_by_category(extracted_ner_obj, "person")
            df = pd.DataFrame(person_entities)
            col1, col2, col3 = st.columns([.1,.8,.1])
            with col2:
                st.dataframe(df, use_container_width=True, hide_index=True)

            # Location
            st.subheader(f'Location:', anchor=False, divider="grey")
            location_entities = extract_entities_by_category(extracted_ner_obj, "location")
            df = pd.DataFrame(location_entities)
            col1, col2, col3 = st.columns([.1,.8,.1])
            with col2:
                st.dataframe(df, use_container_width=True, hide_index=True)

            # Organization
            st.subheader(f'Organization:', anchor=False, divider="grey")
            org_entities = extract_entities_by_category(extracted_ner_obj, "organization")
            df = pd.DataFrame(org_entities)
            col1, col2, col3 = st.columns([.1,.8,.1])
            with col2:
                st.dataframe(df, use_container_width=True, hide_index=True)

            st.balloons()
