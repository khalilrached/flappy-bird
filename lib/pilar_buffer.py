from lib.pilar import Pilar
import pygame

class PilarBuffer:

    __COLOR = (0, 0, 255)
    __INIT_SPEED = 3
    __MAX_SPEED = 10
    def __init__(self,display,screen_width,screen_height,pilar_per_display):
        self.speed = self.__INIT_SPEED
        self.display = display
        self.screen_width = screen_width
        self.screen_height = screen_height
        if pilar_per_display in range(2,10):
            self.pilar_per_display = pilar_per_display
            self.__space_between = ((1-pilar_per_display*0.05)/(pilar_per_display-2))*screen_width
        else:
            raise Exception("pilar_per_display should be in range of (2,7).")
        self.buffer = []
        for i in range(0,self.pilar_per_display):
            self.buffer.append(Pilar(screen_width,screen_height,screen_width*0.5+i*self.__space_between))

    def draw(self):
        for pilar in self.buffer:
            pygame.draw.rect(self.display, self.__COLOR, pilar.upper_rect)
            pygame.draw.rect(self.display, self.__COLOR, pilar.lower_rect)

    def rect_list(self):
        list = []
        for pilars in self.buffer:
            list.append(pilars.lower_rect)
            list.append(pilars.upper_rect)
        return list

    def increase_speed(self,delta_v):
        if self.speed < self.__MAX_SPEED:
            self.speed += delta_v

    def move(self):
        for pilar in self.buffer:
            pilar.upper_rect = pilar.upper_rect.move(-self.speed, 0)
            pilar.lower_rect = pilar.lower_rect.move(-self.speed, 0)
            if pilar.is_out_of_range():
                self.buffer.remove(pilar)
                self.buffer.append(Pilar(self.screen_width,self.screen_height,self.pilar_per_display*self.__space_between))