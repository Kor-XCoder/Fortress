import sys
import tanks.tank

from settings import settings
from settings.settings import *

# Pygame Settings
pygame.init()
pygame.display.set_caption("Fortress")

# screen = 디스플레이
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# 게임이 끝났는지 여부
isGameOver: bool = False

# 디버깅용, 릴리즈 시 보이지 않음.
print(str(screenWidth) + 'x' + str(screenRealHeight))

# 프레임 유지(deltaTime)
clock = pygame.time.Clock()

def toDisplayCoord(v):
    return pygame.Vector2(v.x * settings.tileSize, v.y * settings.tileSize)

def main():
    # 이미지 불러오기 테스트

    # print(tanks.tank.projectPath+'/assets/Tank/tanks_tankNavy1.png')  # 이미지 경로 출력


    global isGameOver
    while not isGameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameOver = True

        game()

    pygame.quit()
    sys.exit()

def game():
    global isGameOver, screen, clock

    # 배경 렌더링
    screen.fill((125, 229, 255))

    tempTank = tanks.tank.Tank(screen)
    screen.blit(tempTank.tankImage, (64, 64))

    # cr = pygame.Vector2(0, 7)
    # dcr = toDisplayCoord(cr)

    # Maracle = pygame.image.load('assets/Green tiles/?.png')
    # Maracle = pygame.transform.scale(Maracle, (96, 80))  #(96, 80)
    # screen.blit(Maracle, dcr)

    # 디스플레이 업데이트
    pygame.display.update()

    clock.tick(60)  # 60 FPS 기준

main()