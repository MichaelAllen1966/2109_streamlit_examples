import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# To set up a streamlit environment with SimPy available:
# conda create -n streamlit python=3.8
# conda activate streamlit
# conda install matplotlib numpy pandas
# pip install simpy streamlit

# Add a title
st.title('My first app')

# Run app from terminal with `streamlit run basic_examples.py"

# Show a dataframe
df = pd.DataFrame()
df['Name'] = ['Bill', 'Ben', 'Bob']
df['Height'] = [1.75, 1.85, 1.70]

# Use st.write to display 'stuff'
st.write("Hello world! Here is a Pandas DataFrame.....")
st.write(df)

# Show a matplotlib chart based on user input
power = st.slider('Power', min_value=0, max_value=5, value=2)

def draw_chart():

    # Calculate results
    x = np.arange(0,10.1, 0.1)
    y = x ** power

    # Draw MatPltLib chart
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label = power)
    ax.set_xlim(0,10)
    ax.set_ylim(0)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(title='Power')

    # Render chart with streamlit
    st.pyplot(fig)

if st.button('Draw chart'):
    draw_chart()

# Produce a map from random Lat Long
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    
st.map(map_data)


# Upload csv
file = st.file_uploader('Upload a CSV file')

# Process file
def process_file(file):
    st.write(file)
    df = pd.read_csv(file)
    st.write(df)


if st.button('Process file'):
    process_file(file)

