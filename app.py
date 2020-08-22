import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split


def main():

    train, test, store = load_data()

    page = st.sidebar.selectbox("Choose a page", ['Homepage', 'Exploration', 'Prediction'])

	
    if page == 'Homepage':
			 	st.title('A brief Data Description  ⓿ ➀ ➁ ➂ 🔢 ')
        st.write("""This data would show the people who used our service in different stores, we would sample some rows to show 
				what the data is about but basically we have data that shows""")
        train = pd.merge(train, store, on='Store')
				test = pd.merge(test, store, on='Store')
        st.dataframe(train.sample(20))
        st.text('Select a page in the sidebar')
				
				
    elif page == 'Exploration':
        st.title('Explore Rossman Data-set')
        if st.checkbox('Show column descriptions'):
            st.dataframe(train.describe())
        
       
				
    else:
        st.title('Modelling')
        st.markdown('### Make prediction')
				df = pd.read_csv("https://iyanu2.blob.core.windows.net/unzipped/prediction.csv")
        st.dataframe(df)
        row_number = st.number_input('Select Store', min_value=1, max_value=len(df['Store'].nunique()-1), value=0)
				sub = df[df['Store']==row_number]
				start_date = st.sidebar.date_input('start date', datetime.date(2015,8,1))
        end_date = st.sidebar.date_input('end date', datetime.date(2015,9,20))
        days = (sub['Date'] > start_date) & (sub['Date'] <= end_date)
        st.markdown('#### Predicted Sales')
				dis = sub.loc[days]
				st.write(dis)



@st.cache
def load_data():
    train= pd.read_csv("https://iyanu2.blob.core.windows.net/unzipped/rossmann-store-sales/train.csv"),
		test= pd.read_csv("https://iyanu2.blob.core.windows.net/unzipped/rossmann-store-sales/test.csv"), 
		store= pd.read_csv("https://iyanu2.blob.core.windows.net/unzipped/rossmann-store-sales/store.csv")
		return train, test, store

if __name__ == '__main__':
    main()
