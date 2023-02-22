from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
import time

x,y,theta,x2,y2=0,0,0,0,0
def clearscreen():
    gluOrtho2D(-500,500,-500,500)
    glClearColor(1,1,1,1)



def planet():
    global x,y,x2,y2
    glClear(GL_COLOR_BUFFER_BIT)
    circle()
    circle1()
    round(0,0)
    round(x,y)
    round(x2,y2)
    glFlush()

def round(x1,y1):
    glColor3f(1,.5,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta=math.pi*(i/180)
        x=x1+20*math.cos(theta)
        y=y1+20*math.sin(theta)
        glVertex2f(x,y)
    glEnd()
def animate(value):
    global x,y,theta,x2,y2
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,0)
    x=400*math.cos(math.radians(theta))
    y=200*math.sin(math.radians(theta))
    x2=320*math.cos(math.radians(theta))
    y2=180*math.sin(math.radians(theta))
    theta+=1

def circle():
    glBegin(GL_LINE_LOOP)
    for i in range(0,360,1):
        theta=math.pi*(i/180)
        x=400*math.cos(theta)
        y=200*math.sin(theta)
        glVertex2f(x,y)
    glEnd()

def circle1():
    glBegin(GL_LINE_LOOP)
    for i in range(0,360,1):
        theta=math.pi*(i/180)
        x=320*math.cos(theta)
        y=160*math.sin(theta)
        glVertex2f(x,y)
    glEnd()


def main():
    glutInit()
    glutInitWindowSize(1000,1000)
    glutCreateWindow("window")
    glutDisplayFunc(planet)
    glutTimerFunc(0,animate,0)
    clearscreen()
    glutMainLoop()
main()