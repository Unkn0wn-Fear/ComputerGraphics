from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

import numpy as np

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
        
    def rasterline(self, x0, y0, x1, y1):
        #voor meer informatie over hoe de formule werkt bezoek https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
        # controleerd of het verschil van delta y kleiner dan delta x is
        if abs(y1- y0) < abs(x1 - x0):
            if x0 > x1:
                # calculate the difference
                dx = x1 - x0
                dy = y1 - y0

                yi = 1
                if dy < 0:
                    yi = -1
                    dy = -dy
                
                d = (2 * dy) - dx
                y = y0

                for x in range(x0, x1 + 1):
                    grid.addPoint(x, y)
                    if d > 0:
                        y = y + yi
                        d = d + (2 * (dy - dx))
                    else:
                        d = d + 2 * dy
            else:
             
                dx = x0 - x1
                dy = y0 - y1

                yi = 1
                if dy < 0:
                    yi = -1
                    dy = -dy
                
                d = (2 * dy) - dx
                y = y1

                for x in range(x0, x1 + 1):
                    grid.addPoint(x, y)
                    if d > 0:
                        y = y + yi
                        d = d + (2 * (dy - dx))
                    else:
                        d = d + 2 * dy
        else:
            if y0 > y1:
                dx = x0 - x1
                dy = y0 - y1

                xi = 1
                if dx < 0:
                    xi = -1
                    dx = -dx
                
                d = (2 * dx) - dy
                x = x1

                for y in range(y1, y0 + 1):
                    grid.addPoint(x, y)
                    if d > 0:
                        x = x + xi
                        d = d + (2 * (dx - dy))
                    else:
                        d = d + 2 * dx
            else:
                dx = x1 - x0
                dy = y1 - y0

                xi = 1
                if dx < 0:
                    xi = -1
                    dx = -dx
                
                d = (2 * dx) - dy
                x = x0

                for y in range(y0, y1 + 1):
                    grid.addPoint(x, y)
                    if d > 0:
                        x = x + xi
                        d = d + (2 * (dx - dy))
                    else:
                        d = d + 2 * dx
 

 
# testcode
# let op: de beoordeling wordt gedaan op basis van andere waarden
grid = Grid(50, 50)
grid.rasterline(0, 0, 19, 19)
# grid.addPoint(0,3)
grid.rasterline(0,40 , 40,0)
grid.draw()

    

