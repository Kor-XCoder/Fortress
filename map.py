import pygame
from tiles import Tile
from settings import *
from player import Player

class Map:
    def __init__(self, lv_data, surface):
        # Level Setup
        self.tank2 = None
        self.tank1 = None

        self.p1 = None
        self.p2 = None

        self.tiles = None
        self.displaySurface = surface
        self.setup(lv_data)
        self.world_shift = 0
        self.map = None
        self.ending = False

    def setup(self, layout):
        self.tiles = pygame.sprite.Group()
        self.p1 = pygame.sprite.GroupSingle()
        self.p2 = pygame.sprite.GroupSingle()

        self.tank1 = Player(pygame.Vector2(1, 9), 'Green', 1)
        self.p1.add(self.tank1)

        plus = screenRealHeight - screenHeight

        for y, row in enumerate(layout):
            for x, cell in enumerate(row):
                if cell != ' ':
                    tile = Tile((x * tileSize, plus + y * tileSize), tileSize, cell, 'Green')
                    self.tiles.add(tile)


    # def scroll_x(self):
    #     player = self.player.sprite
    #     player_x = player.rect.centerx
    #     direction_x = player.power.x
    #
    #     limit = screenWidth / 4
    #
    #     if player_x < limit and direction_x < 0:
    #         self.world_shift = round(player.power.x)
    #         **DEPRECATED**# player.maxSpeed = 0
    #     elif player_x > screenWidth - limit and direction_x > 0:
    #         self.world_shift = round(player.power.x)
    #         # player.maxSpeed = 0
    #     else:
    #         self.world_shift = 0
    #         **DEPRECATED**# player.maxSpeed = 8

    def run(self):
        # self.scroll_x()
        self.tiles.update(-self.world_shift)
        self.tiles.draw(self.displaySurface)
        # self.displaySurface.blit(self.Maracle, (100, 575))

        # self.spikes.update(-self.world_shift)
        # self.spikes.draw(self.display_surface)
        #
        self.p1.update()
        #
        self.check_horizontal()
        # self.check_vertical()
        #
        # self.exits.update(-self.world_shift)
        # self.exits.draw(self.display_surface)
        self.p1.draw(self.displaySurface)


    def check_horizontal(self):
        player = self.p1.sprite

        if self.world_shift == 0:
            player.rect.x += player.power.x

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.power.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.power.x > 0:
                    player.rect.right = sprite.rect.left

        player.rect.x = max(player.rect.x, 0)
        player.rect.x = min(player.rect.x, screenWidth - player.rect.width)

    # def check_vertical(self):
    #     player = self.player.sprite
    #     player.apply_gravity()
    #
    #     for sprite in self.tiles.sprites():
    #         if sprite.rect.colliderect(player.rect):
    #             if player.power.y > 0:
    #                 player.rect.bottom = sprite.rect.top
    #                 player.power.y = 0
    #                 if player.isSpiking:
    #                     if abs(player.power.x) <= 1.5:
    #                         player.isJumping = False
    #                         player.canMove = True
    #                         player.isSpiking = False
    #                 else:
    #                     player.isJumping = False
    #                     player.canMove = True
    #             elif player.power.y < 0:
    #                 player.rect.top = sprite.rect.bottom
    #                 player.power.y = 0
    #
    #     for spike in self.spikes.sprites():
    #         if spike.rect.colliderect(player.rect):
    #             player.power.x = -spike.knockback.x
    #             player.power.y = -spike.knockback.y
    #             player.isJumping = True
    #             player.canMove = False
    #             player.isSpiking = True
    #     if player.isJumping or player.power.y > 0:
    #         player.power.y = min(player.power.y, 20)
    #
    #     if self.exits.sprite.rect.colliderect(player.rect):
    #         self.ending = True

    def checkDebug(self):
        return self.player.sprite.isDebugVisible