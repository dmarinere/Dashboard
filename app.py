import streamlit as st
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="ignore")

def main():
    test, store, df = load_data()
    test = pd.merge(test, store, on='Store')

    page = st.sidebar.selectbox(
        "Choose a page", ['Homepage', 'Exploration', 'Prediction'])

    if page == 'Homepage':
        st.title('A brief Data Description')
        st.text('Select a page in the sidebar')
        st.dataframe(test.sample(20))

    elif page == 'Exploration':
        st.title('Explore Rossmann Data-set')
        if st.checkbox('Show column descriptions'):
            st.dataframe(test.describe())

    else:
        st.title('Modelling')
        st.markdown('### Make prediction')
        row_number = st.number_input('Select Store to make prediction for', min_value=0, max_value=(df['Store'].nunique()-1), value=0)
        sub = df[df['Store']  == row_number]
        st.markdown('#### Predicted Sales for store', row_number)
        st.write(sub)


@st.cache
def load_data():
    """This loads the data from the Azure File share where i saved it."""
    test = pd.read_csv(
        "https://iyanu2.blob.core.windows.net/unzipped/rossmann-store-sales/test.csv")
    store = pd.read_csv(
        "https://iyanu2.blob.core.windows.net/unzipped/rossmann-store-sales/store.csv")
    df = pd.read_csv('https://iyanu2.blob.core.windows.net/unzipped/prediction.csv')

    return test, store, df


if __name__ == '__main__':
    main()
