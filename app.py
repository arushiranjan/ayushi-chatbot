import streamlit as st
from PIL import Image
import tensorflow as tf  # or import torch for PyTorch models
import numpy as np

# Load the model (example with TensorFlow)
model = tf.keras.models.load_model('path_to_your_model.h5')

def predict(image, model):
    # Resize the image to the input size of the model (e.g., 224x224)
    img = image.resize((224, 224))  # Adjust to your model's input shape
    img = np.array(img)
    img = img / 255.0  # Normalize if your model expects normalized input
    img = np.expand_dims(img, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(img)
    return predictions


st.title("Image Processing Model Prediction")

# Upload an image
uploaded_file = st.file_uploader("Choose an image..." ,type=["jpg" ,"jpeg" ,"png"])

if uploaded_file is not None:
    # Open the image using PIL
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image ,caption="Uploaded Image" ,use_column_width=True)

    # Predict button
    if st.button("Predict"):
        # Run prediction
        predictions = predict(image ,model)

        # Display predictions (adjust this part to fit your model's output)
        st.write(f"Predicted class: {np.argmax(predictions)}")
        st.write(f"Prediction confidence: {np.max(predictions)}")
