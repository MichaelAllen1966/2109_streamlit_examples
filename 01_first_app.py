import streamlit as st
import numpy as np
import pandas as pd

# Add a title
st.title('My first app')

# Show a dataframe
df = pd.DataFrame()
df['Name'] = ['Bill', 'Ben', 'Bob']
df['Height'] = [1.75, 1.85, 1.70]

# Use st.write to display 'stuff'
st.write("Hello world! Here is a Pandas DataFrame.....")
st.write(df)

# Produce a chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Produce a map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Add a checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data