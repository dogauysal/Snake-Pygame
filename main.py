import pygame
import os

from enums import Directions,Colors,GameVariables as gv

from classes.Food import Food
from classes.Snake import Snake
from classes.Button import Button


pygame.init()

screen = pygame.display.set_mode((gv.SCREEN_WIDTH,gv.SCREEN_HEIGHT))

gameSurface = pygame.Surface((gv.SURFACE_WIDTH,gv.SURFACE_HEIGHT))
gameSurface = gameSurface.convert()
gameSurface.fill(Colors.BLACK)

pygame.display.set_caption(gv.GAME_CAPTION)
clock = pygame.time.Clock()

screen.blit(gameSurface,(0,gv.TEXT_AREA_HEIGHT))


#Score and text area

textSurface = pygame.Surface((gv.SURFACE_WIDTH,gv.TEXT_AREA_HEIGHT))
textSurface = textSurface.convert()
textSurface.fill(Colors.BLACK)

FONT = pygame.font.SysFont('comicsansms',20)
GAME_TEXT = FONT.render(gv.GAME_CAPTION,True,Colors.WHITE)



def gameOver():

    gv.INTRO = True
    gv.DONE = True
    
    gameIntro()

def CheckSnakeFoodCollision(_snake,_food):

    if _snake.getSnakesHeadPosition() == _food.position:
        _snake.length += 1
        _snake.score += gv.SELECTED_LEVEL[0]
        _food.randomLocation()
         

def gameIntro():

    introSurface = pygame.Surface(screen.get_size())
    introSurface = introSurface.convert()
    introSurface.fill(Colors.BLACK)


    introText = FONT.render(gv.GAME_CAPTION,True,Colors.WHITE)
    introTextRect = introText.get_rect(center=(gv.SCREEN_WIDTH/2, gv.SCREEN_HEIGHT*0.25))
    introSurface.blit(introText,introTextRect)
   
    while gv.INTRO:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gv.INTRO = False
                pygame.quit()
                os._exit(1)


        playButton = Button("btn_play")
        playButton.drawRectangleButton(introSurface,gv.SCREEN_WIDTH/2,gv.SCREEN_HEIGHT/2,100,50,"PLAY" ,FONT,Colors.WHITE,Colors.GREEN,gameStart)

        i = 0
        while i < gv.LEVEL_COUNT:
            
            levelButton = Button(i+1)
            
            if i + 1 != gv.SELECTED_LEVEL[0]:
                levelButton.drawCircleButton(introSurface,Colors.WHITE,gv.START_X+(i*((2*gv.RADIUS)+(2*gv.BUTTON_MARGIN))),gv.START_Y,gv.RADIUS,0,FONT,str(i+1),Colors.BLACK)
            else:
                levelButton.drawCircleButton(introSurface,Colors.GREEN,gv.START_X+(i*((2*gv.RADIUS)+(2*gv.BUTTON_MARGIN))),gv.START_Y,gv.RADIUS,0,FONT,str(i+1),Colors.BLACK)
                
            
            i+=1
        
        text = FONT.render("Last Score: " + str(gv.LAST_SCORE),True,Colors.WHITE)
        textRect = text.get_rect(center=(gv.SURFACE_WIDTH / 2,350))

        introSurface.blit(text,textRect)
            
        screen.blit(introSurface,(0,0))

        pygame.display.flip()
        pygame.display.update()

def gameStart(): 

    gv.INTRO = False
    gv.DONE = False
    snake = Snake(0)
    food = Food()

    while not gv.DONE:
        
        clock.tick(gv.SELECTED_LEVEL[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gv.DONE = True
                pygame.quit()
                os._exit(1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.switchDirection(Directions.RIGHT)
                elif event.key == pygame.K_LEFT:
                    snake.switchDirection(Directions.LEFT)
                elif event.key == pygame.K_UP:
                    snake.switchDirection(Directions.UP)
                elif event.key == pygame.K_DOWN:
                    snake.switchDirection(Directions.DOWN)


        if snake.move(snake.direction) != False:
             #Game
            gameSurface.fill((0,0,0))
            CheckSnakeFoodCollision(snake,food)
            snake.drawSnake(gameSurface)
            food.drawFood(gameSurface)
            screen.blit(gameSurface,(0,gv.TEXT_AREA_HEIGHT))
                

            pygame.draw.line(screen, Colors.WHITE, (0,gv.TEXT_AREA_HEIGHT), (gv.SURFACE_WIDTH,gv.TEXT_AREA_HEIGHT), 2)

            # Text
            LEVEL_TEXT = FONT.render("Level " + str(gv.SELECTED_LEVEL[0]),True,Colors.WHITE)
            textSurface.fill(Colors.BLACK)
            SCORE_TEXT = FONT.render(str(snake.score),True,Colors.WHITE)
            textSurface.blit(LEVEL_TEXT,(50,10))
            textSurface.blit(GAME_TEXT, (gv.SURFACE_WIDTH/2 -50,10))
            textSurface.blit(SCORE_TEXT, (gv.SURFACE_WIDTH-50,10))
            screen.blit(textSurface,(0,0))

            pygame.display.flip()
            pygame.display.update()
            
        else:
            gv.LAST_SCORE = snake.score
            gameOver()

    # pygame.quit()
    
gameIntro()
gameStart()



