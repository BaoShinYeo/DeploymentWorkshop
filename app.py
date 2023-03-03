import streamlit as st

st.set_page_config(
    page_title="App",
    page_icon="👋",
)
st.sidebar.success("Select a page above.")
st.write("# Welcome to SMUBIA Deployment Workshop! 👋")
st.write("In this workshop, we will be going through the syntax of Streamlit and learning how to build interactive and dynamic user interfaces for our machine learning models. We will also be learning how to deploy a logistic regression model on the famous iris dataset using Streamlit - a powerful Python library for building web applications.")
st.write("At the end of this workshop, you will have a fully functional web application that can predict the species of an iris flower based on its sepal length, sepal width, petal length, and petal width.")

st.header("Details")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Date: 6 Mar 2023")
with col2:
    st.write("Time: 7:00pm - 10:30pm")
with col3:
    st.write("Location: YHPSL Seminar Room 2-05")

st.header("Agenda")
st.write("1. Introduction to Streamlit")
st.write("2. Basic Syntax of Streamlit")
st.write("3. Building a User Interface for the Model")
st.write("4. Q&A and Closing Remarks")

st.header("Prerequisites")
st.write("To get the most out of this workshop, you should have a basic understanding of Python programming and machine learning concepts. You should also have the following software installed on your computer:")
st.write("- Python 3.7+")
st.write("- Streamlit")