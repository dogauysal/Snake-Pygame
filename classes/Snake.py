import pygame
from enums import Colors, Directions, GameVariables as gv


class Snake(object):

    def __init__(self,score):
        self.rect = pygame.Rect(gv.SURFACE_WIDTH / 2, gv.SURFACE_HEIGHT / 2,gv.SNAKE_WIDTH,gv.SNAKE_HEIGHT)
        self.positions = [((gv.SURFACE_WIDTH/2),(gv.SURFACE_HEIGHT/2))]
        self.color = Colors.WHITE
        self.direction = Directions.RIGHT
        self.length = 1
        self.lastScore = 0
        self.score = score
        

    def move(self,direction):
        curX,curY = self.positions[0]

        directionSwitch = {
            Directions.RIGHT: [
                curX + gv.STEP,
                curY
                ],
            Directions.LEFT: [
                curX - gv.STEP,
                curY
                ],
            Directions.UP: [
                curX,
                curY - gv.STEP],
            Directions.DOWN: [
                curX,
                curY + gv.STEP]
        }

        newX,newY = directionSwitch.get(direction,"")

        if newX == gv.SURFACE_WIDTH or newX < 0:
            newX = newX - (direction * gv.SURFACE_WIDTH)
        
        if newY == gv.SURFACE_HEIGHT or newY < 0:
            newY = newY - ((direction/2)* gv.SURFACE_HEIGHT)

        new = (newX,newY)

        if self.length > 2 and new in self.positions:
            return False
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def switchDirection(self,new):
        
        if self.length > 1  and self.direction * -1 == new :
            return
        else:
            self.direction = new
    
    def getSnakesHeadPosition(self):

        return self.positions[0]
        
    def drawSnake(self,surface):
        for p in self.positions:
            rect = pygame.Rect((p[0],p[1]),(gv.SNAKE_WIDTH,gv.SNAKE_HEIGHT))
            pygame.draw.rect(surface,self.color,rect)
