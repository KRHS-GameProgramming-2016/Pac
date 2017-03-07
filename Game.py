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

level = Level("level1.lvl")
pacs = level.ghosts
cheeses = level.cheeses
walls = level.walls
player = level.players[0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_LEFT:
                player.go("left")
            if event.key == pygame.K_RIGHT:
                player.go("right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_LEFT:
                player.go("stop left")
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
      
    player.move()
    player.bounceScreen(size)
    for wall in walls:
        player.bounceWall(wall)
    for cheese in cheeses:    
        if player.bounceCheese(cheese):
            cheeses.remove(cheese)
        
    for pac in pacs:
        pac.move()
        pac.bounceScreen(size)
        for wall in walls:
            pac.bounceWall(wall)
    
    
    
        
    bgColor = r,g,b
    screen.fill(bgColor)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    for cheese in cheeses:
        screen.blit(cheese.image, cheese.rect)
    for pac in pacs:
        screen.blit(pac.image, pac.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
    
