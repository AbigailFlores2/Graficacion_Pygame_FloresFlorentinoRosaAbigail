import pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Cambio de color con tecla C")

# Definir colores
LILA  = (210, 150, 227)
AZUL_LIGHT = (173, 216, 230)

# Color inicial
color_fondo = LILA

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            # Cambia el color al presionar C
            if evento.key == pygame.K_c: 
                # Alternar entre LILA y AZUL_LIGHT
                if color_fondo == LILA:
                    color_fondo = AZUL_LIGHT
                else:
                    color_fondo = LILA

    ventana.fill(color_fondo)
    pygame.display.flip()

pygame.quit()