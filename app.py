import streamlit as st


st.header("Application moyenne")

x = st.number_input("note x ")
y = st.number_input("note  y")

moy = (x+y)/2

if st.button("OK"):
    st.info(moy)


