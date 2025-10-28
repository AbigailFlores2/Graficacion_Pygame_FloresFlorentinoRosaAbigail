import pygame
pygame.init()

ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mi primer programa gráfico")

AZUL_LIGHT = (173, 216, 230)
COLOR_FONDO = AZUL_LIGHT

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            
        elif evento.type == pygame.KEYDOWN:

            # Verifica si se presionó la tecla Esc
            if evento.key == pygame.K_ESCAPE:  
                corriendo = False

    #Llenar la ventana con el color        
    ventana.fill(COLOR_FONDO)
    pygame.display.flip()

pygame.quit()