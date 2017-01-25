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

DobekBackground = Background('dane/jaszczurbezoczu.png', [0, 0])

jaszczur = pygame.image.load('dane/jaszczur.png')
oceny = pygame.image.load('dane/oceny.png')

trygo = [pygame.mixer.Sound('dane/sinus.wav'),
         pygame.mixer.Sound('dane/cosinus.wav'),
         pygame.mixer.Sound('dane/tangens.wav'),
         pygame.mixer.Sound('dane/cotangens.wav')] 
blad = pygame.mixer.Sound('dane/blad.wav')
blads = pygame.mixer.Sound('dane/blads.wav')
violin = pygame.mixer.Sound('dane/sadviolin.wav')

class Zero:
    zer = 0

    def __init__(self):
        self.lx = random.randint(0, 800)
        self.ly = -100
        self.speed = random.randint(5 + Zero.zer//5, 20+Zero.zer//5)

        self.rozm = random.randint(60, 100)
        self.ocena = pygame.transform.scale(oceny, (self.rozm, self.rozm))

        Zero.zer += 1

    def rysuj(self):
        self.ly += self.speed
        if self.ly > 900:
            return True
        screen.blit(self.ocena, (self.lx, self.ly))

    def zestrzel(self, x, y):
        if x >= self.lx and x <= self.lx+self.rozm:
            if y >= self.ly and y <= self.ly+self.rozm:
               return True

    @staticmethod
    def zeruj():
        Zero.zer = 0


def boom(kolumna = False):
    v1 = 0
    v2 = 0
    g = 15
    krok = 0.2
    y1 = 340
    y2 = 370

    pygame.mixer.stop()
    blad.play()

    if kolumna:
        pygame.display.set_caption("Dobek Patrzy - BŁĄD KURWA UKRYTA KOLUMNA. Level: %d" % (Zero.zer//5,))
    else:
        pygame.display.set_caption("Dobek Patrzy - BŁĄD KURWA KONIEC STAMINY. Level: %d" % (Zero.zer//5,))

    screen.fill([0xff, 0, 0])
    screen.blit(jaszczur, (405, y1))
    screen.blit(jaszczur, (535, y2))
    screen.blit(DobekBackground.image, DobekBackground.rect)
    pygame.display.flip()

    while pygame.mixer.get_busy():
        pygame.time.wait(10)
    violin.play(-1)

    cz1 = 0
    cz2 = random.randint(0, 100)
    if random.choice([True, False]):
        cz1, cz2 = cz2, cz1

    while cz1 <= 100 or cz2 <= 100:
        if y1 < 870:
            if cz1 > 0:
                pygame.display.set_caption("Dobek Patrzy - ZAAWANSOWANA FIZYKA CZERWONYCH OCZU. Level: %d"
                        % (Zero.zer//5,))
                cz1 -= 1
            else:
                v1 -= g*krok
                y1 -= v1*krok
        else:
            v1 = -v1-7
            y1 -= v1*krok
            if v1 < 0:
                cz1 = 1000
        if y2 < 870:
            if cz2 > 0:
                cz2 -= 1
            else:
                v2 -= g*krok
                y2 -= v2*krok
        else:
            v2 = -v2-7
            y2 -= v2*krok
            if v2 < 0:
                cz2 = 1000

        screen.fill([0xff, 0, 0])
        screen.blit(DobekBackground.image, DobekBackground.rect)
        if cz1 == 1000:
            screen.blit(jaszczur, (405, 870))
        else:
            screen.blit(jaszczur, (405, y1))
        if cz2 == 1000:
            screen.blit(jaszczur, (535, 870))
        else:
            screen.blit(jaszczur, (535, y2))

        pygame.display.flip()

    pygame.time.wait(500)

def hehe(wyni):
    alive = True
    while alive:
        # Ograniczenie liczby klatek
        deltat = clock.tick(30)

        pygame.display.set_caption("Dobek Patrzy - level: %d, stamina: %d, średnia: %d" % \
                (Zero.zer//5, 73-oczy, wynik))

        # Wejście
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    lazors = True
                else:
                    return
            elif event.type == MOUSEBUTTONUP:
                lazors = False
            elif event.type == MOUSEMOTION:
                x, y = event.pos


def gra():
    x = 405
    y = 342
    lazors = False
    lx = random.randint(100,800)
    ly = -100
    zera = []
    oczy = 0
    moczy = 73
    wynik = 10

    Zero.zeruj()
    pygame.mixer.stop()

    alive = True
    while alive:
        # Ograniczenie liczby klatek
        deltat = clock.tick(30)

        pygame.display.set_caption("Dobek Patrzy - level: %d, stamina: %d, średnia: %d" % \
                (Zero.zer//5, 73-oczy, wynik))

        # Wejście
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    lazors = True
                else:
                    return
            elif event.type == MOUSEBUTTONUP:
                lazors = False
            elif event.type == MOUSEMOTION:
                x, y = event.pos

        x1 = 405
        y1 = 340
        xr = 40
        yr = 30

        lewo = (x-10)-x1
        dol = (y-10)-y1
        kat = math.atan2(dol, lewo)

        if oczy > 0:
            oczy -= 1
        kolory = [0xb7+oczy, 0xba-(oczy*2), 0xb3-(oczy*2)]
        for i, kolor in enumerate(kolory):
            if kolor < 0:
                kolory[i] = 0
            elif kolor > 0xff:
                kolory[i] = 0xff

        screen.fill(kolory)
        screen.blit(jaszczur, (x1+8*math.cos(kat),y1+4*math.sin(kat),xr,yr))
        z = x1+8*math.cos(kat)+10
        zz = 10+y1+4*math.sin(kat)

        x1 = 535
        y1 = 370
        xr = 40
        yr = 30

        lewo = (x-10)-x1
        dol = (y-10)-y1
        kat = math.atan2(dol, lewo)

        screen.blit(jaszczur, (x1+8*math.cos(kat),y1+4*math.sin(kat),xr,yr))
        screen.blit(DobekBackground.image, DobekBackground.rect)

        szansa = 30 - Zero.zer//5
        if szansa < 1:
            szansa = 1
        if random.randint(0, szansa) == 0:
            zera += [Zero()]
        for nr, zero in enumerate(zera):
            if zero.rysuj():
                del zera[nr]

                wynik -= 5
                if wynik < 0:
                    boom(True)
                    alive = False
                else:
                    blads.play()
            elif lazors and zero.zestrzel(x, y):
                del zera[nr]
                wynik += 1
                random.choice(trygo).play()

        if lazors:
            oczy += 2
            pygame.draw.line(screen, [0xff,0,0], [x1+8*math.cos(kat)+10,10+y1+4*math.sin(kat)], [x,y], 20)
            pygame.draw.line(screen, [0xff,0,0], [z,zz], [x,y], 20)

            if oczy > moczy:
                boom()
                alive = False

        pygame.display.flip()

def main():
    pygame.mixer.init(channels=6)

    while True:
        gra()

if __name__ == "__main__":
    main()
