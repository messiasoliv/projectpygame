import pygame
from random import randrange

def image_asteroide():
    img = pygame.image.load("ast.png").convert()
    img = pygame.transform.scale(img, (40,40))
    return img

def cria_asteroide():
    return {
        'surface': image_asteroide(),
        'posicao': [randrange(460), -40],
        'speed': randrange(1,11)
    }
 
