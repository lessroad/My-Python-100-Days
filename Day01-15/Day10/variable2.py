"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :

Date    : 2019-08-20 10:04:47
Author  : Younth Yang (8593009@qq.com)
"""

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    pygame.display.set_caption('大球吃小球')

    screen.fill((242, 242, 242))

    ball_image = pygame.image.load('./vh.jpg')

    screen.blit(ball_image, (50, 50))

    x, y = 50, 50

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((242, 242, 242))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        pygame.time.delay(50)
        x, y = x + 5, y + 5

if __name__ == '__main__':
    main()
