# food.py
import random
from OpenGL.GL import *
from OpenGL.GLUT import *

class Food:
    """
    Class for Food object.
    """

    def __init__(self):
        # Initialize the food's position in 3D space using random coordinates.
        self.position = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]

    def update(self):
        """
        Regenerate food at a new location if needed.
        Here, I've assumed you would call this method when the food is eaten by the snake.
        """
        # Regenerate the food's position in 3D space using new random coordinates.
        self.position = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]

    def draw(self):
        """
        Render the food object using OpenGL.
        """

        # Initialize OpenGL color to red for the food.
        glColor3f(1.0, 0.0, 0.0)

        # Translate to the food's position in 3D space and render it using a glutSolidSphere.
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glutSolidSphere(0.1, 20, 20)
        glPopMatrix()

# Additional OpenGL setup and game loop code needed here
