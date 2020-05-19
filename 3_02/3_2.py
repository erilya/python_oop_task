import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        
    def __str__(self):
        return str(self.x) + " " + str(self.y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line:
    def __init__(self, a, b, c):
        if a == 0 and b == 0:
            raise ValueError("All coefficients of line is zero")
        self.a = a
        self.b = b
        self.c = c

    # Проверка совпадают ли прямые 
    def __eq__(self, other):
        if other.a != 0:
            k = self.a / other.a
        else:
            k = self.b / other.b
            
        return (self.a == other.a if other.a == 0 else k == self.a / other.a) and \
               (self.b == other.b if other.b == 0 else k == self.b / other.b) and \
               (self.c == other.c if other.c == 0 else k == self.c / other.c)

    # Параллельны ли прямые
    def check_parallel(self, other):
        if other.a != 0:
            k = self.a / other.a
        else:
            k = self.b / other.b
        return (self.a == other.a if other.a == 0 else k == self.a / other.a) and \
               (self.b == other.b if other.b == 0 else k == self.b / other.b) and \
               not (self.c == other.c if other.c == 0 else k == self.c / other.c)
    
    # Точка пересечения прямых 
    def get_intersection_point(self, other):
        if self == other:
            raise ValueError("lines is same")
        if self.check_parallel(other):
            raise ValueError("lines is parallel")
            
        d = (self.a * other.b) - (other.a * self.b)
        x = ((self.c * other.b) - (other.c * self.b)) / d
        y = ((self.a * other.c) - (other.a * self.c)) / d
        return Point(x, y)

lines=[]

f = open('input.txt','r')
for l in f:
    k = [float(x) for x in l.split(" ")]
    lines.append(Line(k[0], k[1], k[2]))
f.close()

r_point = None
zero_point = Point(0, 0)

for i in range(len(lines)-1):
    l1 = lines[i]
    for j in range(i+1, len(lines)):
        l2 = lines[j]       
        if l1 != l2 and not l1.check_parallel(l2):
            point = l1.get_intersection_point(l2)
            if r_point is None or zero_point.distance_to(point) < zero_point.distance_to(r_point):
                r_point = point

f = open('output.txt', 'w')
f.write(str(r_point))
f.close()
