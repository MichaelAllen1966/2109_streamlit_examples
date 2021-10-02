import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title('Power function')

# Get user to input power
power = st.slider('Power', min_value=0, max_value=5, value=1)


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

    st.pyplot(fig)

if st.button('Draw chart'):
    draw_chart()