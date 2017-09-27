import pygame
import time
import random
# initiate the pygame module
pygame.init()
# making variables for display_width and display_height
display_height = 600
display_width = 800
# we'll define color using RGB methodology
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#the width of the car in pixels
car_width = 73
# set the size of the display window
gameDisplay = pygame.display.set_mode((display_width,display_height))
# the heading that will be on the top of the display window
pygame.display.set_caption('A bit racey')
# initiate the game clock in the game using frames per second (fps)
clock = pygame.time.Clock()
# loading image in a variable
carImg = pygame.image.load('img/racecar.png')

# defining a function make objects for avoiding things
def things(thingx , thingy , thingw ,thingh, color):
    pygame.draw.rect(gameDisplay , color, [thingx , thingy ,thingw , thingh])




# creating a function to display car on the background at the position x and y from the origin
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

# display message
def crash():
    message_display('You Crashed')

 # define function for the font to be displayed when crashed
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def text_objects(text , font):
    textSurface = font.render (text, True , black)
    return textSurface, textSurface.get_rect()

def game_loop():
    # defining the point where we want our car to start

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
# defining the location of the objects
    thing_startx = random.randrange(0 , display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100


    # by default we'll start the game as not crashed
    gameExit = False
    # creating the loop for crashing
    # this is just our event handling loop
    while not gameExit:
        for event in pygame.event.get(): #getting what user does every frame per second
        # eg clicking mouse or pressing key
            if event.type == pygame.QUIT:
                gameExit == True
        # asking if the user has pressed any key
            if event.type == pygame.KEYDOWN:
                # if the key pressed is left key
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

    # when the pressed key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change=0
        # changing the value of x as the key is pressed
        x+= x_change

        gameDisplay.fill(white) #this will display whole of the background as white
        #things(thingx , thingy ,thingw , thingh, color)
        things(thing_startx , thing_starty , thing_width , thing_height , black)

        thing_starty += thing_speed

        car(x,y) # calling the function to car to display the car by giving them the parameter of x and y, which are the starting point of the car image

    #making boundaries to crash when the car hits the boundary
        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange( 0 , display_width)


        pygame.display.update()
        clock.tick(60) #the no here is fps
game_loop()
pygame.quit()
quit()
