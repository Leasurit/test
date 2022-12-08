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

#average = range(elements)/len(elements)

st.pyplot(fig2)

#from ipywidgets import interact

xls = pd.ExcelFile('data/OxAndEl2.xlsx')
sheet_names = ['Tabelle1', 'Tabelle2']
df_data = pd.read_excel('data/OxAndEl2.xlsx', sheet_name="Tabelle1",index_col="Constituent")
df_metadata = pd.read_excel('data/OxAndEl2.xlsx', sheet_name="Tabelle2")
std_names = df_data['Standard'].drop_duplicates() 

option1 = st.selectbox('Please select a standard:', (names))
st.write('Selected:', option1)

def SelectData (name):
    fil  = df_data['Standard'] == name
    return df_data.loc[fil].T
   
#interact(SelectData, name = std_names)

def SelectMetadata (name):
    fil  = df_metadata['Standard'] == name
    return df_metadata.loc[fil]
    
#interact(SelectMetadata, name = std_names)
