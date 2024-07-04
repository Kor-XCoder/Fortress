import pygame

# pygame의 sprite.Sprite 클래스 상속(Inheritance)
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, ty, color):
        super().__init__()
        # 아스키 코드
        self.image = pygame.image.load('assets/' + color + ' tiles/' + ty + '.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect(topleft=pos)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self, x_shift):
        self.rect.x += x_shift