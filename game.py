import pygame 

#Inits pygame and all the modules, it needs to be the first line. 
pygame.init()

display_width = 800
display_height = 600

#color definitions 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#Games width and height. The dimensions are a Tuple.
gameDisplay = pygame.display.set_mode((display_width, display_height))
#Title of the game
pygame.display.set_caption('A Bit Racey')
#Defining the game clock-for frames per second
clock = pygame.time.Clock()

carImg = pygame.image.load('car.bmp')

#Function to make car show up on the screen. 
def car(x,y):
  gameDisplay.blit(carImg,(x,y))

x = (display_width * 0.30)
y = (display_height * 0.6)

#Setting a boolean flag to False
crashed = False

while not crashed:

  #Gets any event that happens on the screen
  for event in pygame.event.get():
    #QUIT is from pgame
    if event.type == pygame.QUIT:
      crashed = True 

  gameDisplay.fill(white)
  car(x,y)
  pygame.display.update()
  #How many frames per second.
  clock.tick(60)

pygame.quit()
quit()








































