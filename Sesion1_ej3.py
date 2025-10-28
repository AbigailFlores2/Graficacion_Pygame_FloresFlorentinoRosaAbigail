import pygame
pygame.init()

ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mi primer programa gráfico")

lila = (210, 150, 227)
COLOR_FONDO = lila

# Inicializa el contador de frames
frame_actual = 0  
# Límite de frames
MAX_FRAMES = 300 

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

    frame_actual += 1
    # Imprime el número de frame en la terminal
    print(f"Frame: {frame_actual}")  

    if frame_actual >= MAX_FRAMES:
        corriendo = False

pygame.quit()