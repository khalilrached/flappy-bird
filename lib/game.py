import os
import sys
import pygame
from lib import *


def check_collision():
    collided = False
    #   if player.boundaries()["x-boundaries"][1] > buffer.buffer[0].boundaries()["x-boundaries"][0]:
    #   collided = True


class Game:
    FPS = 60
    WHITE = (255, 255, 255)
    PILLARS_COUNT = 6
    PILLARS_DELTA_SPEED = 0.005
    SPAWN_POSITION_X = 300

    def __init__(self, window_height, window_width):
        pygame.init()
        self.window_height = window_height
        self.window_width = window_width
        self.display = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        self.pillars = PilarBuffer(self.display, self.window_width, self.window_height, self.PILLARS_COUNT)
        self.players = [Player(self.display, self.SPAWN_POSITION_X, self.window_height / 2)]
        self.__player_front_x = self.SPAWN_POSITION_X+self.players[0].player_rect.w
        self.__next_pillar = self.pillars.get_first(self.__player_front_x)
        self.score = 0

    def animate(self):
        self.pillars.increase_speed(self.PILLARS_DELTA_SPEED)
        self.pillars.move()
        for p in self.players:
            p.animate()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for p in self.players:
                        p.jump()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def status(self):
        os.system("cls")
        print(f"[ pilar_speed: {self.pillars.speed}, score: {self.score} ,buffer_size: {len(self.pillars.buffer)} ]")

    def __calculate_score(self):
        cur_next_pillar = self.pillars.get_first(self.__player_front_x)
        if cur_next_pillar != self.__next_pillar:
            self.__next_pillar = cur_next_pillar
            self.score += 1

    def draw(self):
        # fill window with white
        self.display.fill(self.WHITE)
        # event loop
        self.event_loop()
        self.pillars.draw()
        self.players[0].draw()
        self.animate()
        self.__calculate_score()
        self.status()
        pygame.display.update()
        # frame clock ticking
        # clock.tick(frames_per_second)
