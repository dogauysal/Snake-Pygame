import pygame
import random
from enums import Colors, GameVariables as gv

class Food(object):

    def __init__(self):
        self.color = Colors.GREEN
        self.position = (0,0)
        self.randomLocation()

    def randomLocation(self):

        self.position = random.randrange(0,gv.SURFACE_WIDTH,10), random.randrange(0,gv.SURFACE_HEIGHT,10)
    
    def drawFood(self,surface):
        rect = pygame.Rect((self.position[0],self.position[1]),(gv.FOOD_WIDTH,gv.FOOD_HEIGHT))
        pygame.draw.rect(surface,self.color,rect)


