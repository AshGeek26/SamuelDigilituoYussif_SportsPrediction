import streamlit as st
import joblib
import os

# # Specify the model file name and its path
# model_filename = 'RandomForestClassifier.pkl'

model_filepath = 'C:/Users/user/OneDrive - Ashesi University/Sophomore Year Semester II/Introduction to Artificial Intelligence/Fifa_Assignment/RandomForestRegressor.pkl'
# If the file path might change or you want to use a relative path, uncomment the line below
# model_filepath = os.path.join(os.path.dirname(__file__), model_filename)

def load_model(filepath):
    # Check if the file exists before loading
    if os.path.exists(filepath):
        return joblib.load(filepath)
    else:
        raise FileNotFoundError(f"Model file not found at {filepath}")

try:
    model = load_model(model_filepath)
    st.write("Model loaded successfully!")
except FileNotFoundError as e:
    st.error(str(e))
except Exception as e:
    st.error(f"An error occurred while loading the model: {str(e)}")

def main(): 

    st.title("Player Rating Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Player Rating Prediction App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Input fields for features
    potential = st.number_input("Potential", value=0.0)
    movement_reactions = st.number_input("Movement Reactions", value=0.0)
    value_in_euros = st.number_input("Value in Euros", value=0.0)
    wage_in_euros = st.number_input("Wage in Euros", value=0.0)
    passing = st.number_input("Passing Rate", value=0.0)
    dribbling = st.number_input("Dribbling", value=0.0)
    physic = st.number_input("Physic", value=0.0)
    mentality_composure = st.number_input("Mentality Composure", value=0.0)
    
    # Prediction button
    if st.button("Predict"): 
        # Create a DataFrame from user inputs
        features = [[potential, movement_reactions, value_in_euros, wage_in_euros, passing, dribbling, physic, mentality_composure]]
        df = pd.DataFrame(features, columns=['Potential', 'Movement Reactions', 'Value in Euros', 'Wage in Euros', 'Passing', 'Dribbling', 'Physic', 'Mentality Composure'])
        
        # Convert DataFrame to list of lists
        features_list = df.values.tolist()
        
        # Make prediction using the loaded model
        prediction = model.predict(features_list)
        
        # Display prediction
        st.write(f'Player Overall Rating: {prediction[0]}')
      
if __name__=='__main__': 
    main()
