import streamlit as st


def p_title(title):
    st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>', unsafe_allow_html=True)


def hide_anchor_link(text):
    st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:22px;">{text}</h3>', unsafe_allow_html=True)

def txt(a, b):
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

def txt3(a, b):
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {

left: 0;
bottom: 0;
width: 100%;
background-color: none;
color: white;
text-align: left;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style=' text-align: left; color:white;' href="https://linkedin.com/in/dharmikm9/" target="_blank">Dharmik</a></p>
</div>
"""

a_example = 'Albert Einstein, the renowned physicist, was born in Ulm, Germany, on March 14, 1879. He is best known for his theory of relativity and the equation E=mc². Einstein spent much of his career in Berlin, where he worked at the Kaiser Wilhelm Institute for Physics. In literature, Shakespeare, the famous playwright from Stratford-upon-Avon, England, wrote numerous plays including Hamlet, Macbeth, and Romeo and Juliet. His works are still widely studied and performed worldwide. Moving to politics, Barack Obama served as the 44th President of the United States from 2009 to 2017. He was born in Honolulu, Hawaii, and studied law at Harvard University before entering politics.    '
