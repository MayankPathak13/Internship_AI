import pandas as pd
import streamlit as st
import pickle;


model = pickle.load('file')

st.title("Bedroom price prediction")

area = st.number_input("enter the area")

def prediction(area):
    p = model.predict([[area]])
    return p
if(st.button('predict')):
    result = prediction(area)

st.success("the predicted price is {}".format(result))


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# # import pillow as pil

# st.title('hello AI/ML ')
# st.subheader('Data sets')



# st.success('Hello')
