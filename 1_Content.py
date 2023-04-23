import streamlit as st
st.set_page_config(page_title="Contents ", page_icon="\U0001F4DD")
st.markdown("# Contents")
st.sidebar.header(" Contents of this app")

st.write("""
### Input variables :
1 - fixed acidity

2 - volatile acidity

3 - citric acid

4 - residual sugar

5 - chlorides

6 - free sulfur dioxide

7 - total sulfur dioxide

8 - density

9 - pH

10 - sulphates

11 - alcohol

### Output variable :
12 - quality 

### Tips
quality of 6.5 or higher can be classified as 'good/1' and the remainder as 'not good/0'.

- $quality$ > 6.5 => "good"

- TRUE => "bad"

### Inspiration
- Use machine learning to determine which physiochemical properties make a wine 'good'!
"""
)