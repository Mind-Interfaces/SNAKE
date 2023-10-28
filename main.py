# Import libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from snake import Snake
from food import Food

def initialize_game():
    """
    Initialize OpenGL settings and game objects.
    """
    global snake, food, constants
    pygame.init()
    # Set display size and mode
    display = (SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
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
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # Draw game objects
        snake.draw()
        food.draw()
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    initialize_game()
    game_loop()
