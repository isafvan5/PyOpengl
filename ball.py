from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
import time
ref_x=-80
ref_y=0
initialPos=1



def cleerScreen():
    gluOrtho2D(-100,100,-100,100)
    glClearColor(0,0,0,1)

def ball(x1,y1):
    global ref_x,ref_y,initialPos
    r=10
   
        
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2f(-100,-40)
    glVertex2f(100,-40)
    glEnd()
    glColor(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
       

        radian=math.pi*(i/180)
        x=ref_x+r*math.cos(radian)
        y=ref_y+r*math.sin(radian)
        glVertex2f(x,y)
    glEnd()
    glColor3f(0,1,0)
    glPointSize(5)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(ref_x,ref_y)
    glVertex2f(ref_x-x1,ref_y+y1)
    glEnd()
    glFlush()

def move(key,x,y):
    global ref_x,initialPos,ref_y
    key=key.decode()
    if (key=='w'):
        ref_x+=1
        initialPos+=1
        ball()
    if(key=='s'):
        ref_x-=1
        initialPos+=1
        ball()
    if(key=='a'):
        ref_y+=1
        initialPos+=1
        ball()

def bounce():
    global ref_x,ref_y,initialPos
    s=30
    for i in range(0,900,1):
        radian=math.pi*(i/180)
        
        if(math.sin(radian)<0):
            ref_y=30*math.sin(radian)
        else:
            ref_y=s*math.sin(radian)    
        if(math.sin(radian)==-1):
            s-=10

        ref_x=ref_x+.2
        x=7*math.cos(radian)
        y=7*math.sin(radian)
        ball(x,y)
        time.sleep(.01)






def main():
    glutInit()
    glutInitWindowSize(1000,1000)
    glutCreateWindow("my window")
    glutDisplayFunc(bounce)
    glutKeyboardFunc(move)
    cleerScreen()
    glutMainLoop()
main()