import pygame
import random
import time
import requests
from io import BytesIO
from PIL import Image


# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
CARD_SIZE = 175
GRID_SIZE = 4
WHITE = (255, 255, 255)
FLIP_DELAY = 0.5
BUTTON_WIDTH = 140
BLACK = (0, 0, 0)
BUTTON_HEIGHT = 40
TIMER_LIMIT = 15

# URLs for images
image_urls = [
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120810/f.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311121011/d.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120802/a.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120802/b.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120801/c.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122347/z.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122913/y.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122913/x.webp"
]

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Puzzle Game")


# Load card back image from URL and convert to PNG format
#response = requests.get("https://media.geeksforgeeks.org/wp - content / uploads / 20240311145552 / geeksforgeeks.png")
#esponse = requests.get(https://media.geeksforgeeks.org/wp - content / uploads / 20240311145552 / geeksforgeeks.png)
#response = requests.get("
#response = requests.get("https://geeksforgeeks.org")
#image = Image.open(BytesIO(response.content))
#image = image.convert("RGB")


# Use the direct image URL instead of the homepage URL
#response = requests.get(
#    "https://geeksforgeeks.org"
#)

#image = Image.open(BytesIO(response.content))
#image = image.convert("RGB")

# Define a standard browser User-Agent
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

# Add the headers parameter to your request
response = requests.get(
    "https://geeksforgeeks.org",
    headers=headers,
)

# Open and convert the image
image = Image.open(BytesIO(response.content))
image = image.convert("RGB")

print("Image loaded successfully!")
"""

"""
# Use an open-access image link that doesn't block automated scripts
url = "https://picsum.photos"

response = requests.get(url)

# Open and process the image data securely
image = Image.open(BytesIO(response.content))
image = image.convert("RGB")

print("Image successfully downloaded and converted!")

with BytesIO() as img_bytes:
    image.save(img_bytes, "PNG")
    img_bytes.seek(0)
    card_back = pygame.image.load(img_bytes)
"""

"""
# Change from "https://picsum.photos" to include dimensions
url = "https://picsum.photos"

response = requests.get(url)

# Open and process the image data securely
image = Image.open(BytesIO(response.content))
image = image.convert("RGB")

print("Image successfully downloaded and converted!")

with BytesIO() as img_bytes:
    image.save(img_bytes, "PNG")
    img_bytes.seek(0)
    card_back = pygame.image.load(img_bytes)

"""


# Load card images from URLs and convert to PNG format
"""
card_images = []
for url in image_urls:
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.convert("RGB")
"""

"""
url = "https://picsum.photos"

response = requests.get(url)

# Open and process the image data securely
image = Image.open(BytesIO(response.content))
image = image.convert("RGB")

print("Image successfully downloaded and converted!")

with BytesIO() as img_bytes:
    image.save(img_bytes, "PNG")
    img_bytes.seek(0)
    card_images.append(pygame.image.load(img_bytes))
"""

"""
# Download the unrestricted placeholder image
response = requests.get("https://picsum.photos")
print("1")
# Turn the downloaded network bytes directly into a usable Pygame Surface
image_file = BytesIO(response.content)
print("2")
pygame_surface = pygame.image.load(image_file)
print("3")
"""

"""
url = "https://picsum.photos"
print("1")
response = requests.get(url)
print("2")
# Add the 'namehint' directly when loading the raw network stream
card_back = pygame.image.load(BytesIO(response.content), "image.png")
print("3")
"""

"""
url = "https://picsum.photos"
print("1")
response = requests.get(url)
print("2")
# Change this line:
# pygame_surface = pygame.image.load(image_file)

# To this (add the namehint parameter):
pygame_surface = pygame.image.load(image_file, "image.png")
print("3")
"""

"""
url = "https://picsum.photos"
print("1")
response = requests.get(url)
print("2")
# Add the 'namehint' directly when loading the raw network stream
card_back = pygame.image.load(BytesIO(response.content), "image.png")
print("3")
"""

"""
url = "https://picsum.photos"
print("1")
response = requests.get(url)
print("2")
image = Image.open(BytesIO(response.content)).convert("RGB")
print("3")
with BytesIO() as img_bytes:
    image.save(img_bytes, "PNG")
    img_bytes.seek(0)
    # Add the 'namehint' here so Pygame knows it's a PNG stream
    card_back = pygame.image.load(img_bytes, "image.png")
"""


# 1. FIXED: Added image dimensions (/200/300) to the end of the string
url = "https://picsum.photos/200/300"
print("1")

response = requests.get(url)
print("2")

# 2. This will now run cleanly because the response is a true graphic file
image = Image.open(BytesIO(response.content)).convert("RGB")
print("3")

with BytesIO() as img_bytes:
    image.save(img_bytes, "PNG")
    img_bytes.seek(0)
    card_back = pygame.image.load(img_bytes, "image.png")

print("Successfully loaded card graphic into Pygame!")





# Load card images from URLs and convert to PNG format
card_images = []
for url in image_urls:
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.convert("RGB")
    with BytesIO() as img_bytes:
        image.save(img_bytes, "PNG")
        img_bytes.seek(0)
        card_images.append(pygame.image.load(img_bytes))





# Make sure pygame is initialized first!
pygame.init()

# 1. FIXED: Define the font object here (Fixes the NameError)
# Parameters: (Font type or None for default, Font size in pixels)
font = pygame.font.SysFont(None, 36)

# --- 1. Define missing colors and dimensions ---
WHITE = (255, 255, 255)
BLUE = (0, 122, 255)
SCREEN_WIDTH = 800
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 40


# --- 2. FIXED: Define the missing functions (Fixes the NameError) ---
def draw_restart_button():
    # Calculate button position matching your click-detection math
    restart_button_rect = pygame.Rect(
        SCREEN_WIDTH - BUTTON_WIDTH - 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT
    )
    # Draw button background
    pygame.draw.rect(screen, BLUE, restart_button_rect, border_radius=5)

    # Draw button text label
    button_font = pygame.font.SysFont(None, 24)
    btn_text = button_font.render("Restart", True, WHITE)
    text_rect = btn_text.get_rect(center=restart_button_rect.center)
    screen.blit(btn_text, text_rect)


def draw_timer():
    # Placeholder to keep the next line from throwing an error
    import time
    elapsed_time = int(time.time() - timer_start_time)
    timer_text = font.render(f"Time: {elapsed_time}s", True, WHITE)
    screen.blit(timer_text, (SCREEN_WIDTH - 150, 70))

# Duplicate card images to create pairs
card_images *= 2

# Shuffle the cards
random.shuffle(card_images)

# Create a list to store the state of each card (True: face-up, False: face-down)
card_state = [False] * (GRID_SIZE ** 2)





# 1. Initialize your game variables FIRST (Add this above your main loop)
GRID_SIZE = 4                  # Adjust this to match your actual grid size
card_state = [False] * (GRID_SIZE ** 2)
flipped_cards = []
moves = 0
matched_pairs = 0
timer_start_time = time.time() # Make sure to import time at the top of your script

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # ... your event loop continues cleanly below ...
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            restart_button_rect = (
                SCREEN_WIDTH - BUTTON_WIDTH - 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
            # Turn the tuple into a real Pygame Rect object
            button_rect_obj = pygame.Rect(SCREEN_WIDTH - BUTTON_WIDTH - 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
            if button_rect_obj.collidepoint(mouse_x, mouse_y):
                random.shuffle(card_images)
                card_state = [False] * (GRID_SIZE ** 2)
                flipped_cards = []
                matched_pairs = 0
                moves = 0
                timer_start_time = time.time()  # Restart the timer
            else:
                col = mouse_x // CARD_SIZE
                row = mouse_y // CARD_SIZE
                index = row * GRID_SIZE + col
                if not card_state[index] and len(flipped_cards) < 2:
                    card_state[index] = True
                    flipped_cards.append(index)
                    moves += 1

    screen.fill(WHITE)

    # Draw grid of cards
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            index = i * GRID_SIZE + j
            pygame.draw.rect(screen, WHITE, (j * CARD_SIZE,
                                             i * CARD_SIZE, CARD_SIZE, CARD_SIZE))
            if card_state[index] or index in flipped_cards:
                card = card_images[index]
            else:
                card = card_back
            card = pygame.transform.scale(card, (CARD_SIZE - 8, CARD_SIZE - 8))
            screen.blit(card, (j * CARD_SIZE + 4, i * CARD_SIZE + 4))

    # Render moves counter
    moves_text = font.render(f"Moves: {moves}", True, WHITE)
    screen.blit(moves_text, (10, 10))

    # Draw restart game button
    draw_restart_button()

    # Draw timer
    draw_timer()



# Function to draw restart game button
def draw_restart_button():
    restart_button_rect = (SCREEN_WIDTH - BUTTON_WIDTH -
                           20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, WHITE, restart_button_rect)
    # Specify text color (black)
    restart_text = font.render("Restart Game", True, (0, 0, 0))
    text_rect = restart_text.get_rect(center=(
        restart_button_rect[0] + BUTTON_WIDTH / 2, restart_button_rect[1] + BUTTON_HEIGHT / 2))
    screen.blit(restart_text, text_rect)

# Function to draw timer
def draw_timer():
    elapsed_time = max(0, int(time.time() - timer_start_time))
    remaining_time = max(0, TIMER_LIMIT - elapsed_time)
    timer_text = font.render(f"Time: {remaining_time}s", True, BLACK)
    screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))

# Function to display message on the window
def display_message(message):
    message_text = font.render(message, True, BLACK)
    text_rect = message_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(message_text, text_rect)





# Check for matched pairs
if len(flipped_cards) == 2:
    time.sleep(FLIP_DELAY)
    if card_images[flipped_cards[0]] == card_images[flipped_cards[1]]:
        matched_pairs += 1
        flipped_cards = []
    else:
        card_state[flipped_cards[0]] = False
        card_state[flipped_cards[1]] = False
        flipped_cards = []

    # Check for game over
if matched_pairs == GRID_SIZE ** 2 // 2:
    display_message("Congratulations! You found all the pairs!")
    pygame.display.flip()
    time.sleep(2)  # Display the message for 2 seconds
    running = False

    # Check for time limit reached
elapsed_time = time.time() - timer_start_time
if elapsed_time >= TIMER_LIMIT:
    display_message("Time's up! You lost the game.")
    pygame.display.flip()
    time.sleep(2)  # Display the message for 2 seconds
    running = False

pygame.display.flip()

pygame.quit()


