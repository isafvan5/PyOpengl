from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
import time

scale=1
dir=0
def clearscreen():
    gluOrtho2D(-100,100,-100,100)
    glClearColor(0,0,0,1)

def star():
    global scale
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1,0,1)
    glBegin(GL_POLYGON)
    glVertex2f(scale*0,scale*40)
    glVertex2f(scale*20,scale*20)
    glVertex2f(scale*40,0)
    glVertex2f(scale*20,scale*-20)
    glVertex2f(0,scale*-40)
    glVertex2f(scale*-20,scale*-20)
    glVertex2f(scale*-40,0)
    glVertex2f(scale*-20,scale*20)
    glEnd()
    glFlush()
def animate(value):
    global scale,dir
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,0)
    if(dir==0):
        scale-=0.1
        if(scale<0.1):
            dir=1
    elif dir==1:
        scale+=0.1
        if(scale>0.9):
            dir=0

def main():
    glutInit()
    glutInitWindowSize(1000,1000)
    glutCreateWindow("hello")
    glutDisplayFunc(star)
    glutTimerFunc(0,animate,0)
    clearscreen()
    glutMainLoop()
main()