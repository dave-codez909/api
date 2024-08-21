import os
import google.generativeai as genai

# Directly set the API key or retrieve it from an environment variable
API_KEY = "AIzaSyDQNXV3aiIx4rSyz5JeaCsByknalpr5FGw"

# Configure the generative AI with the API key
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

# Generate content based on the prompt
response = model.generate_content("")

# Print the response
print(response.text)