import pygame as pg

from random import randint

mw_size = (1000, 800)

class Base_sprite(pg.sprite.Sprite):
    def __init__(self, pic, x, y, w, h, speed_x=0, speed_y=0):
        super().__init__()
        self.picture = pg.transform.scale(
            pg.image.load(pic).convert_alpha(), (w, h)
        )
        self.image = self.picture
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        
                
    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))
        # pg.draw.rect(mw, (255,0,0), self.rect, 3)


    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Ball(Base_sprite):
    def __init__(self, pic, x, y, w, h, speed_x=0, speed_y=0):
        self.picture = pg.transform.scale(
            pg.image.load(pic).convert_alpha(), (w, h)
        )
        self.image = self.picture
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        
                
    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 5:
            self.speed_y *= -1
        elif self.rect.y >= mw_size[1] - self.:
            self.speed_y *= -1

mw = pg.display.set_mode(mw_size)
pg.display.set_caption("Пинг понг")
clock = pg.time.Clock()


background = pg.transform.scale(pg.image.load("background.png"), mw_size)

ball = Ball('ball2.png', 500, 400, 70, 70, 0, 5)



play = True
win = False
game = True

while play:

    for e in pg.event.get():
        if e.type == pg.QUIT or \
                    (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                play  = False

    if game:         
        mw.blit(background, (0, 0))

        ball.update()
        ball.draw()

    pg.display.update()
    clock.tick(60)
            