from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Lines:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.lines = []

    def addLine(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if 0 <= x1 < self.sizeX and \
           0 <= y1 < self.sizeY and \
           0 <= x2 < self.sizeX and \
           0 <= y1 < self.sizeY:
            self.lines.append((x1, y1, x2, y2))

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor(1, 1, 1)
        glBegin(GL_LINES)
        for i in self.lines:
            x1, y1, x2, y2 = i
            glVertex(x1, y1)
            glVertex(x2, y2)
        glEnd()
        glFlush()

    def end(self, key, x, y):
        os._exit(0)

    def draw(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(self.sizeX, self.sizeY)
        glutCreateWindow("Lines".encode("ascii"))
        glOrtho(0, self.sizeX, self.sizeY, 0, -1, 1)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.end)
        glutMainLoop()

# testcode
lines = Lines(640, 480)
lines.addLine((100, 100), (500, 300))
p = (100, 200)
for i in range(100, 600, 50):
    lines.addLine(p, (i, 400))
lines.draw()
