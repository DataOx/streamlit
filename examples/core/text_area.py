import streamlit as st

i1 = st.text_area('text area 1')
st.write('value 1: "', i1, '"')

i2 = st.text_area('text area 2', 'default text')
st.write('value 2: "', i2, '"')

i3 = st.text_area('text area 3', 1234)
st.write('value 3: "', i3, '"')

i4 = st.text_area('text area 4', None)
st.write('value 4: "', i4, '"')