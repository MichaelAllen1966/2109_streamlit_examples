import streamlit as st
import numpy as np
import pandas as pd
import time

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

    # When an object is on its own st.write() is assumed
    chart_data

# Use a selectbox for options
option = st.selectbox(
    'Which number do you like best?',
     [1, 3, 5, 7, 11])

'You selected: ', option


# Use a sidebar for options (appears on left)
option_2 = st.sidebar.selectbox(
    'Which number do you like best?',
     [1, 3, 5, 7, 11],
     key=2)

'You selected:', option_2

# A progress bar
'Starting a long computation...'

# Add a timer bar
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.3)

'...and now we\'re done!'