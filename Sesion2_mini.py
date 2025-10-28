import pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Casa con cambio de color")

# Colores
ROSA = (255, 105, 180)
AZUL_LIGHT = (100, 150, 255)
BLANCO = (255, 255, 255)
GRIS = (180, 180, 180)

# Color inicial de la casa
color_casa = ROSA

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                color_casa = ROSA
            elif evento.key == pygame.K_b:
                color_casa = AZUL_LIGHT

    ventana.fill(GRIS)  # Fondo gris claro

    # Cuerpo de la casa (rectángulo)
    x = 300
    y = 300
    ancho = 200
    alto = 200
    pygame.draw.rect(ventana, color_casa, (x, y, ancho, alto))

    # Tejado (triángulo)
    punto1 = (x, y)
    punto2 = (x + ancho // 2, y - 100)
    punto3 = (x + ancho, y)
    pygame.draw.polygon(ventana, color_casa, [punto1, punto2, punto3])

    # Ventanas (círculos)
    pygame.draw.circle(ventana, BLANCO, (x + 50, y + 60), 20)
    pygame.draw.circle(ventana, BLANCO, (x + 150, y + 60), 20)

    pygame.display.flip()

pygame.quit()