import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="App",
    page_icon="\U0001F377"
)

st.write("# Welcome to Wine Quality Prediction Web App!"+"\U0001F377")
st.sidebar.success("Some thing more")
# ("\U0001F44B" for hello and "\U0001F377"  for wine)
image=Image.open(r"C:\Users\shiva\Downloads\red-wine-1502122953qXg.jpg")
image=image.resize((400,400))
st.image(image,caption="Red Wine")
st.markdown(
    """
   # This is a Wines quality prediction web app....
    
    **👈Selcect given slides from sidebar** to see something more

    ### Links of Datasets
    -Dataset Link no.1 [Kaggel.dataset_link]  (https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

    -Dataset Link no.2 [UCI.repository.dataset_link]  (https://archive.ics.uci.edu/ml/datasets/wine+quality)
    """
)