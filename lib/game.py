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
    PILLARS_COUNT = 4
    PILLARS_DELTA_SPEED = 0.005
    SPAWN_POSITION_X = 300

    def __init__(self, window_height, window_width):
        pygame.init()
        self.window_height = window_height
        self.window_width = window_width
        self.display = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        self.pillars = PilarBuffer(self.display, self.window_width, self.window_height, self.PILLARS_COUNT)
        self.neural_network = []
        self.players = []
        self.__player_front_x = self.SPAWN_POSITION_X+Player.SIZE
        self.__next_pillar = self.pillars.get_first(self.__player_front_x)
        self.score = 0

    def animate(self):
        self.pillars.increase_speed(self.PILLARS_DELTA_SPEED)
        self.pillars.move()
        for p in self.players:
            p.animate()

    def jumpHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for p in self.players:
                    p.jump()

    def event_loop(self):
        for event in pygame.event.get():
            if len(self.neural_network) != 0:
                self.jumpHandler(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def status(self):
        os.system("cls")
        print(f"[ pilar_speed: {self.pillars.speed}, score: {self.score} ,buffer_size: {len(self.pillars.buffer)} ]")

    def __calculate_score(self):
        cur_next_pillar = self.pillars.get_first(self.__player_front_x)
        if cur_next_pillar != self.__next_pillar:
            for net, genome in self.neural_network:
                genome.fitness += 5
            self.__next_pillar = cur_next_pillar
            self.score += 1

    def isOver(self) -> bool:
        return len(self.players) == 0

    def add_player(self, neural_network=None):
        self.players.append(Player(self.display, self.SPAWN_POSITION_X, self.window_height / 2))
        if neural_network is not None:
            self.neural_network.append(neural_network)

    def remove_player(self, index):
        self.players.pop(index)
        if len(self.neural_network) != 0:
            self.neural_network.pop(index)

    def restart(self):
        self = self.__init__(self.window_height,self.window_width)

    def draw(self):
        # fill window with white
        self.display.fill(self.WHITE)

        # event loop
        self.event_loop()
        self.pillars.draw()
        for _index, _player in enumerate(self.players):
            _player.draw()
            if len(self.neural_network) != 0:
                # decide if jump or not
                self.neural_network[_index][1].fitness += 0.05
                outputs = self.neural_network[_index][0].activate(_player.inputs(self.__next_pillar))
                if outputs[0] > 0.5:
                    _player.jump()
            if _player.isCollided(self.__next_pillar):
                self.neural_network[_index][1].fitness -= 2
                self.remove_player(_index)
        self.animate()
        self.__calculate_score()
        pygame.display.update()
        # frame clock ticking
        self.clock.tick(self.FPS)
