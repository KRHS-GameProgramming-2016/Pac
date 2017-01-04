import pygame, sys, math, random
from Ball import *
from Wall import *
from Level import *
from PlayerBall import *
pygame.init()

clock = pygame.time.Clock()
.
width = 800 
height = 600
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0
