import streamlit as st
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="ignore")

def main():
    train, test, store, df = load_data()
    train = pd.merge(train, store, on='Store')
    test = pd.merge(test, store, on='Store')

    page = st.sidebar.selectbox(
        "Choose a page", ['Homepage', 'Exploration', 'Prediction'])

    if page == 'Homepage':
        st.title('A brief Data Description')
        st.text('Select a page in the sidebar')
        st.dataframe(train.sample(20))

    elif page == 'Exploration':
        st.title('Explore Rossmann Data-set')
        if st.checkbox('Show column descriptions'):
            st.dataframe(train.describe())

    else:
        st.title('Modelling')
        st.markdown('### Make prediction')
        st.dataframe(df)
        row_number = st.number_input('Select Store', min_value=1, max_value=(df['Store'].nunique()-1), value=0)
        sub = df[df['Store']  == row_number]
        sub['Date'] = pd.to_datetime(sub['Date']) 
        start_date = st.sidebar.date_input('start date', datetime.date(2015,8,1))
        end_date = st.sidebar.date_input('end date', datetime.date(2015,9,20))
        days = (sub['Date'] > start_date) & (sub['Date'] <= end_date)
        st.markdown('#### Predicted Sales')
        dis = sub.loc[days]
        st.write(dis)


@st.cache
def load_data():
    train = pd.read_csv(
        "https://iyanu2.blob.core.windows.net/unzipped/rossmann-store-sales/train.csv", low_memory=False)
    test = pd.read_csv(
        "https://iyanu2.blob.core.windows.net/unzipped/rossmann-store-sales/test.csv")
    store = pd.read_csv(
        "https://iyanu2.blob.core.windows.net/unzipped/rossmann-store-sales/store.csv")
    df = pd.read_csv('https://iyanu2.blob.core.windows.net/unzipped/prediction.csv')

    return train, test, store,df


if __name__ == '__main__':
    main()
