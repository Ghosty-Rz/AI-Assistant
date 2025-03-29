import requests

headers = {"Authorization": "Bearer "}


# Hugging Face API URL and your API key
# url = "https://api-inference.huggingface.co/models/gpt2"  # You can replace this with another model like gpt-neo-1.3B

# Hugging Face API URL for the T5 model
# url = "https://api-inference.huggingface.co/models/t5-large"

# Deepseek
# url = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-V3-0324" #too large to use

# BERT
# url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-distilled-squad"

# BART
# url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

# Another version of deepseek
# url = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1"

# def get_model_response(prompt):
#     payload = {"inputs": prompt}
#     response = requests.post(url, headers=headers, json=payload)
    
#     if response.status_code == 200:
#         return response.json()[0]['generated_text']
#     else:
#         return f"Error: {response.status_code} - {response.text}"

# # Example usage
# user_input = "What is the capital of Morocco?"
# response = get_model_response(user_input)
# print(response)



######### GPT 2 ##########
# url = "https://api-inference.huggingface.co/models/gpt2"

# def chat_with_gpt2(prompt):
#     payload = {"inputs": prompt}
#     response = requests.post(url, headers=headers, json=payload)
    
#     if response.status_code == 200:
#         return response.json()[0]['generated_text']
#     else:
#         return f"Error: {response.status_code} - {response.text}"

# user_input = "Once upon a time"
# response = chat_with_gpt2(user_input)
# print(response)




# Hugging Face API URL for the GPT-2 model
url = "https://api-inference.huggingface.co/models/gpt2"

def chat_with_gpt2(prompt):
    payload = {"inputs": prompt, "parameters": {"temperature": 0.7, "max_length": 100}}
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Interactive loop for user input
print("Welcome to your GPT-2 Assistant! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    assistant_response = chat_with_gpt2(user_input)
    print("Assistant:", assistant_response)
