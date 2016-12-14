#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import math

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

DobekBackground = Background('jaszczurbezoczu.png', [0, 0])
jaszczur = pygame.image.load('jaszczur.png')

def main():
    pygame.display.set_caption("Sub Zero")

    print(pygame.display.get_wm_info())

    x = 405
    y = 342
    while True:
        # Ograniczenie liczby klatek
        deltat = clock.tick(30)

        # Wejście
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if not event.button == 1:
                    continue
                return
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                #print(event.pos)

        #data = display.Display().screen().root.query_pointer()._data
        #print(data["root_x"], data["root_y"])
        print( pygame.mouse.get_pos())

        x1 = 405
        y1 = 340
        xr = 40
        yr = 30

        lewo = (x-10)-x1
        dol = (y-10)-y1
        kat = math.atan2(dol, lewo)
        deg = kat * (180/math.pi)
        obrot = jaszczur

        screen.fill([0xc7, 0xca, 0xc3])
        screen.blit(obrot, (x1+8*math.cos(kat),y1+4*math.sin(kat),xr,yr))

        x1 = 535
        y1 = 370
        xr = 40
        yr = 30

        lewo = (x-10)-x1
        dol = (y-10)-y1
        kat = math.atan2(dol, lewo)
        deg = kat * (180/math.pi)
        obrot = jaszczur

        screen.blit(obrot, (x1+8*math.cos(kat),y1+4*math.sin(kat),xr,yr))
        screen.blit(DobekBackground.image, DobekBackground.rect)


        pygame.display.flip()

if __name__ == "__main__":
    main()
