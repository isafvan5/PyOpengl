from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
x = 0.0
y = 0.0
FPS = 60
angle = 0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawCar():

    global x,y,angle

    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,0.0)
    glVertex2f(x-50,y+25)
    glVertex2f(x+50,y+25)
    glVertex2f(x+50,y-25)
    glVertex2f(x-50,y-25)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0,0.0,0.0)
    glVertex2f(x-25,y-40)
    for i in range(0,361,1):
        glVertex2f(15*math.cos(i*math.pi/180.0)+x-25,15*math.sin(i*math.pi/180.0)+y-40)
    glEnd()

    glLineWidth(1.0)
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x-25,y-40)
    glVertex2f(15*math.cos(angle*math.pi/180.0)+x-25,15*math.sin(angle*math.pi/180.0)+y-40)
    glEnd()


    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0,0.0,0.0)
    glVertex2f(x+25,y-40)
    for i in range(0,361,1):
        glVertex2f(15*math.cos(i*math.pi/180.0)+x+25,15*math.sin(i*math.pi/180.0)+y-40)
    glEnd()

    glLineWidth(1.0)
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x+25,y-40)
    glVertex2f(15*math.cos(angle*math.pi/180.0)+x+25,15*math.sin(angle*math.pi/180.0)+y-40)
    glEnd()

    glutSwapBuffers()

def animate(temp):

    global x,y,angle

    if(x + 50 >= WINDOW_SIZE):
        x = -WINDOW_SIZE + 50
    else:
        x += 1

        angle = angle - 1

    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,0)

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Car")
    glutDisplayFunc(drawCar)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawCar)
    init()
    glutMainLoop()

main()