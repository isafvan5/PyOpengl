from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
import time
ref_x=0
ref_y=0
step=0
points = [[-40,0],[40,0]]
def clearscreen():
    gluOrtho2D(-100,100,-100,100)
    glClearColor(0,0,0,1)

def seasow():
    global ref_x,ref_y,points
    glClear(GL_COLOR_BUFFER_BIT)
    # glBegin(GL_TRIANGLES)
    # glVertex2f(ref_x,ref_y)
    # glVertex2f(ref_x-10,ref_y-10)
    # glVertex2f(ref_x+10,ref_y+10)
    # glEnd()
    animate()
    round(points[1])
    round(points[0])
    glFlush()

def animate():
    global ref_x,ref_y,step
    glColor3f(1,0,1)
    glLineWidth(15)
    glBegin(GL_LINES)
    glVertex2f(points[0][0],points[0][1])
    glVertex2f(points[1][0],points[1][1])
    glEnd()
    step+=.5
    points[0][1] = 10*math.sin(math.radians(step))
    points[1][1] = - points[0][1]


def person(xc,yc):
    glColor3f(1,1,0)
    head=8
    height=30
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta=math.pi*(i/180)
        x=xc+head*math.cos(theta)
        y=yc+head*math.sin(theta)+height
        glVertex2f(x,y)
    glEnd()
    # body
    glLineWidth(30)
    glBegin(GL_LINES)
    glVertex2f(xc,yc+height)
    glVertex2f(xc,yc)
    glEnd()


    # hands
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(xc,yc+height-head)
    glVertex2f(xc+10,yc+height/2-8)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(xc,yc+height-head)
    glVertex2f(xc+16,yc+height/2)
    glEnd()

def round(p):
    global ref_x,ref_y
    
    r=10
    person(*points[0])

    glColor3f(0,0,1)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta=math.pi*(i/180)
        x=ref_x+p[0]+r*math.cos(theta)
        y=ref_y+p[1]+r/3*math.sin(theta)
        glVertex2f(x,y)

    glEnd()


def main():
    glutInit()
    glutInitWindowSize(1000,1000)
    glutCreateWindow("window")
    glutDisplayFunc(seasow)
    glutIdleFunc(seasow)
    #glutKeybeardFunc()
    clearscreen()
    glutMainLoop()
main()