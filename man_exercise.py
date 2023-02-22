from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
import time
ref_x=100
ref_y=0
theta=0
dir=0
def clearscreen():
    gluOrtho2D(-500,500,-500,500)
    glClearColor(1,1,1,1)

def man():
    global ref_x,ref_y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(0,50)
    glVertex2f(0,-100)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(ref_x,ref_y)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(-ref_x,ref_y)
    glEnd()
    animate()
    glFlush()

def animate():

    global ref_x,ref_y,theta,dir
    
    for i in range(0,60,1):
        ref_x=100*math.cos(math.radians(theta))
        ref_y=100*math.sin(math.radians(theta))
        if(dir==0):
            theta+=1
            if(theta>90):
                dir=1
        elif(dir==1):
            theta-=1
            if(theta<0):
                dir=0



    
def main():
    glutInit()
    glutInitWindowSize(1000,1000)
    glutCreateWindow("window")
    glutDisplayFunc(man)
    clearscreen()
    glutMainLoop()
main()