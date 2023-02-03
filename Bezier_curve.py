import matplotlib.pyplot as plt
import numpy as np

class point():
    def __init__(self, x, y, father = None, depth = 0):
        self.x = x
        self.y = y
        self.father = father
        self.depth = depth + 1
        
    def __repr__(self):
        return f"({self.x},{self.y}, on {self.father}, depth {self.depth})"

class vector():
    def __init__(self, sx, sy, ex, ey, depth = 0, father = None):
        self.x = sx
        self.y = sy
        
        self.endx = ex
        self.endy = ey
        
        self.dx = ex-sx
        self.dy = ey-sy
        
        self.depth = depth + 1
        self.father = father
        
    def __repr__(self):
        return f"({self.x},{self.y}) -> ({self.endx},{self.endy})"
    

def movePoint(mPoint):
    pass

def bezier(allPoints):
    vectors = []
    vectors.append(getVectors(allPoints))
    
    for i in range(len(allPoints) - 2):
        nextSetOfPoints = []
        for v in vectors[i]:
            pOV = point(v.x, v.y, v, v.depth)
            nextSetOfPoints.append(pOV)
        
        vectors.append(getVectors(nextSetOfPoints))
        
    return vectors

def getVectors(points):
    output = []
    
    for i,p in enumerate(points[:-1]):
        output.append(vector(p.x, p.y, points[i+1].x, points[i+1].y, p.depth, p.father))
    
    return output

startPoint = point(0,0)
endPoint = point(5,2)

startEnd = [startPoint,endPoint]

midPoint1 = point(1,2)
midPoint2 = point(2,0)

allPoints = [startPoint,midPoint1,midPoint2,endPoint]
midPoints = allPoints[1:-1]

for i in range(len(bezier(allPoints))):
    print('\n',i)
    for p in bezier(allPoints)[i]:
        print(p.father) if p.father else print(p)