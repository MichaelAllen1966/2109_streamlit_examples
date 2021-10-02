import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Upload csv
file = st.file_uploader('Upload a CSV file')

# Process file
def process_file(file):
    st.write(file)
    df = pd.read_csv(file)
    st.write(df)


if st.button('Process file'):
    process_file(file)

