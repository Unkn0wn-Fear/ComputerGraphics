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
        
    def rasterline(self, x1, y1, x2, y2):
        grid.addPoint(x1,y1)
        grid.addPoint(x2,y2)
        #bereken delta x 
        dx = abs(x2 - x1)
        #bereken delta y 
        dy = abs(y2 - y1)
        
        #S
        m = dy/dx
        
        # step 3 perform test to check if pk < 0
        flag = True
        
        line_pixel = []
        line_pixel.append((x1,y1))
        
        step = 1
        if x1>x2 or y1>y2:
            step = -1

        mm = False   
        if m < 1:
            x1, x2 ,y1 ,y2 = y1, y2, x1, x2
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            mm = True
            
        p0 = 2*dx - dy
        x = x1
        y = y1
        
        for i in range(abs(y2-y1)):
            if flag:
                x_previous = x1
                p_previous = p0
                p = p0
                flag = False
            else:
                x_previous = x
                p_previous = p
                
            if p >= 0:
                x = x + step

            p = p_previous + 2*dx -2*dy*(abs(x-x_previous))
            y = y + 1
            
            if mm:
                grid.addPoint(y,x)
                
            else:
                grid.addPoint(x,y)
                
        pass

# testcode
# let op: de beoordeling wordt gedaan op basis van andere waarden
grid = Grid(50, 50)
#grid.rasterline(0, 0, 19, 19)
# grid.addPoint(0,3)
# grid.addPoint(30,40)
grid.rasterline(0, 3, 30, 40)
grid.draw()



