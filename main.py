import sys
import pygame
import math
from map import Map
from settings import *

# Pygame Settings
pygame.init()
pygame.display.set_caption("Fortress")

# screen = 디스플레이
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# 게임이 끝났는지 여부
isGameOver: bool = False

# 디버깅용, 릴리즈 시 보이지 않음.
print(str(screenWidth) + 'x' + str(screenRealHeight))

# 맵 데이터는 map.py에 존재.
# Map 클래스는 'def __init__(self, lv_data, surface)'가 생성자, lv_data는 맵 2차원 배열 데이터, surface에는 screen을 넣어주면 됨.
fmap = Map(map1, screen)

# setup 메서드로 타일 위치 세팅
fmap.setup(map1)

# 프레임 유지(deltaTime)
clock = pygame.time.Clock()

def toDisplayCoord(v):
    return pygame.Vector2(v.x * 64, v.y * 64)

def main():
    global isGameOver
    while not isGameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameOver = True

        game()

    pygame.quit()
    sys.exit()

def game():
    global isGameOver, screen, fmap, clock

    # 배경 렌더링
    screen.fill((125, 229, 255))

    # 맵 렌더링
    fmap.run()

    # cr = pygame.Vector2(0, 7)
    # dcr = toDisplayCoord(cr)

    # Maracle = pygame.image.load('assets/Green tiles/?.png')
    # Maracle = pygame.transform.scale(Maracle, (96, 80))  #(96, 80)
    # screen.blit(Maracle, dcr)

    # 디스플레이 업데이트
    pygame.display.update()

    clock.tick(60)  # 60 FPS 기준

main()