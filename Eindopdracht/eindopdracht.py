import math
import random

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

x, y, z = 0.0, 0.0, 0.0
vx, vy, vz = 0.03, 0.02, 0.01
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
    gluQuadricTexture(quad, GL_TRUE)
    glTranslatef(x, y, z)
    gluSphere(quad, 0.2, 20, 20)
    
  

def drawPlane():
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glEnd()

    
def checkCollision():
    global x, y, z, vx, vy, vz
    print("x is = " + str(x))
    print("y is = " + str(y))
    print("z is = " + str(z))
   

    if x < (-1 + 0.2 ) or x > (1 - 0.2):
        vx = -vx * random.uniform(0.8, 1.2)
        if (vx ==  0): 
            vx + 0.01
    if y < (-1 + 0.2) or y > (1 - 0.2):
        vy = -vy * random.uniform(0.8, 1.2)
        if (vx == 0): 
            vy + 0.01
    if z < (-1+0.2) or z > (1 -0.2):
        vz = -vz * random.uniform(0.8, 1.2)
        if (vx == 0): 
            vz + 0.01
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
    #drawPlane()

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    light_pos = (1.0, 0.0, 1.0, 0.0)
    glLight(GL_LIGHT0, GL_AMBIENT, [1, 1, 1])
  
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    drawCube()
    drawPlane()

#   # Enable texture mapping
#     glEnable(GL_TEXTURE_2D)

#     # Load the image
#     img = Image.open("Eindopdracht/die-petronas-towers-sind.jpg")

#     # Bind the image as a texture
#     glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
#     texture = glGenTextures(1)
#     glBindTexture(GL_TEXTURE_2D, texture)
#     glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
#     glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
#     glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img.tobytes())
    
    drawSphere()
    
#    glDisable(GL_TEXTURE_2D)



   
    checkCollision()
    glDisable(GL_LIGHTING)
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

glutDisplayFunc(display)
glEnable(GL_DEPTH_TEST)
glutKeyboardFunc(keyboard)    
glutMainLoop()