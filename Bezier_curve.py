import matplotlib.pyplot as plt
import numpy as np

class point():
    def __init__(self, x, y, father = None, depth = 0):
        self.t = 0
        self.x = x
        self.y = y
        self.father = father
        self.depth = depth + 1
        
        
    def movePoint(self, dt):             
        self.x = (1 - self.t) * self.father.startPoint.x + self.t * self.father.endPoint.x
        self.y = (1 - self.t) * self.father.startPoint.y + self.t * self.father.endPoint.y
        
    
    def __repr__(self):
        return f"({self.x},{self.y}) on {self.father}, depth {self.depth}"

class vector():
    def __init__(self, startPoint, endPoint, depth = 0):
        self.startPoint = startPoint
        self.endPoint = endPoint
        
        self.startX = startPoint.x
        self.startY = startPoint.y
        
        self.depth = depth + 1
        
    def __repr__(self):
        return f"({self.x},{self.y}) -> ({self.endx},{self.endy})"
    



def bezier(allPoints):
    vectors = []
    vectors.append(getVectors(allPoints))
    
    xvalues = []
    yvalues = []
    
    dt = 0.001
    t = int(1/dt)
    
    for i in range(len(allPoints) - 2):
        nextSetOfPoints = []
        for v in vectors[i]:
            pOV = point(v.startX, v.startY, v, v.depth)
            nextSetOfPoints.append(pOV)
        
        vectors.append(getVectors(nextSetOfPoints))
    
    for i in range(t):
        for i in range(1, len(vectors)):
            if len(vectors[i]) == 1:
                xvalues.append(vectors[i][0].startPoint.x)
                yvalues.append(vectors[i][0].startPoint.y)
            else:
                for v in vectors[i]:
                    v.startPoint.movePoint(dt)
                    v.endPoint.movePoint(dt)
                
    
    return xvalues, yvalues

def getVectors(points):
    output = []
    
    for i,p in enumerate(points[:-1]):
        output.append(vector(p, points[i+1], p.depth))
    
    return output

startPoint = point(0,0)
endPoint = point(5,2)

startEnd = [startPoint,endPoint]

midPoint1 = point(1,2)
midPoint2 = point(2,0)

allPoints = [startPoint,midPoint1,midPoint2,endPoint]
midPoints = allPoints[1:-1]

curve = bezier(allPoints)

xvalues = []
yvalues = []

for p in allPoints:
    xvalues.append(p.x)
    yvalues.append(p.y)

plt.plot(xvalues, yvalues)
plt.show()