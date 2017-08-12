import pygame
pygame.init()
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('bugatti.png')

def car(x,y):
    #blit is used to show image and x,y is where we want to show image
    gameDisplay.blit(carImg,(x,y))

x = (display_width * 0.35)
y = (display_height * 0.8)
crashed = False
while not crashed:
    # it gets the event what is doing on the screen where is mouse or the key pressed
    for event in pygame.event.get():
        # to quit from window it close the and detect when person click x and display pop up message are you want to quit
        if event.type == pygame.QUIT:
            crashed = True
        # print all event which pygame is tracking only for single frame
        # print (event)
    # in this we can put single thing which we want to update like update(xyz) but in .flip() everything is updated
    # to change background coloe
    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    # its no of frames per second we will change as fast we want to move
    clock.tick(30)
pygame.quit()
quit()