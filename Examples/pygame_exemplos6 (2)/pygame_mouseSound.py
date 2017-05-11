import pygame
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([500, 500])

pygame.display.set_caption("mouse lunar bug...")

clock = pygame.time.Clock()
 
# Before the loop, load the sounds:
click_sound = pygame.mixer.Sound("0614.ogg")
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
background_image = pygame.image.load("lunar.png").convert()
background_image = pygame.transform.scale(background_image, (500,500))
player_image = pygame.image.load("bug.jpg").convert()
player_image = pygame.transform.scale(player_image, (50,50))
player_boomm = pygame.image.load("boomm.jpg").convert()
player_boomm = pygame.transform.scale(player_boomm, (100,100))

player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
 
    # Copy image to screen:
    screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
    if event.type == pygame.MOUSEBUTTONDOWN:
        screen.blit(player_boomm, [x, y])
    else:
        screen.blit(player_image, [x, y])    
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
