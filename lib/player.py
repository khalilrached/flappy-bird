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

    def isCollided(self, _object):
        sky, ground, x_collide, y_top_collide, y_bottom_collide = False, False, False, False, False
        if _object.boundaries()["x-boundaries"][0] <= self.player_rect.x + self.player_rect.w <= \
                _object.boundaries()["x-boundaries"][1]:
            x_collide = True
        # upper pillar
        if 0 <= self.player_rect.y <= _object.boundaries()["y-boundaries"][0]:
            y_top_collide = True
        # lower pillar
        if _object.boundaries()["y-boundaries"][1] <= self.player_rect.y + self.player_rect.h <= self.display.get_height():
            y_bottom_collide = True
        # hit sky
        if self.player_rect.y <= 0:
            sky = True
        if self.player_rect.y + self.player_rect.h >= self.display.get_height():
            ground = True
        return x_collide and (y_bottom_collide or y_top_collide) or sky or ground

    def boundaries(self):
        return {
            "x-boundaries": [self.player_rect.x, self.player_rect.x + self.player_rect.w],
            "y-boundaries": [self.player_rect.y, self.player_rect.y + self.player_rect.h]
        }

    def animate(self):
        self.player_rect = self.gravity.apply()
