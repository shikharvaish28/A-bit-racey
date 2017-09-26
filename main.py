import pygame
# initiate the pygame module
pygame.init()
# making variables for display_width and display_height
display_height = 600
display_width = 800
# we'll define colour using RGB methodology
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# set the size of the display window
gameDisplay = pygame.display.set_mode((display_width,display_height))
# the heading that will be on the top of the display window
pygame.display.set_caption('A bit racey')
# initiate the game clock in the game using frames per second (fps)
clock = pygame.time.Clock()
# loading image in a variable
carImg = pygame.image.load('img/racecar.png')
# creating a function to display car on the background
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

# defining the point where we want our car to start

x = (display_width * 0.45)
y = (display_height * 0.8)

# by default we'll start the game as not crashed
crashed = False
# creating the loop for crashing
# this is just our event handling loop
while not crashed:
    for event in pygame.event.get(): #getting what user does every frame per second
    # eg clicking mouse or pressing key
        if event.type == pygame.QUIT:
            crashed == True
    gameDisplay.fill(white) #this will display whole of the background as white
    car(x,y) # calling the function to car to display the car by giving them the parameter of x and y, which are the starting point of the car image
    pygame.display.update()
    clock.tick(60) #the no here is fps
pygame.quit()
quit()
