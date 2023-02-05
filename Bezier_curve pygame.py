import matplotlib.pyplot as plt
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
        self.endX = endPoint.x
        self.endY = endPoint.y
        
        
        self.depth = depth + 1
        
    def __repr__(self):
        return f"({self.startPoint.x},{self.startPoint.y}) -> ({self.endPoint.x},{self.endPoint.y})"
    



def bezier(allPoints):
    vectors = []
    vectors.append(getVectors(allPoints))
    
    xvalues = [allPoints[0].x]
    yvalues = [allPoints[0].y]
 
    line = []
    
    dt = 0.001
    t = int(1/dt)
    
    for i in range(len(allPoints) - 2):
        nextSetOfPoints = []
        for v in vectors[i]:
            pOV = point(v.startX, v.startY, v, v.depth)
            nextSetOfPoints.append(pOV)
        
        vectors.append(getVectors(nextSetOfPoints))

    finalPoint = point(vectors[-1][0].startX, vectors[-1][0].startY, vectors[-1][0], vectors[-1][0].depth)
    
 
    for i in range(t):
 

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
        
        # Draws all vectors
        for i in range(len(moved) - 1):
            pygame.draw.lines(screen, color=(46, 46, 46), closed=False, points=[(moved[i].x, (size[1] - moved[i].y)), (moved[i+1].x, (size[1] - moved[i+1].y))], width=1)
            pygame.draw.circle(screen, color=(35, 35, 35), center=(moved[i].x, (size[1] - moved[i].y)), radius=3, width=5)
            pygame.draw.circle(screen, color=(35, 35, 35), center=(moved[i+1].x, (size[1] - moved[i+1].y)), radius=3, width=5)
        
        for n in range(len(vectors)):
            for v in vectors[n]:
                pygame.draw.lines(screen, color=(35, 35, 35), closed=False, points=[(v.startX, (size[1] - v.startY)), (v.endX, (size[1] - v.endY))], width=3)
        # Draws all points        
        for p in allPoints:
            pygame.draw.circle(screen, color=(35, 35, 35), center=(p.x, (size[1] - p.y)), radius=5, width=5)
            
        
        # Makes a list of the bezier curve so it can be drawn every time
        line.append([(xvalues[-2], (size[1] - yvalues[-2]) ),(xvalues[-1], (size[1] - yvalues[-1]))])
        for i in line:
            pygame.draw.lines(screen, color=(237,35,0), closed=False, points=i, width=3)
        pygame.draw.circle(screen, color=(237,35,0), center=(xvalues[-1], (size[1] - yvalues[-1])), radius=3, width=3)
        pygame.display.update()
        pygame.time.delay(2)
        screen.fill((12, 12, 12))
    
    return xvalues, yvalues

def getVectors(points): 
    output = []
    
    for i,p in enumerate(points[:-1]):
        output.append(vector(p, points[i+1], p.depth))
    
    return output

allPoints = []

size = width, height = 700, 700

screen = pygame.display.set_mode(size)

screen.fill((12, 12, 12))
pygame.display.update()
midPoints = allPoints[1:-1]

    
while True:
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            allPoints.append(point(pygame.mouse.get_pos()[0], size[1] - pygame.mouse.get_pos()[1]))
            for p in allPoints:
                pygame.draw.circle(screen, color=(35, 35, 35), center=(p.x, (size[1] - p.y)), radius=5, width=5)
            pygame.display.update() 
        
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RETURN:
                bezier(allPoints)

            if events.key == pygame.K_ESCAPE:
                allPoints = []
                screen.fill((12, 12, 12))
                pygame.display.update()
        
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
