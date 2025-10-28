import pygame
pygame.init()

ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mi primer programa gráfico")

lila = (210, 150, 227)
COLOR_FONDO = lila

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    #Llenar la ventana con el color        
    ventana.fill(COLOR_FONDO)
    pygame.display.flip()

pygame.quit()

