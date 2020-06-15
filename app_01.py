import time

import streamlit as st

import numpy as np
import pandas as pd
from sklearn.datasets import load_boston

if __name__ == '__main__':

    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'

    data = load_boston()
    X = data.data
    y = data.target
    columns = data.feature_names

    option = st.sidebar.selectbox(
        'Column name:',
        columns
    )

    'You selected:', option

    plot_data = np.vstack((X[:, list(columns).index(option)], y[:]))
    st.line_chart(plot_data.T)