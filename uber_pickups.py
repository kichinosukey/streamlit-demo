import os

import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pick up in NYC')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

if __name__ == '__main__':

    DATE_COLUMN = 'date/time'
    DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

    data_load_state = st.text('Loading data...')

    data = load_data(10000)

    data_load_state.text('Done! (using st.cache)')

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)

    st.subheader('Number of pickups by hour')

    hist_values, bins = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))

    st.bar_chart(hist_values)

    hour_to_filter = st.slider('hour, 0, 23, 17')
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)