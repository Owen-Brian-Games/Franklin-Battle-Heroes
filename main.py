#NOTE: for making buttons there is no built in function so 
#we will make everything controlled with the keyboard
#example (pick attack with keys 1-4)

#imports
import pygame as py
from pygame import mixer
import sys
from pygame.locals import QUIT
import os


#set up window
py.init()
#display size
screenWidth = 720
screenHeight = 720
midWidth = screenWidth/2
midHeight = screenHeight/2
#display surface
DISPLAYSURF = py.display.set_mode((screenWidth, screenHeight))
#set caption
py.display.set_caption('Franklin Battle Heroes')
#clock for maintaining framerate
clock = py.time.Clock()

#font
font = py.font.Font('Assets/Arkitech Medium.ttf', 32)
font1 = py.font.Font('Assets/Arkitech Medium.ttf', 16)
font2 = py.font.Font('Assets/Arkitech Medium.ttf', 10)

#store what screen we are currently in
current_screen = "menu"

#default colors we can use
GREY = (100, 100, 100)
BKGD = (25, 25, 25)
BLUE = (75, 75, 255)
RED = (255, 75, 75)
GREEN = (75, 255, 75)
WHITE = (255, 255, 255)

#menu music
mixer.init()
mixer.music.load("Assets/Franklinite Title Theme.wav")
mixer.music.set_volume(0)
#mixer.music.set_volume(0.75)
mixer.music.play(-1)

#a simple rectangle that tells the player what keys to press for certain options
def keyhint(x, y, text, box=True):
    #draw the hint
    text = font2.render(text, True, WHITE)
    height = 30
    width = text.get_width() + 10
    if box:
        py.draw.rect(DISPLAYSURF, GREY, (x - width/2, y-height/2, width, height), 0, 5)
    DISPLAYSURF.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

def title(title, box=False):
    text = font.render(title, True, WHITE)
    DISPLAYSURF.blit(text, (midWidth - text.get_width()/2, 100))

#main menu function
def menu():
    text = font.render("Franklin Battle Heroes", True, WHITE)
    DISPLAYSURF.blit(text, (midWidth - text.get_width()/2, 100))
    keyhint(midWidth, midHeight - 60, "Press SPACE to start")
    keyhint(midWidth, midHeight - 15, "Press 1 for credits")
    keyhint(midWidth, midHeight + 30, "Press ESC to quit")

def credits():
    title("Game Credits")
    keyhint(midWidth, midHeight - 60, "Press SPACE to return to menu")
    keyhint(midWidth, midHeight - 15, "Programming by Owen Schmidt and Brian Moore", False)
    keyhint(midWidth, midHeight + 30, "Game Idea by Jett Cherry", False)
    keyhint(midWidth, midHeight + 75, "Music and art by Brian Moore", False)

def charSelect():
    title("Select a Character")
    keyhint(midWidth, midHeight + 100, "Use LEFT ARROW and RIGHT ARROW to select a character")


def fight():
    mixer.music.stop()
    #mixer.music.load("Franklinite Battle Theme.mp3")
    #mixer.music.play()

#main code loop
while True:
    #check for events
    for event in py.event.get(): 
        #close when the window is closed
        if event.type == QUIT:
            py.quit()
            sys.exit()
        #get keypresses
        elif event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                if current_screen == "menu":
                    current_screen = "charSelect"
                elif current_screen == "credits":
                    current_screen = "menu"
                elif current_screen == "charSelect":
                    current_screen = "fight"
            if event.key == py.K_1:
                if current_screen == "menu":
                    current_screen = "credits"
            if event.key == py.K_ESCAPE:
                py.quit()
                sys.exit()
                
    
    #check which sceen we are on and display it
    if current_screen == "menu":
        menu()
    elif current_screen == "credits":
        credits()
    elif current_screen == "charSelect":
        charSelect()
    elif current_screen == "fight":
        fight()

    #update the display
    py.display.update()
    #set background color
    DISPLAYSURF.fill(BKGD)
    #maintain 60 fps
    clock.tick(60)
    
