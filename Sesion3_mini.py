import pygame

pygame.init()

# Configuración de ventana y colores
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
azul = (0, 0, 255)
gris = (100, 100, 100)

# Posición inicial y velocidad
x, y = 400, 300
velocidad = 2
ancho, alto = 100, 50

# Lista para almacenar el rastro
rastro = []

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Guardar posición actual en el rastro
    rastro.append((x + ancho // 2, y + alto // 2))  # Centro del rectángulo

    ventana.fill(blanco)

    # Dibujar el rastro
    for pos in rastro:
        pygame.draw.circle(ventana, gris, pos, 5)

    # Dibujar el rectángulo
    pygame.draw.rect(ventana, azul, (x, y, ancho, alto))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()