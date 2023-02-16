from lib.pilar import Pilar
from threading import Thread
import pygame

class PilarBuffer:

    __COLOR = (0, 0, 255)
    __INIT_SPEED = 1
    __MAX_SPEED = 2
    def __init__(self,display,screen_width,screen_height,pilar_per_display):
        self.speed = self.__INIT_SPEED
        self.display = display
        self.screen_width = screen_width
        self.screen_height = screen_height
        if pilar_per_display in range(2,10):
            self.pilar_per_display = pilar_per_display
            self.space_between = ((1-pilar_per_display*0.05)/(pilar_per_display-2))*screen_width
        else:
            raise Exception("pilar_per_display should be in range of (2,7).")
        self.buffer = []
        for i in range(0,self.pilar_per_display):
            self.buffer.append(Pilar(screen_width,screen_height,screen_width*0.5+i*self.space_between))

    def draw(self):
        for pilar in self.buffer:
            pygame.draw.rect(self.display, pilar.color, pilar.upper_rect)
            pygame.draw.rect(self.display, pilar.color, pilar.lower_rect)

    def rect_list(self):
        list = []
        for pilars in self.buffer:
            list.append(pilars.lower_rect)
            list.append(pilars.upper_rect)
        return list

    def increase_speed(self,delta_v):
        if self.speed < self.__MAX_SPEED:
            self.speed += delta_v

    def remove(self,pilar):
        self.buffer.remove(pilar)
        self.buffer.append(Pilar(self.screen_width, self.screen_height,
                                        self.pilar_per_display * self.space_between))

    def get_first(self,x_pos):
        for pilar in self.buffer:
            if pilar.lower_rect.x + pilar.lower_rect.w > x_pos:
                return pilar

    def move(self):
        for pilar in self.buffer:
            pilar.upper_rect = pilar.upper_rect.move(-self.speed, 0)
            pilar.lower_rect = pilar.lower_rect.move(-self.speed, 0)
            if pilar.is_out_of_range():
                x = Thread(target=self.remove,args=(pilar,)).start()
