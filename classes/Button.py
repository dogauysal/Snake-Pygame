import pygame
import math
from enums import GameVariables as gv

class Button(object):

    def __init__(self,id):
        self.id = id
        self.selected = False
        
    def drawRectangleButton(self,surface,x,y,w,h,caption,font,textColor,buttonColor,action = None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        buttonSurface = pygame.Surface((w,h))
        buttonSurface = buttonSurface.convert()
        buttonSurface.fill(buttonColor)

        text = font.render(caption,True,textColor)

        textRect = text.get_rect(center=(x,y))
        buttonSurfaceRect = buttonSurface.get_rect(center=(x,y))

        surface.blit(buttonSurface,buttonSurfaceRect)
        surface.blit(text,textRect)

        if buttonSurfaceRect.x + w > mouse[0] and buttonSurfaceRect.y + h > mouse[1] > buttonSurfaceRect.y:
            if click[0] == 1 and action is not None:
                action()

    def drawCircleButton(self,surface,buttonColor,x,y,radius,width,font,caption,captionColor):

        click = pygame.mouse.get_pressed()

        text = font.render(caption,True,captionColor)
        textRect = text.get_rect(center=(x,y))

        pygame.draw.circle(surface,buttonColor,(int(x),int(y)),radius,width)
        surface.blit(text,textRect)

        if click[0] == 1:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]

            sqX = (mouseX - x)**2
            sqY = (mouseY - y)**2

            if math.sqrt(sqX + sqY) < radius:
                curLevel = str(self.id)
                levelSwitch = {
                    "1": gv.LEVEL_1,
                    "2": gv.LEVEL_2,
                    "3": gv.LEVEL_3,
                    "4": gv.LEVEL_4,
                    "5": gv.LEVEL_5,
                    "6": gv.LEVEL_6,
                    "7": gv.LEVEL_7,
                    "8": gv.LEVEL_8,
                    "9": gv.LEVEL_9,
                    "10": gv.LEVEL_10
                }

                gv.SELECTED_LEVEL = levelSwitch.get(curLevel,"")
                self.selected = True
            else:
                self.selected = False
                
                   

                    