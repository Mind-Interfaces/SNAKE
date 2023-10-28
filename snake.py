# snake.py
from OpenGL.GL import *
from OpenGL.GLUT import *

class Snake:
    """
    Class for Snake object.
    """
    def __init__(self):
        self.position = [0, 0, 0]
        self.body = [[0, 0, 0]]
        self.direction = 'UP'

    def update(self, food):
        """
        Update snake based on direction and food object.
        """
        
        # Compute the new head based on the current direction
        new_head = self.body[0][:]
        if self.direction == 'UP':
            new_head[1] += 1
        elif self.direction == 'DOWN':
            new_head[1] -= 1
        elif self.direction == 'LEFT':
            new_head[0] -= 1
        elif self.direction == 'RIGHT':
            new_head[0] += 1

        # If the snake eats the food
        if new_head == food.position:
            self.body.insert(0, new_head)
            food.randomize_position()
        else:
            # Move snake by adding new_head and removing last segment
            self.body.insert(0, new_head)
            self.body.pop()

    def draw(self):
        """
        Render the snake object.
        """
        
        # Initialize OpenGL color to green for the snake
        glColor3f(0.0, 1.0, 0.0)

        # Draw the snake body
        for segment in self.body:
            x, y, z = segment
            glPushMatrix()
            glTranslate(x, y, z)
            glutSolidCube(1)
            glPopMatrix()
