
#import Polygon
from Polygon import Polygon
from Point_1 import Point
from Rec import Rectangle



My_new = open('project01data.txt','r')
line = My_new.readline()
points = []
meo = ""
vertices=0
count=0
while line!="":
    items = line.split()
    #x = Point_1(items[0],(items[1]))
    if items[0] == "P":
        print("Reading vertices for a polygon with %s vertices"% (items[1]))
        vertices = int(items[1])
        count = 0
        meo="p"
        points=[]
    elif items[0] == "R":
        print("Reading vertices for a Rectangular with %s vertices"%(items[1]))
        vertices = int(items[1])
        count = 0
        meo = "R"
        points=[]
    else:
        x = Point(float(items[0]), float(items[1]))
        points.append(x)
        count = count + 1
        print("Vertexhas %d coordinates at" % (count))
        print(x)
        if count >= vertices:
            if meo == "p":
                poly = Polygon(points)
                print(poly.perimeter())
                print()
            else :
                ripreimeter=Rectangle(points)
                print(ripreimeter.perimeter())
                print()
    line = My_new.readline()
#print(My_new.read())
My_new.close()





