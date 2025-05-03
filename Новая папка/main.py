import pygame as pg

from random import randint

mw_size = (1000, 800)

pg.init()

class Base_sprite(pg.sprite.Sprite):
    def __init__(self, pic, x, y, w, h, speed_x=0, speed_y=0):
        super().__init__()
        self.picture = pg.transform.scale(
            pg.image.load(pic).convert_alpha(), (w, h)
        )
        self.image = self.picture
        self.rect = self.picture.get_rect()
        self.rect = pg.Rect(x, y, w, h)
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
        self.rect = pg.Rect(x, y, w, h)
        self.speed_x = speed_x
        self.speed_y = speed_y
        
                
    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))

    def update(self):
        global count1
        global count2
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 5:
            self.speed_y *= -1

        elif self.rect.y >= mw_size[1]-60:
            self.speed_y *= -1

        if self.rect.x <= -65:
            self.rect.x = 500
            self.rect.y = 400
            count1 += 1

        if self.rect.x >= mw_size[0]:
            self.rect.x = 500
            self.rect.y = 400
            count2 += 1

class Rocket(Base_sprite):
    def __init__(self, pic, x, y, w, h, speed_y=0):
        self.picture = pg.transform.scale(
            pg.image.load(pic).convert_alpha(), (w, h)
        )
        self.image = self.picture
        self.rect = self.picture.get_rect()
        self.rect = pg.Rect(x, y, w, h)
        self.speed_y = speed_y

    def r_update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed_y
        
        elif keys[pg.K_DOWN] and self.rect.y <= mw_size[1] - 200:
            self.rect.y += self.speed_y
    def l_update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed_y
        
        elif keys[pg.K_s] and self.rect.y <= mw_size[1] - 200:
            self.rect.y += self.speed_y

def set_text(text, x, y, color=(255, 255, 200)):
     mw.blit(font1.render(text, True, color),[x, y])

mw = pg.display.set_mode(mw_size)
pg.display.set_caption("Пинг понг")
clock = pg.time.Clock()


background = pg.transform.scale(pg.image.load("background.png"), mw_size)

ball = Ball('ball2.png', 500, 400, 70, 70, -5, 5)
rocket1 = Rocket('ping_rocket1.png', 30, 390, 50, 200, 5)
rocket2 = Rocket('ping_rocket2.png', 940, 390, 50, 200, 5)

font1 = pg.font.Font(None, 70)

play = True
win = False
game = True
count1 = 0 
count2 = 0 


while play:

    for e in pg.event.get():
        if e.type == pg.QUIT or \
                    (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                play  = False

    if game:         
        mw.blit(background, (0, 0))

        ball.update()
        ball.draw()
        rocket1.r_update()
        rocket1.draw()
        rocket2.l_update()
        rocket2.draw()

        if ball.rect.colliderect(rocket1.rect):
            ball.speed_x *= -1

        if ball.rect.colliderect(rocket2.rect):
            ball.speed_x *= -1

        set_text(f'{count2}:{count1}', 500, 20)

    pg.display.update()
    clock.tick(60)
            