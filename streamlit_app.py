import streamlit as st
import pandas as pd

st.title('🤖Machine learning app')

st.info('This is a app that builds a machine learning model!')

df = pd.read_csv('https://raw.githubusercontent.com/yashashree7/predictive-maintanence/refs/heads/master/streamlit_app.py')
df

