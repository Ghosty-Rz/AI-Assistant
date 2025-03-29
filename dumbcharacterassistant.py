import pygame
import requests

headers = {"Authorization": "Bearer "}

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # Larger window for better layout
pygame.display.set_caption("Pygame Character with GPT-2 Subtitles")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 48, 96)
LIGHT_BLUE = (173, 216, 230)

# Load background (replace with your background image or use a solid color)
try:
    background = pygame.image.load("background.jpg")  # Replace with your background image file
    background = pygame.transform.scale(background, (800, 600))  # Resize it to fit the window
except pygame.error:
    background = pygame.Surface((800, 600))  # Fallback to a solid color if background image doesn't load
    background.fill(LIGHT_BLUE)  # Background color (light blue)

# Load character image (replace 'character.png' with your character image)
try:
    character = pygame.image.load("logowhiteaui.png")  # Replace with your character image
    character = pygame.transform.scale(character, (120, 120))  # Resize the character
except pygame.error as e:
    print(f"Error loading character image: {e}")
    character = pygame.Surface((120, 120))  # Fallback to a colored block if the image fails
    character.fill(DARK_BLUE)  # Blue block for illustration

# Hugging Face API URL for the GPT-2 model
url = "https://api-inference.huggingface.co/models/gpt2"

# GPT-2 Text Generation Function
def chat_with_gpt2(prompt):
    payload = {"inputs": prompt, "parameters": {"temperature": 0.7, "max_length": 100}}
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Initialize fonts
title_font = pygame.font.SysFont('Helvetica', 40, bold=True)
font = pygame.font.SysFont('Arial', 28)
input_font = pygame.font.SysFont('Arial', 30)

# Interactive loop
running = True
clock = pygame.time.Clock()

# User input handling
user_input = ""
assistant_response = "Waiting for input..."

while running:
    screen.blit(background, (0, 0))  # Draw the background

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # When user presses Enter, send the input to GPT-2 and get the response
                assistant_response = chat_with_gpt2(user_input)
                user_input = ""  # Clear input after submitting
            elif event.key == pygame.K_BACKSPACE:
                # Handle backspace
                user_input = user_input[:-1]
            else:
                # Handle text input
                user_input += event.unicode

    # Display the idle character at a fixed position
    screen.blit(character, (340, 230))  # Position the character in the middle

    # Display the title (e.g., "GPT-2 Assistant")
    title_surface = title_font.render("GPT-2 Assistant", True, WHITE)
    screen.blit(title_surface, (250, 50))

    # Display the GPT-2 response as subtitles
    text_surface = font.render(assistant_response, True, BLACK)
    text_rect = text_surface.get_rect(center=(400, 450))  # Center the subtitles
    pygame.draw.rect(screen, WHITE, text_rect.inflate(20, 20))  # Add a background rectangle for better readability
    screen.blit(text_surface, text_rect)

    # Display user input as text on screen with a nice background
    input_surface = input_font.render(user_input, True, BLACK)
    input_rect = input_surface.get_rect(center=(400, 520))  # Position for input text
    pygame.draw.rect(screen, WHITE, input_rect.inflate(20, 20))  # Add a background rectangle for user input
    screen.blit(input_surface, input_rect)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(30)

pygame.quit()
