from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

class ObjModel:
    def __init__(self, name = ""):
        self.name = name
        self.vertices = []
        self.normals = []
        self.uv = []


class ObjParser:
    def __init__(self):
        self.vertices_list = []
        self.normals_list = []
        self.uv = []
        self.vertices_index = []
        self.normals_index = []

    def add_obj_to_list(self, list, obj):
        if obj.name != "":
            vertices = []
            normals = []
            for i in range(len(self.vertices_index)):
                vertices.append(self.vertices_list[self.vertices_index[i] - 1])
                normals.append(self.normals_list[self.normals_index[i] - 1])
            obj.vertices = vertices
            obj.normals = normals
            obj.uv = self.uv
            del self.uv[:]
            del self.vertices_index[:]
            del self.normals_index[:]
            list.append(obj)

    def read_obj(self, path):
        """
        Read path obj 3d model into a list of ObjModel objects
        """
        objModels = []
        objModel = ObjModel()
        file = open(path, 'r')
        for line in file:
            if line.startswith('o'):
                data = line.split(' ')
                if len(data) == 2:
                    self.add_obj_to_list(objModels, objModel)
                    objModel = ObjModel(data[1])
            elif line.startswith('v '):
                data = line.split(' ')
                if len(data) == 4:
                    self.vertices_list.append([float(data[1]), float(data[2]), float(data[3])])
            elif line.startswith('vt '):
                data = line.split(' ')
                if len(data) == 3:
                    self.uv.append([int(data[1]), -int(data[2])])
            elif line.startswith('vn '):
                data = line.split(' ')
                if len(data) == 4:
                    self.normals_list.append([float(data[1]), float(data[2]), float(data[3])])
            elif line.startswith('f '):
                data = line.split(' ')
                if len(data) == 4:
                    for pair in data[1:]:
                        index_pair = pair.split('//') #index_pair first element is the vertex index, second element is the normal index
                        self.vertices_index.append(int(index_pair[0]))
                        self.normals_index.append(int(index_pair[1]))

        #put last obj into the list
        self.add_obj_to_list(objModels, objModel)

        return objModels

def initGL():
    glClearColor(1, 1, 1, 1.0)
    gluOrtho2D(-3.0, 3.0, -3.0, 3.0)

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1,0,1,0)

    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_LINE)

    glBegin(GL_TRIANGLES)
    for i in range(len(objs)):
        glColor3f(0.8, i, 0.8)
        for vertex in objs[i].vertices:
            glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

    glFlush()


def main():
    if len(sys.argv) != 2:
        print (sys.argv[0] + " [path]")
        return

    parser = ObjParser()

    global objs
    objs = parser.read_obj(sys.argv[1])

    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
    glutInitWindowSize(500,500)
    glutCreateWindow("model")

    glutDisplayFunc(drawFunc)
    initGL()
    glutIdleFunc(drawFunc)
    glutMainLoop()

if __name__ == "__main__":
    main()
