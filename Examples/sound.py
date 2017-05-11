import pygame.mixer
import pygame
sounds = pygame.mixer
sounds.init()
 
def espera_tocar(canal):
    while canal.get_busy():
        pass
 
s = sounds.Sound("tiro.egg")
s.play()
