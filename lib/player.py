import pygame
from lib.physics import *


class Player:
    __SIZE = 30
    __COLOR = (255, 0, 0)
    jump_force = -500

    def __init__(self, display, start_pos_x, start_pos_y):
        self.display = display
        self.player_rect = pygame.rect.Rect(start_pos_x, start_pos_y, self.__SIZE, self.__SIZE)
        self.gravity = GravityForce(1000, self.player_rect)

    def jump(self):
        self.gravity.add_force(self.jump_force)

    def draw(self):
        pygame.draw.rect(self.display, self.__COLOR, self.player_rect)

    def boundaries(self):
        return {
            "x-boundaries": [self.player_rect.x, self.player_rect.x + self.player_rect.w],
            "y-boundaries": [self.player_rect.y, self.player_rect.y + self.player_rect.h]
        }

    def animate(self):
        self.player_rect = self.gravity.apply()
