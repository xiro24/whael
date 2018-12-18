import pygame as pg
from Entity import randParticle
class main:
    def screen(self):
        backgournd_colour = (0,0,0)
        (width, height) = (600, 400)

        screen = pg.display.set_mode((width,height))
        clock = pg.time.Clock()
        pg.display.set_caption('Whael')
        screen.fill(backgournd_colour)

        e = randParticle(150,50,15)
        e.Particle(screen,width,height)

        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            e.Display(screen,width,height)
            clock.tick(60)
            pg.display.update()
        pg.quit()
m = main()
m.screen()