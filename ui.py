import streamlit as st


st.title("Assignment Matcher")
st.write("##### Upload a directory link below to check which assignments are similar:")

if "url" not in st.session_state:
    st.session_state.url = ""

st.session_state.url = st.text_input("Enter the directory link", key="dir_link_main")

if st.button("Find:", key="find_btn_main"):
    if st.session_state.url:
        st.write("Found")
        from clusters import find_clusters
        find_clusters()
        st.write("_______end_______")
    else:
        st.write("No URL found / not a valid URL")