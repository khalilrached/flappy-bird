from random import random
import pygame

class Pilar:
    def __init__(self, screen_width, screen_height,x):
        # the distance between the upper pilar and the lower pilar
        # should be between 15%~30% of screen_height
        # gap center should be
        gap_height_percent = 0.25 + random() * 0.10
        gap_width_percent = 0.05
        self.gap_width = gap_width_percent * screen_width
        self.gap_height = gap_height_percent * screen_height
        self.gap_y_center = screen_height * 0.2 + self.gap_height * 0.5 + random() * (
                screen_height - screen_height * (0.4 + gap_height_percent*0.5))
        self.upper_pilar_height = self.gap_y_center - self.gap_height*0.5
        self.lower_pilar_height = screen_height - (self.gap_y_center + self.gap_height*0.5)
        self.upper_rect = pygame.Rect(x,0,self.gap_width,self.upper_pilar_height)
        self.lower_rect = pygame.Rect(x,screen_height-self.lower_pilar_height,self.gap_width,self.lower_pilar_height)

    def is_out_of_range(self):
        temp_test_upper = self.upper_rect.x <= - self.gap_width
        temp_test_lower = self.lower_rect.x <= - self.gap_width
        return temp_test_lower and temp_test_upper
