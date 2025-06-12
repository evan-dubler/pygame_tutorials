import pygame
from pygame.locals import *
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((639, 480))
pygame.display.set_caption('Pygame Window')

# Main loop
running = True  
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    # Fill the screen with a color
    screen.fill((255, 180, 57))  # Orange background
    # Draw a vertical black line at the center of the screen)
    pygame.draw.line(screen, (0, 0, 0), (213, 0), (213, 480), 5)
    pygame.draw.line(screen, (0, 0, 0), (426, 0), (426, 480), 5) 
    pygame.draw.line(screen, (0, 0, 0), (0, 160), (639, 160), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 320), (639, 320), 5)  
 # Update the display
    pygame.display.flip()
on_clicked=True


# Quit Pygame
pygame.quit()
sys.exit(0)
# This code initializes a Pygame window, handles events, and draws a vertical line.
# It will run until the user closes the window or presses the Escape key.   