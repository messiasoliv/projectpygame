import pygame
from pygame.locals import *
from sys import exit
from random import randrange
import colors

pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode((500,600)) 
pygame.display.set_caption("Asteroide") 
clock = pygame.time.Clock()

x = 300
y = 525
ticks_to_asteroide = 90
asteroides = []
tiros = []
done = False

############################# Módulo Asteroide ################################
def imageAsteroide():
    img = pygame.image.load("ast.png").convert()
    img = pygame.transform.scale(img, (40,40))
    return img
def criaAsteroide():
    return {
        'surface': imageAsteroide(),
        'posicao': [randrange(460), -40],
        'speed': 2
    }
def moveAsteroide():
    for asteroide in asteroides:
        asteroide['posicao'][1] += asteroide['speed']
        screen.blit(asteroide['surface'], asteroide['posicao'])
    
def removeAsteroide():
    for asteroide in asteroides:
        if asteroide['posicao'][1] > 600:
            asteroides.remove(asteroide)
def removeAsteroideColidido(pos):
    asteroides.remove(pos)

def asteroideDestroyed():
    img = pygame.image.load("boomast.jpg").convert()
    img = pygame.transform.scale(img, (50,50))
    return img
#################################################

###### Contruir NAVE #######
def mostraNave(x,y):
    screen.blit(imageNave(),[x,y])

def imageNave():
    img = pygame.image.load("nave.png").convert() 
    img = pygame.transform.scale(img, (60,90))
    return img

def naveDestroyed():
    destroyed = pygame.image.load("boom.jpg").convert()
    destroyed = pygame.transform.scale(destroyed, (100,100))
    return destroyed

#######################################
def imageTiro():
    img = pygame.image.load("tiro.png").convert()
    img = pygame.transform.scale(img,(10,10))
    return img
def criaTiro(x_tiro,y_tiro):
    return{
        'surface':imageTiro(),
        'posicao':[x_tiro,y_tiro],
        'speed':randrange(1,4)
        }
def moveTiro():
    for tiro in tiros:
        tiro['posicao'][1] -= 2
        screen.blit(tiro['surface'], tiro['posicao'])
        
def removeTiro():
    for tiro in tiros:
        if tiro['posicao'][1] < 0:
            tiros.remove(tiro)
            
def removeTiroColidido(pos_t):
    tiros.remove(pos_t)


####### Colisões ##########   
def ColisaoTiroAsteroide():
    for tiro in tiros:
        for asteroide in asteroides:
            pos_x_ast = asteroide['posicao'][0]
            pos_y_ast = asteroide['posicao'][1]

            pos_x_tiro = tiro['posicao'][0]
            pos_y_tiro = tiro['posicao'][1]
            
            dif_x = pos_x_tiro - pos_x_ast
            if (dif_x < 30 and dif_x > -30):
                dif_y = pos_y_tiro - pos_y_ast
                if (dif_y < 7):
                    screen.blit(asteroideDestroyed(),[pos_x_tiro,pos_y_tiro])
                    removeTiroColidido(tiro)
                    removeAsteroideColidido(asteroide)               
            else:
                break
def ColisaoNaveAsteroide(x,y):
    for asteroide in asteroides:
        pos_x_ast = asteroide['posicao'][0]
        pos_y_ast = asteroide['posicao'][1]

        
        dif_y = y - pos_y_ast
        if (dif_y < 7 and dif_y > -30):
            dif_x = x - pos_x_ast
            if (dif_x < 45 and dif_x > -45):       
                screen.blit(asteroideDestroyed(),[pos_x_ast,pos_y_ast])           
                screen.blit(naveDestroyed(),[x,y])
            
                return True
    return False
####################################

while not done:
    if not ticks_to_asteroide:
        ticks_to_asteroide = 200
        asteroides.append(criaAsteroide())
    else:
        ticks_to_asteroide -= 1

    screen.fill(colors.BLACK())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if (x-10) >= 0:
                    x -= 10
            elif event.key == pygame.K_RIGHT:
                if (x+10) <= 445:
                    x += 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                if (y <= 525):
                    y += 10

            if event.key == pygame.K_SPACE:
                tiros.append(criaTiro(x+25,y+25))
                
    moveTiro();
        
    ColisaoTiroAsteroide() 
    
    mostraNave(x,y)
    
    moveAsteroide()
    done = ColisaoNaveAsteroide(x,y)
    
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    #print (asteroides)
    removeAsteroide()
    removeTiro()
#pygame.quit()
