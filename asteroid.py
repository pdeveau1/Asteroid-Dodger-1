import pygame, random

class Asteroid(pygame.sprite.Sprite):
  def __init__(self,pos,size):
    super().__init__()
    #create image
    self.image = pygame.image.load("asteroid.png")
    #scale image using size variable
    self.image = pygame.transform.smoothscale(self.image,(size,size))
    #create rectangle of image
    self.rect = self.image.get_rect()
    #move center of rectangle to pos
    self.rect.center = pos
    #create speed
    self.speed = pygame.math.Vector2(0,3)
    self.speed.rotate_ip(random.randint(0,360))

  def update(self):
    screen_info = pygame.display.Info()
    self.rect.move_ip(self.speed)
    #collision detection
    #check of hit left or right wall
    if self.rect.left < 0 or self.rect.right>screen_info.current_w:
      #flip left/right direction
      self.speed[0] *= -1
      #flip image on x-axis
      self.image = pygame.transform.flip(self.image,True,False)
      self.rect.move_ip(self.speed[0],0)
    #check if hit top or bottom wall
    if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:
      #flip up/down direction
      self.speed[1] *= -1
      #flip image on y-axis
      self.image = pygame.transform.flip(self.image,False,True)
      self.rect.move_ip(0,self.speed[1])


