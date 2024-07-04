import pygame
import os

# Fortress-tank 경로
projectPath = os.getcwd().replace('\\', '/')


class Tank:
    def __init__(self, _screen):
        # image of tank
        image_path = projectPath + '/assets/Tank/tanks_tankNavy1.png'
        if not os.path.exists(image_path):
            print(f"Error: The image path {image_path} does not exist.")
        self.tankImage = pygame.image.load(image_path).convert_alpha()
        self.tankImage = pygame.transform.scale(self.tankImage, (76, 64))

        self.screen = _screen

    def forward(self):
        pass

    def backward(self):
        pass