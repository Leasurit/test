import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("First try")
st.write('Hello world')
option = st. selectbox ('My favourite fruit:', ('Strawberry', 'Raspberry', 'Blueberry'))
st.write('Selected:', option)

x = np.linspace(0, 50, 50)
fig, ax = plt.subplots()
ax.plot(x, x**2)

st.pyplot(fig)
