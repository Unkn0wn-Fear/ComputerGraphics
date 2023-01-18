from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Lines:
    def __init__(self, sizeX, sizeY,):
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
    
        for ribben in ribben:
            for punten in ribben:
                glVertex3fv(punten[punten])
        glEnd()
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
 
    def  vermenmatrixvector(self,matrix1,matrix2,matrix3,vector):
        x1,y1,z1 = matrix1
        x2,y2,z2 = matrix2
        x3,y3,z3 = matrix3
        

# testcode
lines = Lines(10   ,10)

punten = (
    (-1,-1,-1), #0 v1
    (1,-1,-1),  #1 V2
    (1, 1,-1),  #2 V3
    (-1, 1,-1), #3 V4
    (-1,-1, 1), #4 V5
    (1,-1, 1),  #5 V6
    (1, 1, 1),  #6 V7
    (-1, 1, 1)  #7 V8

)
ribben = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (0,4),
    (1,5),
    (2,6),
    (3,7),
    (4,5),
    (5,6),
    (6,7),
    (7,4),



)
# lines.addLine((-5, -5), (6, 6))
# p = (100, 200)
# for i in range(100, 600, 50):
#     lines.addLine(p, (i, 400))
lines.draw()
