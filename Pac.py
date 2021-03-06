                                                  
                                                  
import pygame, sys, math

class Pac():
    def __init__(self, image, speed=[0,0], pos=[0,0], size=None):
        self.image = pygame.image.load("Resources/Pac/"+image)
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2 -1
        self.didBounceX = False
        self.didBounceY = False
        self.living = True
        
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def bounceScreen(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = -self.speedx
            self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = -self.speedy
            self.didBounceY = True
            
    def bouncePac(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.dist(other.rect.center) < self.radius + other.radius:
                    self.living = False
                    
    def bounceWall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if abs((self.rect.x - other.rect.x)) > abs((self.rect.y - other.rect.y)):
                    self.speedx = -self.speedx
                else:
                    self.speedy = -self.speedy
                self.speed = [self.speedx, self.speedy]
                self.rect = self.rect.move(self.speed)
                    
    def dist(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        xDiff = x1 - x2
        yDiff = y1 - y2
        return math.sqrt(xDiff**2 + yDiff**2)  
    
