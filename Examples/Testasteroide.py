    
def cria_asteroide():
    my_image = pygame.image.load("ast.png").convert() # Carrega a imagem e carrega
    my_image = pygame.transform.scale(my_image, (40,40)) # Tamanho da image
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
            
