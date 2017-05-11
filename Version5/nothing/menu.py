import pygame
import colors

pygame.init()
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("Menu Asteroide")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(colors.BLACK())
    pygame.display.flip()

pygame.quit()
