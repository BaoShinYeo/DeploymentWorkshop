import streamlit as st
import pickle
import pandas as pd
import time

@st.cache 
def load_model():
    with open('deploymentWorkshopModel.pkl', 'rb') as model:
        model = pickle.load(model)
    return model

def predict(features):
    with prediction_placeholder:
        with st.spinner("Please wait while our model is predicting..."):
            prediction = model.predict(features)
            time.sleep(0.1)
            flower = flowers[prediction[0]]
    st.session_state.prediction =  f"Your flower is most likely a **{flower}** flower."

"""# Iris Flower Prediction

This application helps to predict the species of the Iris flower using a Logistic Regression model.

Iris flower species are classified into three species: Setosa, Versicolor and Virginica."""

sepal_length = st.sidebar.slider("Sepal Length", min_value = 4.3, max_value = 7.9, value = 5.8, step = 0.1)
sepal_width = st.sidebar.slider("Sepal Width", min_value = 2.0, max_value = 4.4, value = 3.0, step = 0.1)
petal_length = st.sidebar.slider("Petal Length", min_value = 1.0, max_value = 6.9, value = 4.4, step = 0.1)
petal_width = st.sidebar.slider("Petal Width", min_value = 0.1, max_value = 2.5, value = 1.3, step = 0.1)

flowers = ["Setosa", "Versicolor", "Virginica"]
features = pd.DataFrame({"sepal_length": [sepal_length], "sepal_width": [sepal_width], "petal_length": [petal_length], "petal_width": [petal_width]})

st.write("### Input Features")
st.dataframe(features)

model = load_model()

prediction_placeholder = st.empty()

prediction = st.button("Predict", on_click=predict, args=(features,))

if prediction:
    st.balloons()
    st.write(st.session_state.prediction)

# if st.checkbox("Predict"):
#     st.balloons()
#     st.write(f"Your flower is most likely a **{flowers[model.predict(features)[0]]}** flower.")