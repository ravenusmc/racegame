import pygame 
import time
import random

#Inits pygame and all the modules, it needs to be the first line. 
pygame.init()

display_width = 800
display_height = 600

#color definitions 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#Establishing the car width-I actually found this by trial and error
car_width = 85

#Games width and height. The dimensions are a Tuple.
gameDisplay = pygame.display.set_mode((display_width, display_height))
#Title of the game
pygame.display.set_caption('A Bit Racey')
#Defining the game clock-for frames per second
clock = pygame.time.Clock()
#assing the car.bmp file to carImg
carImg = pygame.image.load('car.bmp')

#defining the blocks that car will have to avoid
def things(thingx, thingy, thingw, thingh, color):
  pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


#Function to make car show up on the screen. 
def car(x,y):
  gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect()

def message_display(text):
  largeText = pygame.font.Font('freesansbold.ttf', 115)
  TextSurf, TextRect = text_objects(text, largeText)
  TextRect.center = ((display_width / 2), (display_height / 2))
  #Draws it to the screen
  gameDisplay.blit(TextSurf, TextRect)

  pygame.display.update() 

  time.sleep(2)

  game_loop()

def crash():
  message_display('You Crashed')

def game_loop():
  x = (display_width * 0.30)
  y = (display_height * 0.6)
  #setting variables to change car location.
  x_change = 0

  thing_startx = random.randrange(0, display_width)
  #We want object to start off the screen that is why it is minus
  thing_starty = -600
  thing_speed = 7
  thing_width = 75
  thing_height = 75

  #Setting a boolean flag to False
  gameExit = False

  while not gameExit:

    #Gets any event that happens on the screen
    for event in pygame.event.get():
      #QUIT is from pgame
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      #Adding ability to move car.
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x_change = -5
        elif event.key == pygame.K_RIGHT:
          x_change = 5

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          x_change = 0

    #Changing the location of the car.
    x += x_change

    gameDisplay.fill(white)
    things(thing_startx, thing_starty, thing_width, thing_height, black)
    thing_starty += thing_speed
    car(x,y)

    #Setting up boundaries 
    if x > display_width - car_width or x < 0:
      crash()

    #Keeps blocks keep coming
    if thing_starty > display_height:
      thing_starty = 0 - thing_height
      thing_startx = random.randrange(0, display_width)

    if y < thing_starty + thing_height:
      print('step 1')
      if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
        print("x cross over")
        crash()

    pygame.display.update()
    #How many frames per second.
    clock.tick(60)

game_loop()
pygame.quit()
quit()








































