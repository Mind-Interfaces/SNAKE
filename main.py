# Import libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

from snake import Snake  # Make sure the Snake class is in the same directory or properly imported
from food import Food  # Make sure the Food class is in the same directory or properly imported
from cube import Cube  # Make sure the Cube class is in the same directory or properly imported

def initialize_game():
    """
    Initialize OpenGL settings and game objects.
    """
    global snake, food, constants
    pygame.init()
    # Set display size and mode
    display = (SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Configure initial OpenGL settings
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    
    # Initialize snake and food objects
    snake = Snake()
    food = Food()

def game_loop():
    """
    The main game loop.
    """
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Update game objects
        snake.update(food)
        food.update()
        
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw game objects
        cube.draw()  # Make sure the cube is drawn in the correct context
        snake.draw()
        food.draw()
        
        # Update the display
        pygame.display.flip()
        
        # Delay to create animation effect
        pygame.time.wait(10)

if __name__ == "__main__":
    initialize_game()
    game_loop()

