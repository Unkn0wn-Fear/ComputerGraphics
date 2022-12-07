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
        
    def rasterline(self, x1, y1, x2, y2):
        deltax = x2 - x1
        deltay = y2 - y1

        deltax1 = abs(deltax);
        deltay1 = abs(deltay);

        px = 2 * deltay1 - deltax1;
        py = 2 * deltax1 - deltay1;

        D = (2*deltay) - deltax
        y = y1

        if (deltay1 <= deltax1):
            if (deltax >= 0): 
                x = x1; y = y1; xe = x2;
            else: 
                x = x2; y = y2; xe = x1;
            
            grid.addPoint(x, y)
            while x < xe :
                x = x + 1;
                if (px < 0): 
                    px = px + 2 * deltay1
                else:
                    if ((deltax < 0 and deltay < 0) or (deltax > 0 and deltay > 0)):
                        y = y + 1
                    else:
                        y = y - 1
                    px = px + 2 * (deltay1 - deltax1)
                grid.addPoint(x,y)
             
        
                 
        else:
            if (deltay >= 0):
                x = x1; y = y1; ye = y2
            else:
                x = x2; y = y2; ye = y1
            grid.addPoint(x,y)

            while x < ye:
                y = y + 1
                if (py <= 0):
                    py = py + 2 * deltax1
                else:
                    if ((deltax < 0 and deltay<0) or (deltax > 0 and deltay > 0)):
                        x = x + 1
                    else:
                        x = x - 1
                    py = py + 2 * (deltay1 - deltax1)
                grid.addPoint(x,y)
              
        pass

# testcode
# let op: de beoordeling wordt gedaan op basis van andere waarden
grid = Grid(50, 50)
#grid.rasterline(0, 0, 19, 19)
grid.addPoint( 10,5)
grid.addPoint(19,40)
grid.rasterline(10, 5, 19, 20)
grid.draw()
