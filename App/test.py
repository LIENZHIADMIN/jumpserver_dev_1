# _*_ coding: utf-8 _*_

import pygame
import random
import sys

# 根据背景图大小,设置游戏屏幕大小
WIDTH, HEIGHT = 1024, 576
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('除了你被无所爱')

# 点击不答应按钮后显示的页面
def show_unlike_interface(screen):
    screen.fill((255, 255, 255))
    background_1 = pygame.image.load('./214_3.jpg').convert()
    screen.blit(background_1, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
# 修改之后
#