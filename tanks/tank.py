import pygame
import os

# Fortress-tank 경로
projectPath = os.getcwd().replace('\\', '/')


class Tank:
    def __init__(self, _screen):
        # image of tank
        self.tankImage = pygame.image.load(projectPath+'/assets/Tank/tanks_tankNavy1.png').convert_alpha()
        self.tankImage = pygame.transform.scale(self.tankImage, (76, 64))

        self.screen = _screen

    def forward(self):
        pass

    def backward(self):
        pass
