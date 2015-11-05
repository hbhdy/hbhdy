import random
import json
import os
os.chdir('C:\\Temp\\2DGP\\hbhdy')

from enemy import *
from team import *

from pico2d import *

import game_framework
import start_state

name = "MainState"

background=None

class Background:
    def __init__(self):
        self.image=load_image('background.png')
        pass#
    def draw(self):
        self.image.draw_to_origin(0,0,1600,800)
        pass





def enter():
    global background
    global zombie,vampire,skeleton,golem
    global ch1,ch2,ch3,ch4
    global characterUI
    global character_create


    character_create=[]
    background = Background()
    zombie = Zombie()
    vampire = Vampire()
    skeleton=Skeleton()
    golem=Golem()
    ch1=Ch1()
    ch2=Ch2()
    ch3=Ch3()
    ch4=Ch4()

    characterUI=load_image('UI\\characterUI.png')


def exit():
    global background,characterUI,ch1,ch2,ch3,ch4
    del(characterUI)
    del(background)
    del(ch1)
    del(ch2)
    del(ch3)
    del(ch4)
    pass

def pause():
    pass


def resume():
    pass

def mouse_click():
    global ch1,ch2,ch3,ch4
    if 20<mouse_x<120 and 20<mouse_y<120:
        ch1=Ch1()
        if len(character_create)<50:
            character_create.append(ch1)


    if 130<mouse_x<230 and 20 <mouse_y<120:
        ch4=Ch4()
        if len(character_create)<50:
            character_create.append(ch4)


    if 260<mouse_x<360 and 20<mouse_y<120:
        ch2=Ch2()
        if len(character_create)<50:
            character_create.append(ch2)


    if 370<mouse_x<470 and 20<mouse_y<120:
        ch3=Ch3()
        if len(character_create)<50:
            character_create.append(ch3)



def handle_events():
    global mouse_x,mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(start_state)
        elif event.type == SDL_MOUSEMOTION:
            mouse_x,mouse_y = event.x,event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
             mouse_click()



def update():
    zombie.update()
    vampire.update()
    skeleton.update()
    golem.update()
    ch1.update()
    ch2.update()
    ch3.update()
    ch4.update()
    pass


def draw():

    clear_canvas()
    background.draw()
    zombie.draw()
    vampire.draw()
    skeleton.draw()
    golem.draw()
    for ch1 in character_create:
        ch1.update()
        ch1.draw()
    for ch2 in character_create:
        ch2.update()
        ch2.draw()
    for ch3 in character_create:
        ch3.update()
        ch3.draw()
    for ch4 in character_create:
        ch4.update()
        ch4.draw()
    characterUI.draw(250,735)

    update_canvas()
    delay(0.08)
    pass



