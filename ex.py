from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
import time
theta=0
ref_x=0
ref_y=0
def clearscreen():
    gluOrtho2D(-100,100,-100,100)
    glClearColor(0,0,0,1)

def bird():
    global ref_x,ref_y,theta
    glLineWidth(10)
    glColor3f(1,0,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2f(40,0)
    glVertex2f(-40,0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(10*math.cos(math.radians(theta))+(ref_x+20),10*math.sin(math.radians(theta))+(ref_y+20))
    glVertex2f(-10*math.cos(math.radians(theta))+(ref_x+20),10*math.sin(math.radians(theta))+(ref_y+20))
    glEnd()
    
    glutSwapBuffers()
def animate(value):
    global theta
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,0)
    #x=10*math.cos(math.radians(theta))
    #y=10*math.sin(math.radians(theta))
    #glVertex2f(x,y)
    if(theta<45):
        theta+=1
    else:
        theta=0
    
    
  
def main():
    glutInit()
    glutInitWindowSize(1000,1000)
    glutCreateWindow("window")
    glutDisplayFunc(bird)
    glutTimerFunc(0,animate,0)
    clearscreen()
    glutMainLoop()
main()