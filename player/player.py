from settings import settings
from settings.settings import *


def toDisplayCoord(v):
    return pygame.Vector2(v.x * settings.tileSize, v.y * settings.tileSize + 26)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, ty, pNum):
        super().__init__()

        # ty can be 'Green', 'Desert', 'Grey', 'Navy'
        self.image = pygame.image.load('assets/Tank/tanks_tank'+ty+'1.png')
        self.image = pygame.transform.scale(self.image, (76, 64))
        self.rect = self.image.get_rect(topleft=(toDisplayCoord(pos)))
        self.power = pygame.Vector2(0, 0)
        self.canMove: bool = True
        self.instantSpeed: int = 1
        self.maxSpeed: int = 8
        self.gravity: float = 0.8
        self.isDebugVisible: bool = False
        self.playerNum = pNum
        self.lr = False
        self.coord = pygame.Vector2(0, 0)


    def input(self):
        keys = pygame.key.get_pressed()
        lr = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.power.x < self.maxSpeed:
                self.power.x = 3
                lr = True
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.power.x > -self.maxSpeed:
                self.power.x = -3
                lr = True
        if not lr:
            self.power.x = 0

        

    def update(self):
        self.input()

