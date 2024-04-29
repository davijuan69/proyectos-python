import pygame as py, random as r

py.init()

ancho = 1280
alto = 720

sreen = py.display.set_mode((ancho, alto))

py.display.set_caption("pong")

clock = py.time.Clock()

jugador = py.Rect(ancho-110, alto/2-50, 10, 100)
jugador2 = py.Rect(110, alto/2-50, 10, 100)

pelota = py.Rect(ancho/2-10, alto/2-10, 20, 20)
x_velocidad, y_velocidad = 1, 1

while True: 
    keypress = py.key.get_pressed()

    if keypress[py.K_UP]:
        if jugador.top > 0:
            jugador.y -= 2

    if keypress[py.K_DOWN]:
        if jugador.bottom < alto:
            jugador.y += 2

    pelota.x += x_velocidad
    pelota.y += y_velocidad

    
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()

    sreen.fill((0, 0, 0))

    py.draw.rect(sreen, (255, 255, 255), jugador)
    py.draw.rect(sreen, (255, 255, 255), jugador2)
    py.draw.circle(sreen, (255, 255, 255), (pelota.center), 10)

    py.display.update()
    clock.tick(300)