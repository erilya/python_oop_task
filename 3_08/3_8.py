class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = min(x1, x2)
        self.y1 = min(y1, y2)
        self.x2 = max(x1, x2)
        self.y2 = max(y1, y2)

    def isIntersect(self, rect):
        return not(self.x1 >= rect.x2 or rect.x1 >= self.x2 or self.y1 >= rect.y2 or rect.y1 >= self.y2)

    def __str__(self):
        return str(self.x1) + " " + str(self.y1) + " " + str(self.x2) + " " + str(self.y2)

rectagles=[]

f=open('input.txt','r')
for line in f:
    coords = [float(x) for x in line.split(" ")]
    rectagles.append(Rectangle(coords[0],coords[1],coords[2],coords[3]))
f.close()

f=open('output.txt','w')
for i in range(len(rectagles)):
    rect = rectagles[i]
    is_intersect = False
    for rect_other in rectagles[:i]+rectagles[i+1:]:
        if rect.isIntersect(rect_other):
            is_intersect = True
            break
    if not is_intersect:
        f.write(str(rect)+"\n") 
f.close()
