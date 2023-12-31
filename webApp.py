import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Function to load models
def load_model(model_path):
    try:
        return pickle.load(open(model_path, 'rb'))
    except FileNotFoundError:
        st.error(f"Error: The file {model_path} not found.")
        return None

# Define the file paths
diabetes_model_path = "/workspaces/multi-disease-prediction/Diabetes_RandomForest_model.sav"
heart_disease_model_path = "/workspaces/multi-disease-prediction/heart_Adaboost_model.sav"
parkinsons_model_path = "/workspaces/multi-disease-prediction/parkinsons_Stacking_Ensemble_model.sav"

# Load the models using try-except block to handle potential FileNotFoundError
diabetes_model = load_model(diabetes_model_path)
heart_disease_model = load_model(heart_disease_model_path)
parkinsons_model = load_model(parkinsons_model_path)

# Sidebar
with st.sidebar:
    st.title('Disease Prediction System')
    st.markdown("---")  # Add a horizontal line for separation
    selected = option_menu('Select Disease',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            "Parkinson's Prediction"],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
    st.subheader('Copyright©2023 :blue[Bariul Munshi] :sunglasses:')

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')
    
    # Create columns for better UI
    col1, col2, col3 = st.columns(3)

    # Input fields in the first column
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure value')

    # Input fields in the second column
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI value')
    # Input fields in the third column
    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        Age = st.text_input('Age of the Person')
    
    # Convert input values to numeric types
    try:
        Pregnancies = float(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = float(Age)
    except ValueError:
        st.error('Please enter valid numeric values.')
    #Code for prediction
    diab_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Diabetes Test Result'):   
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1): 
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic'
            
            
    st.success(diab_diagnosis)
    if diabetes_model is not None:  # Check if the model is loaded successfully
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Not Diabetic'
        st.success(diab_diagnosis)
    
    
    
            
#Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    #Page title
    st.title('Heart Disease Prediction using ML')
    
    # Create columns for better UI
    col1, col2, col3 = st.columns(3)

    # Input fields in the first column
    with col1:
        age = st.text_input('Age of the Person')
        sex = st.text_input('Sex of the Person')
        cp = st.text_input('Chest pain types')
        trestbps = st.text_input('Resting Blood Pressure')
        chol = st.text_input('Serum Cholestoral in mg/dl')
    # Input fields in the second column
    with col2:
        fbs = st.text_input('Fasting blood sugar > 120 mg/dl')
        restecg = st.text_input('Resting Electrocardiographic results')
        thalach = st.text_input('Maximum Heart Rate achieved')
        exang = st.text_input('Exercise Induced Angina')
        oldpeak = st.text_input('ST depression induced by exercise')
    # Input fields in the third column
    with col3:
        slope = st.text_input('Slope of the peak exercise ST segment')
        ca = st.text_input('Major vessels colored by flourosopy')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')
    
    # Convert input values to numeric types
    try:
        age = float(age)
        sex = float(sex)
        cp = float(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = float(fbs)
        restecg = float(restecg)
        thalach = float(thalach)
        exang = float(exang)
        oldpeak = float(oldpeak)
        slope = float(slope)
        ca = float(ca)
        thal = float(thal)
    except ValueError:
        st.error('Please enter valid numeric values for Heart Disease Prediction.')
    #Code for prediction
    heart_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person is suffering from Heart disease'
            
        else:
            heart_diagnosis = 'The person is Not suffering from Heart disease'
            
            
    st.success(heart_diagnosis)
    
    
    

    
#Parkinsons Prediction Page
if(selected == "Parkinson's Prediction"):
    
    #Page title
    st.title('Parkinsons Prediction using ML')
    

        # Create columns for better UI with a maximum of 5 inputs per column
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields in the first column
    with col1:
        fo = st.number_input('MDVP:Fo (fo)', key='fo')
        fhi = st.number_input('MDVP:Fhi (fhi)', key='fhi')
        Shimmer = st.number_input('MDVP:Shimmer (shimmer)', key='shimmer')
        APQ = st.number_input('MDVP:APQ (apq)', key='apq')
        RPDE = st.number_input('RPDE (rpde)', key='rpde')

    # Input fields in the second column
    with col2:
        flo = st.number_input('MDVP:Flo (flo)', key='flo')
        Jitter_percent = st.number_input('MDVP:Jitter (%) (jitter_percent)', key='jitter_percent')
        Shimmer_dB = st.number_input('MDVP:Shimmer (dB) (shimmer_db)', key='shimmer_db')
        DDA = st.number_input('Shimmer:DDA (dda)', key='dda')
        DFA = st.number_input('DFA (dfa)', key='dfa')

    # Input fields in the third column
    with col3:
        Jitter_Abs = st.number_input('MDVP:Jitter (Abs) (jitter_abs)', key='jitter_abs')
        RAP = st.number_input('MDVP:RAP (rap)', key='rap')
        APQ3 = st.number_input('Shimmer:APQ3 (apq3)', key='apq3')
        NHR = st.number_input('NHR (nhr)', key='nhr')
        spread1 = st.number_input('spread1 (spread1)', key='spread1')

    # Input fields in the fourth column
    with col4:
        PPQ = st.number_input('MDVP:PPQ (ppq)', key='ppq')
        DDP = st.number_input('Jitter:DDP (ddp)', key='ddp')
        APQ5 = st.number_input('Shimmer:APQ5 (apq5)', key='apq5')
        HNR = st.number_input('HNR (hnr)', key='hnr')
        spread2 = st.number_input('spread2 (spread2)', key='spread2')

    # Input fields in the fifth column
    with col5:
        # Additional inputs
        D2 = st.number_input('D2 (d2)', key='d2')
        PPE = st.number_input('PPE (ppe)', key='ppe')

        
    #Code for prediction
    parkinsons_diagnosis = ''
        
    #Creating a button for prediction
        
    if st.button('Parkinsons Test Result'):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            
            if (parkinsons_prediction[0]==1):
                parkinsons_diagnosis = 'The person is suffering from Parkinsons disease'
                
            else:
                parkinsons_diagnosis = 'The person is Not suffering from Parkinsons disease'
                
                
    st.success(parkinsons_diagnosis)
        

# For run step-2:  python -m streamlit run webApp.py   
# Learn streamlit: https://docs.streamlit.io/library/api-reference/write-magic/st.write 