import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Streamlit app
st.title('Spam or Ham Classification App')

# Create a text input widget
user_input = st.text_area("Enter text for classification:", "")

if st.button("Classify"):
    if user_input:
        # Preprocess the user input using the vectorizer
        user_input_vectorized = vectorizer.transform([user_input])

        # Make predictions using the model
        prediction = model.predict(user_input_vectorized)

        # Display the prediction
        if prediction[0] == 1:
            st.warning("This message is likely spam.")
        else:
            st.success("This message is not spam.")
    else:
        st.warning("Please enter text for classification.")

