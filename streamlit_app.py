import streamlit as st
import pandas as pd
import numpy as np


st.title('Uber pickups in NYC')


import matplotlib.pyplot as plt
# Title for the Streamlit app
st.title("Random Data Histogram")
# Generate random data
data = np.random.randn(1000)
# User input for number of bins using Streamlit's slider
bins = st.slider("Choose number of bins for histogram", 10, 100, 50)

