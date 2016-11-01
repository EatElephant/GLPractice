from OpenGL.GL import *
#from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1,0,0.1,0)
    glutWireTeapot(0.5)
    #glutSolidTeapot(0.5)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(400,200)
glutCreateWindow("First")
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()
