import streamlit as st

st.title("Developer Contact Info", anchor=False)

col1, col2 = st.columns([.5, .5])

with col1:
    st.markdown(
        """<style>.stImage > img {max-width: 100%;height: auto;}.stImage > .fullScreenIcon {display: none !important;}</style>""",
        unsafe_allow_html=True)
    st.image("https://kit8.net/wp-content/uploads/edd/2022/04/robots_and_humans_communication_preview.jpg")

with col2:
    st.header("Meet the Developer", anchor=False)
    st.write("""
        Hello! I'm Dharmik, a passionate developer interested in Machine Learning & ML.
        Feel free to connect with me through the following social media platforms:
        """)

    soc_col1, soc_col2 = st.columns([1, 3])

    with soc_col1:
        st.markdown(
            "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/dharmikm9)"
        )
    with soc_col2:
        st.markdown(
            "[![GitHub](https://img.shields.io/badge/GitHub-Profile-lightgrey)](https://github.com/dharmikm9)"
        )
