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
#assing the car.bmp file to carImg
carImg = pygame.image.load('car.bmp')

#Function to make car show up on the screen. 
def car(x,y):
  gameDisplay.blit(carImg,(x,y))

def game_loop():
  x = (display_width * 0.30)
  y = (display_height * 0.6)
  #setting variables to change car location.
  x_change = 0

  #Setting a boolean flag to False
  crashed = False

  while not crashed:

    #Gets any event that happens on the screen
    for event in pygame.event.get():
      #QUIT is from pgame
      if event.type == pygame.QUIT:
        crashed = True 

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
    car(x,y)
    pygame.display.update()
    #How many frames per second.
    clock.tick(60)



game_loop()
pygame.quit()
quit()








































