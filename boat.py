from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
theta=0
x=0
y=0
window=500
def Init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-window,window,-window,window)
def boat():
    glClear(GL_COLOR_BUFFER_BIT)
    global x,y,theta
    glColor3f(1,0,1)
    glBegin(GL_POLYGON)
    glVertex2f(x+-150,y+0)
    glVertex2f(150+x,0+y)
    glVertex2f(180+x,50+y)
    glVertex2f(120+x,30+y)
    glVertex2f(-120+x,30+y)
    glVertex2f(-180+x,50+y)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,0)
    glVertex2f(x+0,y+50)
    for i in range(0,361,1):
        glVertex2f(x+20*math.cos(math.pi*(i/180)),y+20*math.sin(math.pi*(i/180))+50)
    glEnd()
    glLineWidth(4)
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex2f(x+0,y+30)
    glVertex2f(x+40+30*math.cos(math.radians(theta)),y+-10+30*math.sin(math.radians(theta)))
    glEnd()
    glFlush()
def animate(temp):
    global x,y,theta
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if(x<500):
        x+=1
    else:
        x=-500
    if(theta<30):
        theta=theta-1
    else:
        theta=0
def main():
    glutInit()
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("boat")
    glutDisplayFunc(boat)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(boat)
    Init()
    glutMainLoop()
main()