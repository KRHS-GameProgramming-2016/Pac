import pygame, sys, math

class Wall():
    def __init__(self, pos=[0,0], size=None):
        self.image = pygame.image.load("C:\Users\PLTW\Documents\Game Programming\Alexander DiDominic\Pac\Resources\Wall\Dunanana_cheese_man.jpd")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos
