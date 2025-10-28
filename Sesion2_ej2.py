import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Círculos concéntricos")

# Centro de los círculos
centro_x = 800 // 2
centro_y = 800 // 2

# Lista de radios y colores
radios = [20, 40, 60, 80, 100]
colores = [
    
    (173, 255, 47),   # Verde claro
    (170, 255, 195),  # Menta claro
    (255, 182, 193),  # Rosa claro
    (135, 206, 250),  # Azul claro
    (210, 150, 228)   # Morado claro
]

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))  # Fondo blanco

    # Dibujar círculos concéntricos
    for i in range(len(radios)):
        pygame.draw.circle(ventana, colores[i], (centro_x, centro_y), radios[i], width=3)

    pygame.display.flip()

pygame.quit()