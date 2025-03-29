
import pygame
import openai
import pyttsx3

# Initialize OpenAI API
# openai.api_key = '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'  # Replace this with your actual API key


openai.api_key = ''


# Function to get response from ChatGPT
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use gpt-4 or another model as needed
        messages=[{"role": "user", "content": prompt}],  # New format requires messages
    )
    return response['choices'][0]['message']['content'].strip()

#Function to get responses from Deepseek
# client = OpenAI(api_key="<sk-e3a99a170f3348ca99ae4db8e9874e5b>", base_url="https://api.deepseek.com")
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )
# print(response.choices[0].message.content)

# Function to make the assistant speak (text-to-speech)
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Pygame setup
pygame.init()

# Create a screen (800x600 resolution)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AI Assistant")

# Load your 2D character image (make sure the image is in the same directory or provide the correct path)
character_img = pygame.image.load('character.jpg')  # Replace with the name of your image file
font = pygame.font.SysFont(None, 36)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get user input (you can change this to a GUI input later)
    user_input = input("You: ")

    # Get the response from ChatGPT
    assistant_response = chat_with_gpt(user_input)
    
    # Make the assistant speak
    speak(assistant_response)

    # Clear the screen and display the character
    screen.fill((255, 255, 255))  # White background
    screen.blit(character_img, (100, 100))  # Position the character on the screen

    # Render the assistant's response
    text_surface = font.render(assistant_response, True, (0, 0, 0))  # Black text
    screen.blit(text_surface, (100, 300))  # Position the text on the screen

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
