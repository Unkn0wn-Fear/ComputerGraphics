import math
import random

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x, y, z = 0.0, 0.0, 0.0
vx, vy, vz = 0.003, 0.002, 0.001
camera_x, camera_y, camera_z = 0, 0, 1


vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)


def drawCube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def keyboard(key, x, y):
    global camera_x, camera_y, camera_z
    if key == b'w':
        camera_y += 0.1
    elif key == b's':
        camera_y -= 0.1
    elif key == b'a':
        camera_x -= 0.1
    elif key == b'd':
        camera_x += 0.1

def drawSphere():
    quad = gluNewQuadric()
    glTranslatef(x, y, z)
    gluSphere(quad, 0.1, 20, 20)

def checkCollision():
    global x, y, z, vx, vy, vz
    print("x is = " + str(x))
    print("y is = " + str(y))
    print("z is = " + str(z))
   

    if x < -1 or x > 1:
        vx = -vx * random.uniform(0.8, 1.2)
    if y < -1 or y > 1:
        vy = -vy * random.uniform(0.8, 1.2)
    if z < -1 or z > 1:
        vz = -vz * random.uniform(0.8, 1.2)
    x += vx  
    y += vy  
    z += vz 

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Move the camera


    gluLookAt(camera_x, camera_y, camera_z, 1, 0, 0, 0, 1, 0)
    # Draw the cube
    drawCube()

    # Draw the sphere
    drawSphere()

    checkCollision()

    glutSwapBuffers()
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(900 , 900)
glutCreateWindow("Bouncing sphere")
glEnable(GL_LINE_SMOOTH)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
glFrustum(-1.333, 1.333, -1, 1, 1, 5)
glMatrixMode(GL_MODELVIEW)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLight(GL_LIGHT0, GL_POSITION, [-3, 4, 5])
glLight(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5])
glLight(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5])
glLight(GL_LIGHT0, GL_SPECULAR, [1, 1, 1])
glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [1, 1, 0, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 40)
glutDisplayFunc(display)
glEnable(GL_DEPTH_TEST)
glutKeyboardFunc(keyboard)    
glutMainLoop()