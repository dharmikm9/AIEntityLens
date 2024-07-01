#                   AIEntityLens
#   The AI system to accelerate knowledge 

##########
# LIBRARIES
##########

import streamlit as st


def get_started():
    st.switch_page('./pages/2_🪄_ner.py')
    # st.markdown('<a href="/ner" target="_self">Next page</a>', unsafe_allow_html=True)


st.set_page_config(page_title="AIEntityLens",
                   page_icon=":🕵️‍♂️:",
                   layout="wide",
                   initial_sidebar_state="collapsed"
                   )

st.sidebar.header('AIEntityLens')
st.sidebar.write("<h6 style='color: grey; font-size:14px; margin-top :-10px;'>AI-Powered Entity Discovery.</h6>",
                 unsafe_allow_html=True)



st.markdown("<h1 style='text-align: center; color: white; font-size:28px;'>Welcome to AIEntityLens!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey; font-size:20px;'>Power your discovery journey: Transform text into actionable intelligence with NER.</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-size:56px;'>🕵️</h3>", unsafe_allow_html=True)

st.markdown('___')
st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>What is this App about?<b></h3>", unsafe_allow_html=True)
st.write("Explore the power of natural language processing with our advanced NER (Named Entity Recognition) tool.")
st.write("Our web application seamlessly extracts and identifies entities such as persons, organizations, and locations from user-provided text. Whether you're analyzing news articles, academic papers, or business documents, our intuitive interface delivers accurate insights instantly. Experience streamlined data extraction and harness the efficiency of NER technology to elevate your data-driven decisions.")

if st.button("Get Started"):
    st.switch_page("./pages/2_🪄_ner.py")
# st.markdown('<a href="http://localhost:8501/ner" target="_self">Next page</a>', unsafe_allow_html=True)


#########
# SIDEBAR
########


# nav = st.sidebar.radio('', ['Home', 'Named Entity Extractor', 'Contact'])
#
# # CONTACT
# ########
# # expander = st.sidebar.expander('Contact')
# # expander.write("I'd love your feedback :smiley: Want to collaborate? Develop a project? Find me on [LinkedIn] (https://www.linkedin.com/in/lopezyse/), [Twitter] (https://twitter.com/lopezyse) and [Medium] (https://lopezyse.medium.com/)")
#
# st.sidebar.markdown('')
# st.sidebar.markdown('')
# st.sidebar.markdown('')
#
# st.sidebar.markdown(footer, unsafe_allow_html=True)
# #######
# # PAGES
# ######
#
# # HOME
# #####
#
# if nav == 'Home':
#     home_page()
#
# if nav == 'Named Entity Extractor':
#     ner()
#
# if nav == 'Contact':
#     contactus_page()
