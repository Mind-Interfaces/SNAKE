# food.py
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from cube import CubeFace  # Assuming CubeFace Enum is defined in the cube.py file

class Food:
    """
    Class for Food object.
    """

    def __init__(self):
        # Initialize the food's position on one of the cube's faces.
        self.position = self.randomize_position()

    def randomize_position(self):
        """
        Randomize the food's position on one of the cube's faces.
        """
        # Choose a random face for the food to appear on
        face = random.choice(list(CubeFace))

        # Depending on the chosen face, set the food's position within the face's bounds
        # The Z coordinate is determined by the face, while X and Y are within face bounds
        if face == CubeFace.FRONT:
            return [random.uniform(-1, 1), random.uniform(-1, 1), -1]
        elif face == CubeFace.BACK:
            return [random.uniform(-1, 1), random.uniform(-1, 1), 1]
        # Add logic for other faces...
        # ...

    def update(self):
        """
        Regenerate food at a new location if needed.
        Here, I've assumed you would call this method when the food is eaten by the snake.
        """
        # Regenerate the food's position on one of the cube's faces.
        self.position = self.randomize_position()

    def draw(self):
        """
        Render the food object using OpenGL.
        """

        # Initialize OpenGL color to red for the food.
        glColor3f(1.0, 0.0, 0.0)

        # Translate to the food's position in 3D space and render it as a small sphere.
        glPushMatrix()
        glTranslatef(*self.position)
        glutSolidSphere(0.1, 20, 20)  # Draw food with radius 0.1
        glPopMatrix()

