import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")
print("1")


# Game loop
Num =0
running = True
while running:
    for event in pygame.event.get():
        print(pygame.event)
        Num=Num+1
        print("2")
        if event.type == pygame.QUIT:
            running = False
            print("3")
# Quit Pygame
print("4")
pygame.quit()
""""""