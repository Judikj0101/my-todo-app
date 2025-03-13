import streamlit as st
import functions

todos = functions.get_todos()

st.title("My todo app")
st.subheader("My app")
st.write("This will increase your productaviy")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a now todo...")


