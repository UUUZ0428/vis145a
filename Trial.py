#reference
#https://pythonprogramming.net/making-interactive-pygame-buttons/
#https://pythonprogramming.net/pygame-button-function-events/
#https://stackoverflow.com/questions/47639826/pygame-button-single-click

import pygame
import random
from random import randint
import time
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)
green = (0,200,0)
bright_green = (0,255,0)

pygame.init()
display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Geisel Library Simulator")

ACTIVE_COLOR = pygame.Color('dodgerblue1')
INACTIVE_COLOR = pygame.Color('dodgerblue4')
FONT = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
geiselImg = pygame.image.load("geisel.jpeg")
#fit the background image to screen
geiselImg = pygame.transform.scale(geiselImg, (display_width, display_height))
recurringImg = pygame.image.load("recurring.png")
launchImg = pygame.image.load("launch.png")
join_audioImg = pygame.image.load("join_audio.png")
open_zoomImg = pygame.image.load("open_zoom.png")
shareImg = pygame.image.load("share_screen.png")
muteImg = pygame.image.load("mute.png")
imageList = [recurringImg,launchImg,join_audioImg,open_zoomImg,shareImg]

def text_objects(text, font):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rgb = [r,g,b]

    textSurface = font.render(text, True, rgb)
    return textSurface, textSurface.get_rect()

def draw_button(button, screen):
    #Draw the button rect and the text surface.
    pygame.draw.rect(screen, button['color'], button['rect'])
    screen.blit(button['text'], button['text rect'])


def create_button(x, y, w, h, text, callback):
    # The button is a dictionary consisting of the rect, text,
    # text rect, color and the callback function.
    text_surf = FONT.render(text, True,green)
    button_rect = pygame.Rect(x, y, w, h)
    text_rect = text_surf.get_rect(center=button_rect.center)
    button = {
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': INACTIVE_COLOR,
        'callback': callback,
        }
    return button


def main():
    gameExit = False
    action = False

    def quit_game():
        pygame.display.quit()
        quit()

    def image_display():
        for i in range(200):
            posx = randint(0,400)
            posy = randint(0,400)
            size = randint(0,100)
            index = randint(0,len(imageList)-1)
            gameDisplay.blit(imageList[index],(posx,posy))
            time.sleep(0.3)
            pygame.display.update()

    button1 = create_button(320, 300, 250, 80, 'Start!', image_display)
    button2 = create_button(320, 400, 250, 80, 'Quit', quit_game)
    # A list that contains all buttons.
    button_list = [button1, button2]

    while not gameExit:
        for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   gameExit = True
               # This block is executed once for each MOUSEBUTTONDOWN event.
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   # 1 is the left mouse button, 2 is middle, 3 is right.
                   if event.button == 1:
                       for button in button_list:
                           # `event.pos` is the mouse position.
                           if button['rect'].collidepoint(event.pos):
                               # Increment the number by calling the callback
                               # function in the button list.
                               button['callback']()
               elif event.type == pygame.MOUSEMOTION:
                   # When the mouse gets moved, change the color of the
                   # buttons if they collide with the mouse.
                   for button in button_list:
                       if button['rect'].collidepoint(event.pos):
                           button['color'] = ACTIVE_COLOR
                       else:
                           button['color'] = INACTIVE_COLOR

        #display background image
        gameDisplay.blit(geiselImg,(0,0))
        text = FONT.render("Geisel Library Simulator",True,green)
        gameDisplay.blit(text,(250, 200))

        for button in button_list:
            draw_button(button, gameDisplay)
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
