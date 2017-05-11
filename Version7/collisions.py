
##### Colisões ##########   

def ColisaoTiroAsteroide(screen,tiros,asteroides):
    
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
def ColisaoNaveAsteroide(screen,asteroides,x,y):
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
