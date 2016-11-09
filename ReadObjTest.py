from ReadObj import *

parser = ObjParser()
objs = parser.read_obj("model\monkey.obj")
print len(objs)
for obj in objs:
    print obj.name
    for vertex in obj.vertices:
        print [vertex[0], vertex[1], vertex[2]]
