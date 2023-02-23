from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
x=0
y=0
theta=0
mode =1
def cleerScreen():
    gluOrtho2D(-500,500,-500,500)
    glClearColor(0,0,0,1)

def man():
    global x,y,theta
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,1)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(0,100)
    glVertex2f(0,-300)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,0)
    glVertex2f(0,100)
    for i in range(0,361,1):
        glVertex2f(50*math.cos(math.pi*(i/180)),50*math.sin(math.pi*(i/180))+100)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0,-300)
    glVertex2f(-200,-400)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0,-300)
    glVertex2f(200,-400)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0,20)
    glVertex2f(x+-200*math.cos(math.radians(theta)),y+200*math.sin(math.radians(theta)))
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0,20)
    glVertex2f(x+200*math.cos(math.radians(theta)),y+200*math.sin(math.radians(theta)))
    glEnd()
  


    glFlush()

def animate(value)
    global x,y,theta,mode
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if (mode==1):
        theta += 1
        if(theta>90):
            theta = 90
            mode = 0
    
    if(mode==0):
        theta -= 1
        if (theta< 1):
            theta = 0
            mode = 1
    


def main():
    glutInit()
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("hai")
    glutDisplayFunc(man)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(man)
    cleerScreen()
    glutMainLoop()
main()