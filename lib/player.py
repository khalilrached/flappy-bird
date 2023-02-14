import pygame
from lib.physics import *


class Player:
    __SIZE = 30
    __COLOR = (255, 0, 0)
    jump_force = -1000

    def __init__(self, display, start_pos_x, start_pos_y):
        self.display = display
        self.player_rect = pygame.rect.Rect(start_pos_x, start_pos_y, self.__SIZE, self.__SIZE)
        self.gravity = GravityForce(120, self.player_rect)

    def jump(self):
        self.gravity.add_force(self.jump_force)

    def draw(self):
        pygame.draw.rect(self.display, self.__COLOR, self.player_rect)

    def animate(self):
        self.player_rect = self.gravity.apply()
