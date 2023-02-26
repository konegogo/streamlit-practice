import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('Display Image')

# if st.checkbox('Show Image'):
#     img= Image.open('KitaAlps.jpg')
#     st.image(img,caption="Mountain",use_column_width=True)

# text = st.text_input('What is your name?')
# 'Your Name :',text

st.write('show progress bar')
'Start'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done'


left_column, right_column = st.columns(2)
button= left_column.button('Right button')

if button:
    right_column.write('This is Right button')