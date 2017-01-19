import pygame, sys, math
from Wall import *
class Level():
    def __init__(self, levelFile):
        self.walls = []
        self.players = []
        self.cheeses = []
        self.ghosts = []
        
        self.loadLevel(levelFile) 
        
    def loadLevel(self, levelFile):        
        f = open("Resources/Levels/"+levelFile, 'r')
        lines = f.readlines()
        f.close()

        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]
            
        lines = newlines
        
        for line in lines:
            print line
        print "________________________"
        
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c == '#':
                    self.walls += [Wall([x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
                #if c == 'p':
                    #self.players += [Player([x*self.tileSize + self.tileSize/2,
                                        #y*self.tileSize + self.tileSize/2],
                                       #self.tileSize)
                                  #]
                
                if c == 'c':
                    self.cheeses += [Cheese([x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
