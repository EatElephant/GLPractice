from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL. GLUT import *
from numpy import *
import sys

def init():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5.0)

    #draw Axis
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(1.0, 0)
    glVertex2f(-1.0,0)
    glVertex2f(0, 1.0)
    glVertex2f(0, -1.0)
    glEnd()

    #draw quadratic function
    glColor3f(1.0, 0.2, 0.0)
    glBegin(GL_LINES)
    for x in arange(-0.8, 0.8, 0.01):
        y = x*x
        glVertex2f(x, y)

    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Quadratic")
    glutDisplayFunc(drawFunc)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
