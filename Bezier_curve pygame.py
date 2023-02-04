import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import pygame



pygame.init()



class point():
    def __init__(self, x, y, father = None, depth = 0):
        self.t = 0
        self.x = x
        self.y = y
        self.father = father
        self.depth = depth + 1
        
        
    def movePoint(self, dt):   
        self.t += dt          
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
        return f"({self.startPoint.x},{self.startPoint.y}) -> ({self.endPoint.x},{self.endPoint.y})"
    



def bezier(allPoints):
    vectors = []
    vectors.append(getVectors(allPoints))
    
    xvalues = [allPoints[0].x]
    yvalues = [allPoints[0].y]
    
    dt = 0.01
    t = int(1/dt)
    
    for i in range(len(allPoints) - 2):
        nextSetOfPoints = []
        for v in vectors[i]:
            pOV = point(v.startX, v.startY, v, v.depth)
            nextSetOfPoints.append(pOV)
        
        vectors.append(getVectors(nextSetOfPoints))

    finalPoint = point(vectors[-1][0].startX, vectors[-1][0].startY, vectors[-1][0], vectors[-1][0].depth)
    
    # plt.ion()
    
    # fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    
    for i in range(t+1):
        # ax.cla()

        # scatterX = []
        # scatterY = []
        # colors = []
        # linesegments = []
        
        # for vlist in vectors:
        #     for v in vlist:
        #         scatterX.append(v.startPoint.x)
        #         scatterY.append(v.startPoint.y)
        #         colors.append('blue')
        #         scatterX.append(v.endPoint.x)
        #         scatterY.append(v.endPoint.y)
        #         colors.append('blue')
        #         linesegments.append([(v.startPoint.x, v.startPoint.y), (v.endPoint.x, v.endPoint.y)])
        
        
            
        # scatterX.append(finalPoint.x)
        # scatterY.append(finalPoint.y)
        # colors.append('red')
        # ax.scatter(scatterX, scatterY, c=colors)
        # ls = LineCollection(linesegments, linewidths=1, colors='gray')
        # ax.add_collection(ls)
        # ax.plot(xvalues, yvalues, lw = 3, c='green')
        # fig.canvas.draw()
        # fig.canvas.flush_events()

        

        moved = []

        for i in range(1, len(vectors)):
            for v in vectors[i]:
                if v.startPoint not in moved:
                    v.startPoint.movePoint(dt)
                    moved.append(v.startPoint)
                if v.endPoint not in moved:
                    v.endPoint.movePoint(dt)
                    moved.append(v.endPoint)
        finalPoint.movePoint(dt)
        xvalues.append(finalPoint.x)
        yvalues.append(finalPoint.y)    
        
        pygame.draw.lines(screen, color=(255,0,0), closed=False, points=[(xvalues[-2], (size[1] - yvalues[-2]) ),(xvalues[-1], (size[1] - yvalues[-1]))], width=3)
        pygame.display.update()
        pygame.time.delay(10)
    # while plt.get_fignums():
    #     fig.canvas.draw()
    #     fig.canvas.flush_events()
    
    return xvalues, yvalues

def getVectors(points): 
    output = []
    
    for i,p in enumerate(points[:-1]):
        output.append(vector(p, points[i+1], p.depth))
    
    return output

allPoints = [
    point(20,20),
    point(500,10),
    point(200,500),
    point(500,2)
]

size = width, height = 700, 700

screen = pygame.display.set_mode(size)

midPoints = allPoints[1:-1]


# while True:
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             pygame.quit()
#             quit()

    

curve = bezier(allPoints)

# while True:
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     pygame.display.update()

# for i in range(len(curve[0])):    
#     pygame.draw.circle(screen, color=(255,0,0), center=(curve[0][i], curve[1][i]), radius=4, width=1)

for p in allPoints:
    plt.plot(p.x, p.y, 'o')
plt.plot(curve[0],curve[1])
plt.show()