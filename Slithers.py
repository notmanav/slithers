import pygame
import time
import random

pygame.init()

display_width=800
display_height=600
fps=15

block_size = 10
apple_size = 50
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green = (0,155,0)
lives =10

gameDisplay = pygame.display.set_mode ((display_width,display_height))
pygame.display .set_caption ("Slithers");

img = pygame.image.load('snake.png')

clock = pygame.time.Clock()

#direction = "right"

font = pygame.font.SysFont(None, 25)



def snake(block_size, snakelist, direction):
    if direction == "right":
        head = img
    if direction == "up":
        head = pygame.transform.rotate(img,90)
    if direction == "left":
        head = pygame.transform.rotate(img,180)
    if direction == "down":
        head = pygame.transform.rotate(img,270)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def pause():
    backInBusiness = False
    while not backInBusiness:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or pygame.K_DOWN or pygame.K_LEFT or pygame.K_RIGHT :
                    backInBusiness=True
                    print(backInBusiness)


def text_objects(text,color):
    textSurface=font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color):
      textSurf, textRect = text_objects(msg, color)
      textRect.center = (display_width/2), (display_height/2)
      gameDisplay.blit(textSurf,textRect)  

def gameLoop():   

    gameExit=False
    gameOver=False
    lead_x=display_width/2
    lead_y=display_height/2

    lead_x_change=0
    lead_y_change=0

    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10

    snakelist = []
    snakelength=1
    direction ="right"

    lives = 10
        
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to continue or Q to quit",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver=False
                    gameExit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver=False
                        gameExit=True
                    elif event.key == pygame.K_c:
                        gameLoop()
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change=-block_size
                    lead_y_change=0
                    direction ="left"
                elif event.key == pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    lead_x_change=0
                    lead_y_change=-block_size
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_x_change=0
                    lead_y_change=block_size
                    direction = "down"
        lead_x+=lead_x_change
        lead_y+=lead_y_change

        if (lead_x>=display_width or lead_x <=0 or lead_y>=display_height or lead_y<=0):
            if lives>0:
                pause()
                lives-=1
                print(lives)
            else:
                gameOver = True

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,apple_size,apple_size])

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]
        
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameOver=True

            
        snake(block_size, snakelist, direction)

        pygame.display.update()

        if lead_x>= randAppleX and lead_x<=randAppleX+apple_size-block_size and lead_y >=randAppleY and lead_y <= randAppleY+apple_size-block_size:
            randAppleX = round(random.randrange(0, display_width-apple_size)/10.0)*10
            randAppleY = round(random.randrange(0, display_height-apple_size)/10.0)*10
            snakelength +=1
            
        clock.tick(fps)
    pygame.quit()
    quit()

gameLoop()
