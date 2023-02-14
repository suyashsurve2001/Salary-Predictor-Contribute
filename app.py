import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np 
from plotly import graph_objs as go


data=pd.read_csv("Salary_Data.csv")

x = np.array(data['YearsExperience']).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data['Salary']))



st.title("Salary Predictor & Contribute")
nav = st.sidebar.radio("Navigation", ["Home","Prediction","Contribute"])

if nav =="Home":
    st.image("4537.jpg",width=500)
    if st.checkbox("show Table"):
        st.table(data)
    
    graph=st.selectbox("what kind of Graph ?",["Non-Interactive","Interactive"])

    val = st.slider("filter data using years",0,20)
    data=data.loc[data["YearsExperience"] >= val]

    if graph =="Non-Interactive":
        fig, ax = plt.subplots()
        ax.scatter(data["YearsExperience"],data["Salary"])
        ax.set_xlabel("Years of Experience")
        ax.set_ylabel("Salary")
        st.header('  Years of Experience and Salary Scatter plot ')
        st.pyplot(fig)
    
    if graph =="Interactive":
        layout =go.Layout(
            xaxis = dict(range=[0,16]),
            yaxis = dict(range =[0,210000])
        )
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode='markers'),layout = layout)
        st.plotly_chart(fig)



if nav =="Prediction":
    st.image("6212557.jpg",width=800)
    st.header("Know your Salary")
    val = st.number_input("Enter you Experience",0.00,20.00,step = 0.50)
    val = np.array(val).reshape(1,-1)
    pred =lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(pred)}")
    
    



if nav =="Contribute":
    st.image("na_april_36.jpg",width=700)
    st.header("Contribute to our Dataset")
    ex = st.number_input("Enter you Experience",0.00,20.00,step = 1.00)
    sal = st.number_input("Enter you Salary",0.00,1000000.00,step = 1000.0)
    if st.button("Submit"):
        to_add={"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("Salary_Data.csv",mode='a',header =False,index= False)
        st.success("Submitted")