import streamlit as st
import functions
st.title("My Todo WebApp")
st.subheader("This is todo list page")
st.write("This app is to increase your productivity")

for todo in functions.get_todos():
    st.checkbox(todo)

st.text_input(label="Enter a todo",placeholder="Add a todo")