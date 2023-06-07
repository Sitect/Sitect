from pygame import *


class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, width, height):
    super().__init__()
    self.image = transform.scale(image.load(player_image), (width, height))
    self.speed = player_speed
    self.rect = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y
  def reset(self):
    window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
  def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_DOWN] and self.rect.y < win_height - 80:
      self.rect.y += self.speed
  def update_l(self):
    keys = key.get_pressed()
    if keys[K_W] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_S] and self.rect.y < win_height - 80:
      self.rect.y += self.speed
            
back = (200, 255, 255)            
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

player_l = Player('racket.png', 30, 200, 4, 50, 150)
player_r = Player('racket.png', 30, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 80)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

FPS = 60
clock = time.Clock()
finish = False
run = True
while run:
  for e in event.get():
    if e.type == QUIT:
      run = False
  if finish != True:
    window.fill(back)
    player_l.update_l()
    player_r.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
      speed_x *= -1
      speed_y *= 1
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
      speed_y *= -1
    if ball.rect.x < 0:
      finish = True
      window.blit(lose1, (200, 200))
      run_over = True
    if ball.rect.x > win_windth:
      finish = True
      window.blit(lose2, (200, 200))
    player_l.reset()
    player_r.reset()
    ball.reset()
  display.update()
  clock.tick(FPS)
