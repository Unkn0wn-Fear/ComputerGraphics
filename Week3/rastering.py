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
        # controleerd of het verschil van delta y kleiner dan delta x is en maakt er de absoulute waardes van 
        if abs(y1 - y0) < abs(x1 - x0):
            #controleert welke ocant hij in zit door te vergelijken of de 1e punt groter is dan het 2e punt 
            if x0 > x1:
                #initialiseerd alle waardes 
                tempX = x0
                tempY = y0
                x0 = x1
                x1 = tempX
                y0 = y1
                y1 = tempY
            #berekend delta x en delta y 
            dx = x1 - x0
            dy = y1 - y0
            #interval
            yi = 1
            #controleert of de delta y lager is dan 0 
            if dy < 0:
                yi = -1
                dy = -dy
            #berekend d 
            d = (2 * dy) - dx
            y = y0
            #blijft loopen tot dat de x gelijk is aan x0 tot x1 +1 
            for x in range(x0, x1+1):
                #zet het berekende puntje op het veld
                grid.addPoint(x, y)
                #bekijkt of de net berekende d groter is dan 0
                if d > 0:
                    y = y + yi
                    d = d + (2 * (dy - dx))
                #als d niet groter is dan 0
                else:
                    d = d + 2 * dy
            #als het 1e punt niet groter is dan het 2e punt run deze code
        else:
            #bekijkt nu of de 1e y kleiner is dan de 2e y 
            if y0 > y1:
                #initialiseerd values 
                tempX = x0
                tempY = y0
                x0 = x1
                x1 = tempX
                y0 = y1
                y1 = tempY
            #berekend delta x en delta y 
            dx = x1 - x0
            dy = y1 - y0
            #interval
            xi = 1
            #bekijkt of delta x kleiner is dan 0 
            if dx < 0:
                xi = -1
                dx = -dx
            #berekend d 
            d = (2 * dx) - dy
            x = x0
            #for loop tot dat y gelijk is aan y0 en y1 + 1
            for y in range(y0, y1+1):
                #zet puntje op scherm
                grid.addPoint(x, y)
                #kijkt of d groter dan 0 nis
                if d > 0:
                    x = x + xi
                    d = d + (2 * (dx - dy))
                else:
                    d = d + 2 * dx
 

 
# testcode
# let op: de beoordeling wordt gedaan op basis van andere waarden
grid = Grid(20, 20)
grid.rasterline(5,0,0,5)
grid.draw()
