import pygame
import math

pygame.init()

# Configuración de ventana y colores
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
azul = (0, 0, 255)

# Centro de la trayectoria circular
centro_x, centro_y = 400, 300
radio = 100
angulo = 0
velocidad_angular = 0.01  # Radianes por fotograma

ancho, alto = 100, 50
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Calcular posición circular
    x = centro_x + radio * math.cos(angulo)
    y = centro_y + radio * math.sin(angulo)
    angulo += velocidad_angular

    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, (x, y, ancho, alto))
    pygame.display.flip()
    reloj.tick(60)  # Limita a 60 FPS

pygame.quit()