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
def removeAsteroide():
    for asteroide in asteroides:
        if asteroide['posicao'][1] > 600:
            asteroides.remove(asteroide)
def removeAsteroideColidido(pos_a):
    asteroides.remove(pos_a)

def asteteroideDestroyed():
    img = pygame.image.load("boomast.jpg").convert()
    img = pygame.transform.scale(img, (50,50))
    return img
#################################################

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
def criaTiro(x_tiro):
    return{
        'surface':imageTiro(),
        'posicao':[x_tiro,530],
        'speed':randrange(1,4)
        }
def moveTiro():
    for tiro in tiros:
        tiro['posicao'][1] -= 2

def removeTiro():
    for tiro in tiros:
        if tiro['posicao'][1] < 0:
            tiros.remove(tiro)
            
def removeTiroColidido(pos_t):
    tiros.remove(pos_t)
    
def ColisaoTiroAsteroide():
    for tiro in tiros:
        for asteroide in asteroides:
            pos_x_ast = asteroide['posicao'][0]
            pos_y_ast = asteroide['posicao'][1]

            pos_x_tiro = tiro['posicao'][0]
            pos_y_tiro = tiro['posicao'][1]

            if pos_y_tiro == pos_y_ast:
                for posX in range(41):
                    if (pos_x_tiro == pos_x_ast + posX) or (pos_x_tiro == pos_x_ast - posX):
                        removeTiroColidido(tiro)
                        removeAsteroideColidido(asteroide)
                        screen.blit(asteteroideDestroyed(),[pos_x_tiro,pos_y_tiro])
                        pygame.display.update()

            
                
####################################
x = 300

ticks_to_asteroide = 90
asteroides = []
tiros = []
done = False

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

            
            if event.key == pygame.K_SPACE:
                tiros.append(criaTiro(x+25))
                
    moveTiro();
    for tiro in tiros:
        screen.blit(tiro['surface'], tiro['posicao'])
                      
    ColisaoTiroAsteroide()
   
    screen.blit(imageNave(),[x,525])

    moveAsteroide()
    for asteroide in asteroides:
        screen.blit(asteroide['surface'], asteroide['posicao'])

 
    pos_nave = []
    pos_nave = [x,500]
    for asteroide in asteroides:
        pos_x_ast = asteroide['posicao'][0]
        pos_y_ast = asteroide['posicao'][1]

        pos_x_nav = pos_nave[0]
        pos_y_nav = pos_nave[1]

        if pos_y_nav == pos_y_ast:
            for posX in range(21):
                if (pos_x_nav+posX == pos_x_ast) or (pos_x_nav-posX == pos_x_ast):
                    screen.blit(naveDestroyed(),[pos_x_nav,500])
                    
                    done = True
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    #print (asteroides)
    removeAsteroide()
    removeTiro()
#pygame.quit()
