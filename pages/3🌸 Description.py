import streamlit as st

st.markdown("# IRIS Flower Classification")

st.image('iris.png')

st.write("""This is a simple app to classify the Iris flower species using the sepal and petal lengths and widths.

We used a simple Logistic Regression model to classify the species.

Our model has an accuracy of **97.3%**.

This app is built and deployed using Streamlit.
""")

