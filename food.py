# food.py
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from cube import CubeFace  # Make sure the CubeFace Enum is available in the cube.py file

class Food:
    """
    Class for Food object.
    """

    def __init__(self, cube_size):
        self.cube_size = cube_size
        self.position = self.randomize_position()
        self.face = CubeFace.FRONT

    def randomize_position(self):
        """
        Randomize the food's position on one of the cube's faces.
        """
        # Choose a random face for the food to appear on
        self.face = random.choice(list(CubeFace))
        
        # Generate coordinates within the bounds of the cube face
        x = random.uniform(-self.cube_size / 2, self.cube_size / 2)
        y = random.uniform(-self.cube_size / 2, self.cube_size / 2)

        # Map the face to a position on the cube
        if self.face == CubeFace.FRONT:
            return [x, y, -self.cube_size / 2]
        elif self.face == CubeFace.BACK:
            return [x, y, self.cube_size / 2]
        elif self.face == CubeFace.LEFT:
            return [-self.cube_size / 2, x, y]
        elif self.face == CubeFace.RIGHT:
            return [self.cube_size / 2, x, y]
        elif self.face == CubeFace.TOP:
            return [x, self.cube_size / 2, y]
        elif self.face == CubeFace.BOTTOM:
            return [x, -self.cube_size / 2, y]

    def update(self):
        """
        Regenerate food at a new location if needed.
        """
        # Regenerate the food's position on one of the cube's faces.
        self.position = self.randomize_position()

    def draw(self):
        """
        Render the food object using OpenGL.
        """
        glColor3f(1.0, 0.0, 0.0)  # Set color to red for the food
        glPushMatrix()
        glTranslate(*self.position)
        glutSolidSphere(0.1, 20, 20)  # Draw food with a small radius
        glPopMatrix()
