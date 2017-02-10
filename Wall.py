import pygame, sys, math

class Wall():
    def __init__(self, pos=[0,0], size=None):
        self.image = pygame.image.load("Resources\Wall\frontend-large.png")
        if size: 
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = po
        
        
    
            
