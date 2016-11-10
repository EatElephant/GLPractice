from ReadObj import *

def testParseObj():
    parser = ObjParser()
    objs = parser.read_obj("model\monkey.obj")
    print len(objs)
    for obj in objs:
        print obj.name
        for vertex in obj.vertices:
            print [vertex[0], vertex[1], vertex[2]]

def testGLDesplay():
    obj_list = []
    obj1= ObjModel("Obj1")
    obj2= ObjModel("Obj2")
    obj1.vertices = [[0,1,0],[-1,0,0],[1,0,0]]
    obj2.vertices = [[-1, -1, 0], [-2,-1, 0], [-2,-2, 0], [-2,-2, 0], [-1,-2, 0], [-1, -1, 0]]
    obj_list.append(obj1)
    obj_list.append(obj2)

    glDisplay = GLDisplay(obj_list)
    glDisplay.display()


if __name__ == "__main__":
    testParseObj()
    testGLDesplay()
