# Import the necessary libraries
import numpy as np
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('model.joblib')

# Create a function to predict the status based on user input
def predict_status(age, gender, weight, height):
  # Preprocess the user input
  data = np.array([[age, gender, weight, height]])
  data[:, 1] = data[:, 1].replace({
      'Female': 0,
      'Male': 1
  })
  data[:, 3] = minmax.transform(data[:, 3].reshape(-1, 1))

  # Make the prediction
  prediction = model.predict(data)[0]

  # Return the prediction
  return prediction

# Get user input
age = float(input("Enter the age (in months): "))
gender = str(input("Enter the gender (Female/Male): "))
weight = float(input("Enter the weight (in kg): "))
height = float(input("Enter the height (in cm): "))

# Predict the status
status = predict_status(age, gender, weight, height)

# Print the prediction
print(f"Predicted status: {status}")
