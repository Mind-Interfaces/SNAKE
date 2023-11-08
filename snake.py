# snake.py
from OpenGL.GL import *
from OpenGL.GLUT import *


class CubeFace(Enum):
    FRONT = 1
    BACK = 2
    LEFT = 3
    RIGHT = 4
    TOP = 5
    BOTTOM = 6


class Snake:
    """
    Class for Snake object.
    """
    def __init__(self):
        self.position = [0, 0, 0]  # The head's position
        self.body = [[0, 0, 0]]  # The segments' positions
        self.direction = 'UP'  # Initial movement direction
        self.current_face = CubeFace.FRONT  # The face of the cube the snake is currently on

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

        # Check if the snake has reached the edge of the current face
        if self.has_reached_edge(new_head):
            self.transition_face(new_head)

        # If the snake eats the food
        if new_head == food.position:
            self.body.insert(0, new_head)
            food.randomize_position()
        else:
            # Move snake by adding new_head and removing last segment
            self.body.insert(0, new_head)
            self.body.pop()

    # Define the size of each face of the cube
    face_size = 2
    
    def has_reached_edge(self, position):
        """
        Check if the snake has reached the edge of the current face.
        """
        # Using the size of the cube face to determine if the snake has reached an edge
        x, y, _ = position
        if abs(x) > self.face_size / 2 or abs(y) > self.face_size / 2:
            return True
        return False

    def transition_face(self, position):
        """
        Transition the snake to a different face of the cube.
        """
        # Calculate which face the snake should transition to
        x, y, _ = position
        if x > self.face_size / 2:
            self.current_face = CubeFace.RIGHT
            position[0] = -self.face_size / 2  # Move snake to the left edge of the new face
        elif x < -self.face_size / 2:
            self.current_face = CubeFace.LEFT
            position[0] = self.face_size / 2
        elif y > self.face_size / 2:
            self.current_face = CubeFace.TOP
            position[1] = -self.face_size / 2
        elif y < -self.face_size / 2:
            self.current_face = CubeFace.BOTTOM
            position[1] = self.face_size / 2
        
        # Correct the snake's body segments to be within the new face
        for segment in self.body:
            segment[0] = max(min(segment[0], self.face_size / 2), -self.face_size / 2)
            segment[1] = max(min(segment[1], self.face_size / 2), -self.face_size / 2)

    # ... [rest of the Snake class] ...

    def draw(self):
        """
        Render the snake object.
        """
        glColor3f(0.0, 1.0, 0.0)  # Set color to green for the snake
        for segment in self.body:
            x, y, z = segment
            glPushMatrix()
            glTranslate(x, y, z)
            glutSolidCube(1)
            glPopMatrix()

