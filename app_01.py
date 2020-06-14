import streamlit as st

import numpy as np
import pandas as pd
from sklearn.datasets import load_boston

if __name__ == '__main__':

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