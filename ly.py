from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
theta=0
mode=1

def Init():
    gluOrtho2D(-500,500,-500,500)
    glClearColor(0,0,0,1)

def man():
    global theta
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,1,0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0,100)
    glVertex2f(0,-100)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,120)
    glColor3f(1,0,0)
    for i in range(0,361,1):
        glVertex2f(40*math.cos(math.radians(i)),40*math.sin(math.radians(i))+110)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(100*math.cos(math.radians(theta)),200*math.sin(math.radians(theta)))
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(-100*math.cos(math.radians(theta)),200*math.sin(math.radians(theta)))
    glEnd()
    glFlush()

def animate(valur):
    global theta,mode
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if(mode==1):
        if(theta<90):
            theta=theta+1
        else:
            mode=0
            theta=90
    if(mode==0):
        theta-=1
        if(theta<1):
            mode=1
            theta=0
def main():
    glutInit()
    glutInitWindowSize(500,500)
    #glutInitWindowPosition(0,0)
    glutCreateWindow("boat")
    glutDisplayFunc(man)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(man)
    Init()
    glutMainLoop()
main()