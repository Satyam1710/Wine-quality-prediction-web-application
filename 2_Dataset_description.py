import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
red_wine=pd.read_csv(r"C:\Users\shiva\Downloads\red-wine.csv")

# print(red_wine.columns)
st.set_page_config(page_title="Dataset_description ", page_icon="\U0001F58D")
st.write("# Dataset_description")
#plt.hist(red_wine['fixed acidity'])..['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    #    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    #    'pH', 'sulphates', 'alcohol', 'quality'],


features=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
        'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
        'pH', 'sulphates']
for element in features:
    x=round(red_wine[element].mean(),2)
    y=round(red_wine[element].median(),2)
    p=red_wine[element].min()
    q=red_wine[element].max()

    st.header(element)

    #'fixed acidity'
    if element=='fixed acidity':
        st.markdown("""
        most acids involved with wine or fixed or nonvolatile (do not evaporate readily).
        """)
    #'volatile acidity'
    elif element=='volatile acidity':
        st.markdown("""
        the amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste.
        """)
    #'citric acid'
    elif element=='citric acid':
        st.markdown("""
        found in small quantities, citric acid can add 'freshness' and flavor to wines.
        """) 
    #'residual sugar'
    elif element=='residual sugar':
        st.markdown("""
        the amount of sugar remaining after fermentation stops, it's rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet.
        """)
    #'chlorides'
    elif element=='chlorides':
        st.markdown("""
        the amount of salt in the wine.
        """)
    #'free sulfur dioxide'
    elif element=='free sulfur dioxide':
        st.markdown("""
        the free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents microbial growth and the oxidation of wine.
        """)
    #'total sulfur dioxide'
    elif element=='total sulfur dioxide':
        st.markdown("""
        amount of free and bound forms of S02; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2 concentrations over 50 ppm, SO2 becomes evident in the nose and taste of wine.
        """)
    #'density'
    elif element=='density':
        st.markdown("""
        the density of water is close to that of water depending on the percent alcohol and sugar content.
        """)
    #'pH'
    elif element=='pH':
        st.markdown("""
        describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic); most wines are between 3-4 on the pH scale.
        """)
    #"sulphates"
    else:
        st.markdown("""
        a wine additive which can contribute to sulfur dioxide gas (S02) levels, wich acts as an antimicrobial and antioxidant.
        """)
    
    st.subheader("Mean")
    st.write(x)
    st.subheader("Median")
    st.write(y)
    st.subheader("Max. Value")
    st.write(q)
    st.subheader("Min. Value")
    st.write(p)

    st.subheader("Histogram")

    plt.hist(np.array(red_wine[element]))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show(),clear_figure=True)