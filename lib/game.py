import os
import sys

import pygame

from lib import *
from lib import Player




def main():
    # initialize it
    pygame.init()
    # configurations
    frames_per_second = 60
    window_height = 720
    window_width = 1280

    # colors
    WHITE = (255, 255, 255)

    # creating window
    display = pygame.display.set_mode((window_width, window_height))
    # creating our frame regulator
    clock = pygame.time.Clock()
    buffer = pb(display, window_width, window_height, 6)

    player = Player(display, 300, window_height / 2)

    def animate():
        buffer.increase_speed(0.005)
        buffer.move()
        player.animate()

    jump = False

    def status():
        os.system("cls")
        print(f"[ jump: {jump}, pilar_speed: {buffer.speed} ]")

    # forever loop
    while True:
        # frame Drawing
        display.fill(WHITE)
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                    jump = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # frame clock ticking
        buffer.draw()
        player.draw()
        animate()
        status()
        jump = False
        pygame.display.update()
        clock.tick(frames_per_second)
