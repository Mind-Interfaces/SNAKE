# cube.py
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cube:
    """
    Class for Cube object.
    """
    def __init__(self):
        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        )
        self.edges = (
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7)
        )

    def draw(self):
        """
        Render the cube object.
        """
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)  # White color for the cube edges
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
