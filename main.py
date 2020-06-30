#main file
import sys, pygame
from ship import*
from pygame.locals import*

pygame.init()
screen_info = pygame.display.Info()

#set the width and height to the size of the screen
size = (width,height) = (int(screen_info.current_w*0.5),int(screen_info.current_h*0.5))
screen = pygame.display.set_mode(size)

#create clock object
clock = pygame.time.Clock()
#create color RGB
color = (30,0,30)
#fill screen with color
screen.fill(color)

#setup game variables
NumLevels = 4
Level = 1
AsteroidCount = 3
Player = Ship((20,200))

#create main function
def main():
  global Level

  while Level <= NumLevels:
    #set our maximum refresh rate
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()

  #set maximum refresh rate
  clock.tick(60)
  #set screen color
  screen.fill(color)
  #add in ship image
  screen.blit(Player.image,Player.rect)
  pygame.display.flip()

if __name__ == '__main__':
  main()

