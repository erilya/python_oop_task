# 10. Для набора кругов заданных координатами центра и радиусом, найти круг,
# который лежит внутри максимального кол-ва других кругов.
# В случае существования нескольких подходящих кругов – выбрать минимального радиуса (если и таких будет несколько – то произвольный).
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

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def __contains__(self, item):
        r_dist = self.center.distance_to(item.center)
        return self.r >= r_dist + item.r
    
    def __str__(self):
        return "(%s) %s" % (self.center, self.r)

circles=[]

f = open('input.txt','r')
for l in f:
    k = [float(x) for x in l.split(" ")]
    circles.append(Circle(Point(k[0], k[1]), k[2]))
f.close()


# номер круга : количество вхождений
circles_dict = {}

for i in range(len(circles)-1):
    circle1 = circles[i]
    circles_dict[i] = 0
    for j in range(i+1, len(circles)):
        circle2 = circles[j]      
        if circle1 in circle2:
            circles_dict[i] +=1

r_circle = None
max_in = max(circles_dict.values())
if max_in > 0:
    circles_dict = {k: v for k, v in circles_dict.items() if v == max_in}
    r_circles = [circles[i] for i in circles_dict.keys()]
    sorted(r_circles, key=lambda circle: circle.r)
    r_circle = r_circles[0]

f = open('output.txt', 'w')
f.write(str(r_circle))
f.close()
