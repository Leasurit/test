import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


st.title("First try")
st.write('Hello world')
option = st. selectbox ('My favourite fruit:', ('Strawberry', 'Raspberry', 'Blueberry'))
st.write('Selected:', option)

x = np.linspace(0, 50, 50)
fig1, ax = plt.subplots()
ax.plot(x, x**2)

st.pyplot(fig1)


st.write('Bastar Craton')
df = pd.read_csv('Bastar Craton.csv')

elements = ['Mg', 'Si', 'Fe']
optionx = st. selectbox ('Element x-axis:', (elements))
st.write('Selected:', optionx)
optiony = st. selectbox ('Element y-axis:', (elements))
st.write('Selected:', optiony)

x2 = df[optionx]
y = df[optiony]
fig2, ax = plt.subplots()
ax.scatter(x2, y)

st.pyplot(fig2)
