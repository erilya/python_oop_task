import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distanceTo(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        
    def __str__(self):
        return str(self.x) + " " + str(self.y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Triangle:
    def __init__(self, p1, p2, p3):       
        # Проверка корректности
        # Нет ли одинаковых точек (отрезков нулевой длины)
        if p1 == p2 or p2 == p3 or p3 == p1:
            raise ValueError("Triangle can not have a segment of zero length. Points: %s %s %s" % (p1, p2, p3))
        
        # Проверяем не лежат ли все точки на одной прямой
        # Ax + By + C = 0
        # (y1 - y2)*x + (x2 - x1)*y + (x1*y2 - x2*y1)
        k_A = p1.y - p2.y
        k_B = p2.x - p1.x
        k_C = p1.x*p2.y - p2.x*p1.y
        
        if k_A*p3.x + k_B*p3.y + k_C == 0:
            raise ValueError("All points of a triangle can not belong to one line. Points: %s %s %s" % (p1, p2, p3))
        
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    # Получение длинн отрезков треугольника 
    def getSegmentsLengths(self):
        segments = [self.p1.distanceTo(self.p2), self.p2.distanceTo(self.p3), self.p3.distanceTo(self.p1)]
        segments.sort()
        return segments

    def __str__(self):
        return str(self.p1) + " " + str(self.p2) + " " + str(self.p3)
        
    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2  and self.p3 == other.p3
        
    def isSimilarTriangle(self, other):
        segments_self = self.getSegmentsLengths()
        segments_other = other.getSegmentsLengths()
        k = segments_self[0]/segments_other[0]
        return k == segments_self[1]/segments_other[1] and k == segments_self[2]/segments_other[2]


triangles=[]

f=open('input.txt','r')
for line in f:
    coords = [float(x) for x in line.split(" ")]
    triangles.append(Triangle(Point(coords[0], coords[1]), Point(coords[2], coords[3]), Point(coords[4], coords[5])))
f.close()

triangles_similar=[]
while len(triangles)>0:
    triangle = triangles.pop(0)
    triangles_similar_curr=[triangle]
    index = 0
    while index < len(triangles):
        triangle_curr = triangles[index]
        if triangle.isSimilarTriangle(triangle_curr):
            triangles_similar_curr.append(triangle_curr)
            triangles.pop(index)
        else:
            index = index + 1
    triangles_similar.append(triangles_similar_curr)    

f=open('output.txt','w')
index = 0
for triangles_list in triangles_similar:
    index = index + 1
    f.write("-- group %d --\n" % index)
    for triangle in triangles_list:
        f.write("%s\n" % triangle)
f.close()