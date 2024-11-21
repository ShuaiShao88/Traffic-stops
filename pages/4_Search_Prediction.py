import streamlit as st
import pandas as pd
import pickle

# Load pre-trained model (uncomment when available)
# with open('search_prediction_model.pkl', 'rb') as file:
#     search_model = pickle.load(file)

st.title("Traffic Stop Search Prediction")
st.write("Enter details of the traffic stop to predict if a search will be conducted.")

# Sidebar dropdown menus for the Search Prediction page
st.sidebar.header("Search Prediction Input Features")

# Helper function to get index for selectbox
def get_selectbox_index(options, value):
    if value is None or value not in options:
        return 0
    return options.index(value) + 1

# Extracted unique values for dropdown menus
cmpd_divisions = ["South Division", "Independence Division", "University City Division", "Metro Division", "Freedom Division", "Providence Division", "Westover Division", "Eastway Division", "Hickory Grove Division", "North Division", "Steele Creek Division", "North Tryon Division", "Central Division"]
reasons_for_stop = ["Speeding", "Vehicle Regulatory", "Stop Light/Sign", "Vehicle Equipment", "Other", "Safe Movement", "Investigation", "SeatBelt", "Driving While Impaired", "CheckPoint"]
driver_races = ["Asian", "White", "Black", "Other/Unknown", "Native American"]
driver_genders = ["Female", "Male"]
officer_genders = ["Male", "Female"]
driver_ethnicities = ["Non-Hispanic", "Hispanic"]

# Use values from session state to populate sidebar inputs
Driver_Age = st.sidebar.number_input("Driver Age", min_value=16, max_value=100, value=st.session_state.get('Driver_Age', None), step=1)
CMPD_Division = st.sidebar.selectbox("CMPD Division", ["Select an option"] + cmpd_divisions, index=get_selectbox_index(cmpd_divisions, st.session_state.get('CMPD_Division', None)))
Reason_for_Stop = st.sidebar.selectbox("Reason for Stop", ["Select an option"] + reasons_for_stop, index=get_selectbox_index(reasons_for_stop, st.session_state.get('Reason_for_Stop', None)))
Driver_Gender = st.sidebar.selectbox("Driver Gender", ["Select an option"] + driver_genders, index=get_selectbox_index(driver_genders, 'Male' if st.session_state.get('Driver_Gender', None) == 1 else 'Female'))
Driver_Race = st.sidebar.selectbox("Driver Race", ["Select an option"] + driver_races, index=get_selectbox_index(driver_races, st.session_state.get('Driver_Race', None)))
Officer_Gender = st.sidebar.selectbox("Officer Gender", ["Select an option"] + officer_genders, index=get_selectbox_index(officer_genders, 'Male' if st.session_state.get('Officer_Gender', None) == 1 else 'Female'))
Driver_Ethnicity = st.sidebar.selectbox("Driver Ethnicity", ["Select an option"] + driver_ethnicities, index=get_selectbox_index(driver_ethnicities, st.session_state.get('Driver_Ethnicity', None)))

# Store selected features in session state to be used by other pages
st.session_state['Driver_Age'] = Driver_Age if Driver_Age else None
st.session_state['CMPD_Division'] = CMPD_Division if CMPD_Division != "Select an option" else None
st.session_state['Reason_for_Stop'] = Reason_for_Stop if Reason_for_Stop != "Select an option" else None
st.session_state['Driver_Gender'] = 1 if Driver_Gender == 'Male' else (0 if Driver_Gender == 'Female' else None)
st.session_state['Driver_Race'] = Driver_Race if Driver_Race != "Select an option" else None
st.session_state['Officer_Gender'] = 1 if Officer_Gender == 'Male' else (0 if Officer_Gender == 'Female' else None)
st.session_state['Driver_Ethnicity'] = Driver_Ethnicity if Driver_Ethnicity != "Select an option" else None

# Prepare input data for model prediction
input_features = {
    'Driver_Age': Driver_Age if Driver_Age else None,
    'CMPD_Division': CMPD_Division if CMPD_Division != "Select an option" else None,
    'Reason_for_Stop': Reason_for_Stop if Reason_for_Stop != "Select an option" else None,
    'Driver_Gender': 1 if Driver_Gender == 'Male' else (0 if Driver_Gender == 'Female' else None),
    'Driver_Race': Driver_Race if Driver_Race != "Select an option" else None,
    'Officer_Gender': 1 if Officer_Gender == 'Male' else (0 if Officer_Gender == 'Female' else None),
    'Driver_Ethnicity': Driver_Ethnicity if Driver_Ethnicity != "Select an option" else None
}

# Remove keys with None values
input_data = pd.DataFrame([{k: v for k, v in input_features.items() if v is not None}])

# Predict
if st.button("Predict Search Conducted"):
    # Uncomment the line below when the model is loaded
    # prediction = search_model.predict(input_data)[0]
    
    # Placeholder for prediction result
    prediction = 1  # Assuming a positive outcome for placeholder
    
    if prediction == 1:
        st.write("A search is likely to be conducted during the traffic stop.")
    else:
        st.write("A search is not likely to be conducted during the traffic stop.")