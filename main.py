import sys
import time

import pygame

from lib import *

# initialize it
pygame.init()

# configurations
frames_per_second = 60
window_height = 720
window_width = 1280

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# creating window
display = pygame.display.set_mode((window_width, window_height))
rect = pygame.Rect(0, 0, 100, 100)
circle_center = (100, 100)
circle_radius = 50
# creating our frame regulator
clock = pygame.time.Clock()
buffer = pb(display, window_width, window_height, 4)
pause = True

player = Player(display, 300, window_height/2)


def animate():
    buffer.increase_speed(0.005)
    buffer.move()
    player.animate()

pause = False
# forever loop
while True:
    # frame Drawing
    display.fill(WHITE)
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause = not pause
                if not pause:
                    player.gravity.start = time.time()
            if event.key == pygame.K_SPACE:
                player.jump()
                print("jump")
            if event.key == pygame.K_UP:
                circle_center = (circle_center[0] + 10, circle_center[1] + 10)
                print("up pressed")
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # frame clock ticking
    clock.tick(frames_per_second)
    buffer.draw()
    player.draw()
    if not pause:
        animate()
    pygame.display.update()
