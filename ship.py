import pygame

#create Ship class
class Ship(pygame.sprite.Sprite):

  #create __init__ function that takes in position
  def __init__(self,pos):
    super().__init__()
    #create image
    self.image = pygame.image.load('ship.png')
    #scale image
    self.image = pygame.transform.smoothscale(self.image,(40,40))
    #rotate image
    self.image = pygame.transform.rotate(self.image,-90)
    #create image rectangle
    self.rect = self.image.get_rect()
    #move center of rectangle to position
    self.rect.center = pos
    #set speed
    self.speed = pygame.math.Vector2(0,0)

  #create function to update image
  def update(self):
    #update ships speed
    self.rect.move_ip(self.speed)

  #check if ship has been reset
  def checkReset(self,endPos):
    return self.rect.center[0]>endPos
    
  #reset to original position
  def reset(self,pos):
    self.rect.center = pos

  def edges(self,edgeWall):
    if self.rect.top <= 0:
      self.rect.top = 1
    if self.rect.bottom >= edgeWall:
      self.rect.bottom = edgeWall - 1