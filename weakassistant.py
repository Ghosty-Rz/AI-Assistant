import requests
import pyttsx3

# Hugging Face API URL for the GPT-2 model
url = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer "}


def chat_with_gpt2(prompt):
    payload = {"inputs": prompt}
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set properties for the voice (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  



def speak(text):
    engine.say(text)
    engine.runAndWait()

# Interactive loop for user input
print("Welcome to your GPT-2 Assistant! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        speak("Goodbye!")
        break
    assistant_response = chat_with_gpt2(user_input)
    print("Assistant:", assistant_response)
    speak(assistant_response)  # The assistant will speak its response
