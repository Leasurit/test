import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("First try")
st.write('Hello world')
option = st. selectbox ('My favourite fruit:', ('Strawberry', 'Raspberry', 'Blueberry'))

st.write('You chose:', option)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
