import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)

# Posición y velocidad
x, y = 400, 300
velocidad = 1
ancho, alto = 100, 50

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and x > 0:
        x -= velocidad
    if teclas[pygame.K_RIGHT] and x < 800 - ancho:
        x += velocidad
    if teclas[pygame.K_UP] and y > 0:
        y -= velocidad
    if teclas[pygame.K_DOWN] and y < 600 - alto:
        y += velocidad

    # Detectar si está tocando los bordes
    tocando_borde = (
        x <= 0 or x >= 800 - ancho or
        y <= 0 or y >= 600 - alto
    )
    color_rectangulo = rojo if tocando_borde else azul

    ventana.fill(blanco)
    pygame.draw.rect(ventana, color_rectangulo, (x, y, ancho, alto))
    pygame.display.flip()

pygame.quit()