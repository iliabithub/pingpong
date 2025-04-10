from pygame import *

win_width = 700
win_height = 500
win = display.set_mode((win_width,win_height))
display.set_caption('PingPong is shit')
background = transform.scale(image.load('bg.png'), (win_width,win_height))

FPS = 360
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

left = Player('racket.png',100,350,65,65,2)
right = Player('racket.png',600,350,65,65,2)
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    win.blit(background)
    left.reset()
    left.update_l()
    right.reset()
    right.update_r()

    display.update()
    clock.tick(FPS)