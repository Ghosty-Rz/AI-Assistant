import requests

# Hugging Face API URL for the DeepSeek-V3-0324 model
url = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-V3-0324"
headers = {
    "Authorization": "Bearer "
} 



def chat_with_deepseek(prompt):
    # Prepare the payload with the user input
    payload = {"inputs": prompt}
    
    # Make the POST request to Hugging Face's API
    response = requests.post(url, headers=headers, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()[0]['generated_text']  # Extract the model's response
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
user_input = "What is the capital of Morocco?"
assistant_response = chat_with_deepseek(user_input)
print(assistant_response)
