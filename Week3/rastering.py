from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math 

GRID_SIZE = 10

class Grid:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.points = []

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT) 
        for i in self.points:
            x, y, c = i
            if type(c) == tuple:
                glColor(*c)
            else:
                glColor(c, c, c)
            glRectf(x * GRID_SIZE, y * GRID_SIZE, (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE)
        glColor(.5, .5, .5)
        glBegin(GL_LINES)
        for i in range(1, self.sizeX):
            glVertex(i * GRID_SIZE, 0)
            glVertex(i * GRID_SIZE, self.sizeY * GRID_SIZE)
        for i in range(1, self.sizeY):
            glVertex(0, i * GRID_SIZE)
            glVertex(self.sizeX * GRID_SIZE, i * GRID_SIZE)
        glEnd()
        glFlush()

    def end(self, key, x, y):
        os._exit(0)

    def draw(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(self.sizeX * GRID_SIZE, self.sizeY * GRID_SIZE)
        glutCreateWindow("Raster".encode("ascii"))
        glOrtho(0, self.sizeX * GRID_SIZE, self.sizeY * GRID_SIZE, 0, -1, 1)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.end)
        glutMainLoop()

    def addPoint(self, x, y, c = 1):
        if 0 <= x < self.sizeX and 0 <= y < self.sizeY:
            x = round(x)
            y = round(y)
            self.points.append((x, y, c))

        
    def rasterline(self, x0, y0, x2, y2):
        #wat wil ik doen
        grid.addPoint(x0,y0)
        grid.addPoint(x2,y2)
        deltax = int
        deltay = int
        octant = int
         
        deltax = x2 - x0
        deltay = y2 - y0
        ocant = math.degrees(math.atan(deltay/deltax))

        print(ocant)
         
        
        # to do
        pass

# testcode
# let op: de beoordeling wordt gedaan op basis van andere waarden
grid = Grid(20, 20)

grid.rasterline(0,2,4,8) 
#grid.rasterline(5, 0, 19, 19)
#grid.rasterline(0, 10, 19, 0)
grid.draw()
