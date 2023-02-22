from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
import time

def clearscreen():
    gluOrtho2D(-100,100,-100,100)
    glClearColor(0,0,0,1)

def pipe():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(50,45)
    glVertex2f(50,75)
    glVertex2f(90,75) 
    glVertex2f(90,45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(50,65)
    glVertex2f(30,65)
    glVertex2f(30,35)
    glVertex2f(40,35)
    glVertex2f(30,55)
    glVertex2f(50,55)
    glEnd()

def waterdrop(y):
    glColor(0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex2f(37,y)
    glVertex2f(33,y)
    glVertex2f(35,y-4)
    glEnd()

def water():
    for i in range(0,-15,-1):
        glClear(GL_COLOR_BUFFER_BIT)
        waterdrop(i+40)
        waterdrop(i+33)
        waterdrop(i-2)
        pipe()
        glFlush()
        time.sleep(.05)
        
def animate():
    for i in range(0,5,1):
        water()


def main():
    glutInit()
    glutInitWindowSize(1000,1000)
    glutCreateWindow("window")
    glutDisplayFunc(animate)
    clearscreen()
    glutMainLoop()
main()