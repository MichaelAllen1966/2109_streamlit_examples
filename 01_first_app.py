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