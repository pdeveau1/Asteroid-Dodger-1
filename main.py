#main file
import sys, pygame, pandas as pd
from ship import*
from asteroid import*
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

#read and store game data
df = pd.read_csv("game_info.csv")

#setup game variables
NumLevels = df["LevelNum"].max()
Level = df["LevelNum"].min()
LevelData = df.iloc[Level]
AsteroidCount = LevelData["AsteroidCount"]
Player = Ship((LevelData["PlayerX"],LevelData["PlayerY"]))
Asteroids = pygame.sprite.Group()

#create init function
def init():
  global AsteroidCount,Asteroids,LevelData
  LevelData = df.iloc[Level]
  Player.reset((LevelData["PlayerX"],LevelData["PlayerY"]))
  Asteroids.empty()
  AsteroidCount = LevelData["AsteroidCount"]
  for i in range(AsteroidCount):
    Asteroids.add(Asteroid((random.randint(50,width-50),random.randint(50,height-50)),random.randint(15,60)))

#create win function that displays win screen
def win():
  font = pygame.font.SysFont(None,70)
  text = font.render("You Escaped!",True,(255,0,0))
  text_rect = text.get_rect()
  text_rect.center = (width/2,height/2)
  while True:
    screen.fill(color)
    screen.blit(text,text_rect)
    pygame.display.flip()

#create main function
def main():
  global Level
  init()
  while Level <= NumLevels:
    #set our maximum refresh rate
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      #Check if key being pressed down
      if event.type == pygame.KEYDOWN:
        #Check if it is right arrow
        if event.key == pygame.K_RIGHT:
          #If right arrow set x speed to 10(moving to right)
          Player.speed[0] = 10
        #Check if it is left arrow
        if event.key == pygame.K_LEFT:
          #If left arrow set x speed to -10(moving to left)
          Player.speed[0] = -10
        if event.key == pygame.K_UP:
          Player.speed[1] = -10
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 10
      #Check if key is released
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          #If right arrow set x speed to 0(stop moving)
          Player.speed[0] = 0
        #Check if it is left arrow
        if event.key == pygame.K_LEFT:
          #If left arrow set x speed to 0(stop moving)
          Player.speed[0] = 0
        if event.key == pygame.K_UP:
          Player.speed[1] = 0
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 0
    #update
    Player.update()
    Asteroids.update()
    #check for collision
    get_hit = pygame.sprite.spritecollide(Player,Asteroids,False)
    #set screen color
    screen.fill(color)
    #add asteroids to screen
    Asteroids.draw(screen)
    #add in ship image
    screen.blit(Player.image,Player.rect)
    pygame.display.flip()
    Player.edges(height)
    #if ship reaches edge of screen
    if Player.checkReset(width):
      if Level == NumLevels:
        break
      else:
        Level += 1
      #reset
        init()
    elif get_hit:
      Player.reset((LevelData["PlayerX"],LevelData["PlayerY"]))
  win()

if __name__ == '__main__':
  main()
