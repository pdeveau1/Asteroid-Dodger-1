import sys, pygame
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

#create main function
def main():
  #set maximum refresh rate
  clock.tick(60)
  #set screen color
  screen.fill(color)
  pygame.display.flip()

if __name__ == "__main__":
  main()

