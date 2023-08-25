"""
game 1. game window
"""

import pygame


# initialization
pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600
pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))


# quit
#
while True:
    cmd = input("Press q to quit")
    if cmd == 'q' or cmd == 'quit':
        pygame.quit()
        break



