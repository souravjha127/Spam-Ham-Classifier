#%%writefile is amagic command to create app.py file
import streamlit as st
import joblib
model = joblib.load('spam-ham')
st.title('SPAM-HAM CLASSIFIER')#creates a title in web app
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
ip = st.text_input('Enter the message') #creates a text box in web app
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0]) # st.button create a button with name predict
  #st.title(op[0]) # the output will be displayed as a title
