import streamlit as st
import pandas as pd

#changing st layout to wide
st.set_page_config(layout="wide")
dg = pd.read_csv('data.csv')


st.title('The Best Company')
st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elits, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
st.header('Our Team')
col1, col2, col3 = st.columns(3)
with col1:
    for index, rows in dg[:4].iterrows():
        st.header(rows['first name'] + ' ' + rows['last name'])
        st.write(rows['role'])
        st.image("imgs\\" + rows['image'])

with col2:
    for index, rows in dg[4:8].iterrows():
        st.header(rows['first name'] + ' ' + rows['last name'])
        st.write(rows['role'])
        st.image("imgs\\" + rows['image'])

with col3:
    for index, rows in dg[8:].iterrows():
        st.header(rows['first name'] + ' ' + rows['last name'])
        st.write(rows['role'])
        st.image("imgs\\" + rows['image'])