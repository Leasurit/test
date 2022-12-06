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

df = pd.read_csv('BastarCraton.csv')
x2 = df.loc('Mg')
y = df.loc('Si')
fig2, ax = plt.subplots()
ax.plot(x2, y)

st.pyplot(fig2)
