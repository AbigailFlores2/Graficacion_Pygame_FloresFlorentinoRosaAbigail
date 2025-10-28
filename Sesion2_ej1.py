import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tablero de Ajedrez")

PINK_LIGHT = (255, 182, 193)
BLANCO = (255, 255, 255)

# Tamaño de cada casilla
TAM_CASILLA = 100

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar el tablero
    for fila in range(8):
        for columna in range(8):

            # Alternar colores usando suma de índices
            if (fila + columna) % 2 == 0:
                color = BLANCO
            else:
                color = PINK_LIGHT

            # Calcular posición y dibujar casilla
            x = columna * TAM_CASILLA
            y = fila * TAM_CASILLA
            pygame.draw.rect(ventana, color, (x, y, TAM_CASILLA, TAM_CASILLA))

    pygame.display.flip()

pygame.quit()