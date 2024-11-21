# Streamlit App File
import streamlit as st

st.set_page_config(page_title="Traffic Stop Analysis App")

st.title("Traffic Stop Analysis App")

st.sidebar.success("Select a page above to navigate.")

st.write("""
This app consists of three main pages:
    
1. **Traffic Stop Search Prediction**: Predicts whether a search will be conducted during a traffic stop.
2. **Traffic Stop Outcome Prediction**: Predicts the probability of the result of the traffic stop.
    
Please use the sidebar to navigate through the pages.
""")