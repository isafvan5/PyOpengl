from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
x=0
y=0
scale=1.2
mode = 1

def Init():
    gluOrtho2D(-500,500,-500,500)
    glClearColor(0,0,0,1)



def box():
    global x,y
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(1,0,1)
    glVertex2f(x*-20,y*20)
    glVertex2f(x*20,y*20)
    glVertex2f(x*20,y*-20)
    glVertex2f(x*-20,y*-20)
    glEnd()
    glutSwapBuffers()

def animate(value):
    global x,y
    global mode
    glutPostRedisplay()
    glutTimerFunc(int(1000/5),animate,int(0))
    if (mode == 1):
        x=x+1
        y=y+1
        if(x==8):
            mode=0
    if (mode == 0):
        x=x-1
        y=y-1
        if(x==1):
            mode=1
   




def main():
    glutInit()
    glutInitWindowSize(500,500)
    #glutInitWindowPosition(0,0)
    #glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("box")
    glutDisplayFunc(box)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(box)
    Init()
    glutMainLoop()
main()