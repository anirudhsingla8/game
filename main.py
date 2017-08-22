import pygame
import random
import time
pygame.init()
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
car_width = 128
block_color = (53,115,255)
gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('bugatti.png')

# added score
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
    # blit is used to show image and x,y is where we want to show image
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, (0,255,0))
    return textSurface, textSurface.get_rect()


def message_display(text):
    # large text is font defined
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')


def game_loop():
    x = (display_width * 0.35)
    y = (display_height * 0.8)
    x_change = 0
    # from where the object start
    thing_startx = random.randrange(0, display_width)
    # satrting position of object y
    thing_starty = -600
    # moving speed of object
    thing_speed = 3
    # width of object
    thing_width = 100
    thing_height = 100
    dodged = 0
    gameExit = False
    while not gameExit:
        # it gets the event what is doing on the screen where is mouse or the key pressed
        for event in pygame.event.get():
            # to quit from window it close the and detect when person click x and display pop up message are you want to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        # in this we can put single thing which we want to update like update(xyz) but in .flip() everything is updated
        # to change background color
        gameDisplay.fill(white)
        # things(thingx, thingy, thingw, thingh, color):
        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged*1.2)
        # crash logic is here
        # here y is y dimension of car and thing_starty + thing_height is of object
        if y < thing_starty + thing_height:
            print('y crossover')
            # here x is x dimension of car
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('c crossover')
                crash()



        pygame.display.update()
        # its no of frames per second we will change as fast we want to move
        clock.tick(60)
game_loop()
pygame.quit()
quit()