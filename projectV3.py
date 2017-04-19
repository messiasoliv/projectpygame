import pygame
from pygame.locals import *
from sys import exit
from random import randrange

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

# Esconde o cursor do mouse
pygame.mouse.set_visible(0)

size = (500, 600) # Tamanho da tela
screen = pygame.display.set_mode(size) # Define o tamanho da tela
 
pygame.display.set_caption("Asteroide") # Legenda do jogo

clock = pygame.time.Clock() # Ainda não sei para que serve ###########

############################# Módulo Asteroide ################################    
def cria_asteroide():
    my_image = pygame.image.load("ast.png").convert() # Carrega a imagem e carrega
    my_image = pygame.transform.scale(my_image, (40,40)) # Tamanho da imagem
    return {
        'surface': my_image, # Imagem a ser usada
        'posicao': [randrange(460), -40], # Defina a posição do asteroide
        'speed': randrange(1,11)
    }

ticks_to_asteroide = 90
asteroides = [] # Vetor para adicionar todos os asteroides

# Função para mover o asteroide 
def move_asteroide():
    for asteroide in asteroides:
        asteroide['posicao'][1] += asteroide['speed']

# Remove o asteroide quando passou do limite da tela
def remove_asteroide():
    for asteroide in asteroides:
        if asteroide['posicao'][1] > 600:
            asteroides.remove(asteroide)
#################################################

def nave():
    my_nave = pygame.image.load("nave.png").convert() # Carrega a image e carrega a imagem da nave
    my_nave = pygame.transform.scale(my_nave, (60,60)) # Tamanho da imagem
    
    return my_nave

def colisao(posicao_nave,posicao_asteroide):
    pass
def screenEnd():
    screen.fill(WHITE)
x = 60 # Posição x inicial
  
done = False    
while not done:
    if not ticks_to_asteroide:
        ticks_to_asteroide = 90
        asteroides.append(cria_asteroide())
    else:
        ticks_to_asteroide -= 1
    speed = {
        'x':0,
        'y':0
    }
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10    
        nave()
    
    screen.fill(WHITE)

    move_asteroide()

    screen.blit(nave(),[x,530])
    
    for asteroide in asteroides:
        screen.blit(asteroide['surface'], asteroide['posicao'])
        
        for p_n in range (-40,41):
            if (asteroide['posicao'][0] == (x + p_n) and asteroide['posicao'][1] == 530):
                print ("Colisão")
                screenEnd()
                done = True
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

    remove_asteroide()
    
pygame.quit()
