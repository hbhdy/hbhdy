import random
import game_framework

from pico2d import *


class Zombie:
    PIXEL_PER_METER = (10.0 / 0.1)           # 10 pixel 10 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    WALK, ATTACK, APPEAR, DIE = 3,2,1,0
    def __init__(self):
        self.x=1500
        self.frame=0
        self.start=0
        self.state=self.APPEAR
        self.die = load_image("resource\\enemy\\zombie\\die.png")
        self.walk = load_image("resource\\enemy\\zombie\\walk.png")
        self.attack = load_image("resource\\enemy\\zombie\\attack.png")
        self.appear = load_image("resource\\enemy\\zombie\\appear.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0

    def update(self,frame_time):
        distance = Zombie.RUN_SPEED_PPS * frame_time
        self.walk_frame += Zombie.FRAMES_PER_ACTION * Zombie.ACTION_PER_TIME * frame_time
        self.attack_frame += Zombie.FRAMES_PER_ACTION * Zombie.ACTION_PER_TIME * frame_time
        self.appear_frame += Zombie.FRAMES_PER_ACTION * Zombie.ACTION_PER_TIME * frame_time
        self.die_frame += Zombie.FRAMES_PER_ACTION * Zombie.ACTION_PER_TIME * frame_time

        if self.state==self.APPEAR:
            self.appear_frame=(self.appear_frame+1)%11
        if self.state==self.WALK:
            self.walk_frame =(self.walk_frame+1)%10
            self.x=(self.start*distance)
        if self.state==self.DIE:
            self.die_frame=(self.die_frame+1)%8
        if self.state==self.ATTACK:
            self.attack_frame=(self.attack_frame+1)%7

        if self.state==self.APPEAR:
            self.start=0
            self.state=self.WALK
        if self.state==self.WALK:
            self.start=1







    def draw_die(self):
        self.die.clip_draw(self.die_frame *325, 0, 325, 214,self.x, 500)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *140, 0, 140, 218, self.x,170)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *251, 0, 251, 219, self.x, 700)
    def draw_appear(self):
        self.appear.clip_draw(self.appear_frame *163, 0, 163, 214, self.x, 100)


class Vampire:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    WALK, ATTACK, APPEAR, DIE = 3,2,1,0
    now_state = "Appear"
    init_Start = 0

    def __init__(self):
        self.x=1400
        # self.state=self.APPEAR
        self.now_state = "Appear"

        self.die=load_image("resource\\enemy\\vampire\\die.png")
        self.walk=load_image("resource\\enemy\\vampire\\walk.png")
        self.attack=load_image("resource\\enemy\\vampire\\attack.png")
        self.appear=load_image("resource\\enemy\\vampire\\appear.png")

        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0
        self.init_Start = 0


    def Send_State(self):
        return self.now_state
        pass


    def update(self,frame_time):
        distance = Vampire.RUN_SPEED_PPS * frame_time
        self.total_frames += Vampire.FRAMES_PER_ACTION * Vampire.ACTION_PER_TIME * frame_time

        if self.now_state == "Appear":
            self.appear_frame = int(self.total_frames)%8
            if ( self.appear_frame == 7  and self.init_Start >= 2):
                self.now_state = "Walk"
            else:
                self.init_Start += 1

        if self.now_state == "Walk":
            self.walk_frame = int(self.total_frames)%5
            self.x-=distance
        #
        # self.die_frame=(self.die_frame+1)%8
        # self.attack_frame=(self.attack_frame+1)%9

    def draw_die(self):
        self.die.clip_draw(self.die_frame *192 , 0, 192, 220, self.x, 500)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *120 , 0, 120, 215, self.x, 170)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *290 , 0, 290, 218, self.x, 700)
    def draw_appear(self):
        self.appear.clip_draw(self.appear_frame *191 , 0, 191, 219, self.x, 170)

class Skeleton:
    def __init__(self):
        self.x=1400
        self.now_state="Appear"
        self.die=load_image("resource\\enemy\\skeleton\\die.png")
        self.walk=load_image("resource\\enemy\\skeleton\\walk.png")
        self.attack=load_image("resource\\enemy\\skeleton\\attack.png")
        self.appear=load_image("resource\\enemy\\skeleton\\appear.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0
        self.init_Start = 0

    def update(self):
        self.die_frame=(self.die_frame+1)%8
        self.walk_frame = (self.walk_frame+1)%8
        self.x-=10
        self.attack_frame=(self.attack_frame+1)%8
        self.appear_frame=(self.appear_frame+1)%10

    def draw_die(self):
        self.die.clip_draw(self.die_frame *275 , 0,275, 220, self.x, 500)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *135 , 0, 135, 219, self.x, 170)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *185 , 0, 185, 217, self.x, 700)
    def draw_appear(self):
        self.appear.clip_draw(self.appear_frame *172 , 0, 172, 220, self.x, 300)

class Golem:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 10 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    WALK, ATTACK, APPEAR, DIE = 3,2,1,0
    now_state = "Appear"
    init_Start = 0

    def __init__(self):
        self.x=1400
        self.start=1
        self.state=self.WALK
        self.die=load_image("resource\\enemy\\golem\\die.png")
        self.walk=load_image("resource\\enemy\\golem\\walk.png")
        self.attack=load_image("resource\\enemy\\golem\\attack.png")
        self.appear=load_image("resource\\enemy\\golem\\appear.png")
        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0

    def Send_State(self):
        return self.now_state


    def update(self,frame_time):
        distance = Golem.RUN_SPEED_PPS * frame_time
        self.total_frames += Golem.FRAMES_PER_ACTION * Golem.ACTION_PER_TIME * frame_time

        if self.now_state == "Appear":
            self.appear_frame = int(self.total_frames)%8
            if ( self.appear_frame == 7  and self.init_Start >= 2):
                self.now_state = "Walk"
            else:
                self.init_Start += 1

        if self.now_state == "Walk":
            self.walk_frame = int(self.total_frames)%6
            self.x-=distance

        # self.die_frame=int(self.die_frame)%6
        # self.attack_frame=int(self.attack_frame)%6


    def draw_die(self):
        self.die.clip_draw(int(self.die_frame) *300 , 0,300, 331, self.x, 190)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *320 , 0, 320, 245, self.x, 190)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *350 , 0, 350, 247, self.x, 190)
    def draw_appear(self):
        self.appear.clip_draw(self.appear_frame *322 , 0, 332, 246, self.x, 190)


