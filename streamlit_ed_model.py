# from numpy.lib.arraysetops import ediff1d
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import ed_sim_simpy_model as ed

st.title('Emergency Department Queuing Simulation')

col1, col2, col3 = st.columns(3)
docs = col1.slider('Number of doctors', 1, 5, 2)
inter_arrival = col2.slider(
    'Average time between patient arrivals (minutes)',1, 30, 10)
process_time = col3.slider('Average time to process patients', 5, 40, 18)

model = ed.Model(docs, inter_arrival, process_time)

if st.button('Run model'):
    # Get results
    chart, text = model.run()
    # Show chart
    st.pyplot(chart)
    # Display results (text)
    for t in text:
        st.write(t)


