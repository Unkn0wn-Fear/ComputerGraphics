from OpenGL.GL import *
from OpenGL.GLUT import *
def display():
glClear(GL_COLOR_BUFFER_BIT)
glPushMatrix()
glFrustum(-1.333, 1.333, -1, 1, 1, 5)
glTranslate(0, 0, -2)
glutWireCube(1)
glPopMatrix()
glFlush()
glutInit()
glutInitWindowSize(640, 480)
glutCreateWindow("Projectie".encode("ascii"))
glutDisplayFunc(display)
glutMainLoop()