from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
ref_x=0
ref_y=0
va=0
initialPos=1
def cleerScreen():
    gluOrtho2D(-100,100,-100,100)
    glClearColor(0,0,0,1)

def car():
    global ref_x,ref_y
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(1,0,0)
    glVertex2f(ref_x-20,ref_y-10)
    glVertex2f(ref_x-20,ref_y-30)
    glVertex2f(ref_x+20,ref_y-30)
    glVertex2f(ref_x+20,ref_y-10)
    
    glEnd()
    glBegin(GL_POLYGON)
    
    glVertex2f(ref_x-10,ref_y-10)
    glVertex2f(ref_x-5,ref_y+10)
    glVertex2f(ref_x+5,ref_y+10)
    glVertex2f(ref_x+10,ref_y-10)
    glEnd()
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(ref_x-7,ref_y-7)
    glVertex2f(ref_x-3,ref_y+3)
    glVertex2f(ref_x+3,ref_y+3)
    glVertex2f(ref_x+7,ref_y-7)
    glEnd()
    wheel(-10)
    wheel(10)
    glFlush()

def wheel(x1):
    global ref_x,ref_y,initialPos
    r=5
    

    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        if (initialPos % 2==0):
            if (i<90 or(i>180 and i<270) ):
                glColor3f(0,1,0)
            else:
                glColor3f(0,0,1)
        else:
            if (i<90 or(i>180 and i<270) ):
               glColor3f(0,0,1)
            else:
                 glColor3f(0,1,0)

        radian=math.pi*(i/180)
        x=ref_x+x1+r*math.cos(radian)
        y=ref_y-30+r*math.sin(radian)
        glVertex2f(x,y)
    glEnd()
    
def move(key,x,y):
    global ref_x,ref_y,initialPos
    key=key.decode()
    if key=='w':
        ref_x+=1
        initialPos+=1
        car()
    if key=='s':
        ref_x-=1
        initialPos+=1
        car()




def main():
    global va
    va=input("radius =")
    glutInit()
    glutInitWindowSize(1000,1000)
    glutCreateWindow("mycar")
    glutDisplayFunc(car)
    glutKeyboardFunc(move)
    cleerScreen()
    glutMainLoop()
main()