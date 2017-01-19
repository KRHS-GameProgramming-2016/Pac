import pygame, sys, math, random

from Cheese import *
from Pac import *
from PlayerPac import *
from Wall import *
from Level import *

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 67, 75, 198

level = Level("level.py")
Cheese = Cheese

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    for pac in pacs:
        pac.move()
        pac.bounceScreen(size)
        
    bgColor = r,g,b
    screen.fill(bgColor)
    for pac in pacs:
        screen.blit(pac.image, pac.rect)
    pygame.display.flip()
    clock.tick(60)
    
