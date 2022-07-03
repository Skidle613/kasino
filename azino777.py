import pygame
import sys
import os
import ctypes
import random

pygame.init()
width, height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
screen = pygame.display.set_mode((width, height))


def load_image(name, color_key=None):
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)

    else:
        image = image.convert_alpha()
    return image


def spin(stavka, win, s, roulette, end):
    if (stavka == 1 and win) or (stavka == 2 and not win):
        need = 600
    if (stavka == 2 and win) or (stavka == 1 and not win):
        need = 610
    if s >= 60 and s <= need and s % 10 == 0:
        roulette = pygame.transform.rotate(roulette, 90)
    s += 1
    if s >= need:
        s = 0
        end = True
    return s, roulette, end


def game777(win, lose):
    chance = [1] * (lose + 1) + [0] * (win + 1)
    result = 0
    roulette = pygame.transform.scale(load_image('roulette3.png', -1), (850, 850))
    fon = pygame.transform.scale(load_image('casino.jpg'), (width, height))
    font = pygame.font.Font(None, 60)
    text = font.render('Выберите на что ставить', True, pygame.Color((100, 200, 200)))
    rect_white = pygame.Rect((1020, 200, 350, 150))
    rect_black = pygame.Rect((1020, 500, 350, 150))
    running = True
    rolled = False
    end = False
    win = random.choice(chance)
    clock = pygame.time.Clock()
    stavka = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_white.collidepoint(event.pos) and not stavka:
                    stavka = 1
                if rect_black.collidepoint(event.pos) and not stavka:
                    stavka = 2
        if stavka and not rolled:
            s = 0
            rolled = True
        if stavka and rolled and not end:
            s, roulette, end = spin(stavka, win, s, roulette, end)
        screen.blit(fon, (0, 0))
        screen.blit(roulette, (50, 0))
        screen.blit(text, (900, 50))
        pygame.draw.rect(screen, pygame.Color((255, 255, 255)), rect_white, 0)
        pygame.draw.rect(screen, pygame.Color((0, 0, 0)), rect_black, 0)
        pygame.draw.polygon(screen, pygame.Color((255, 0, 0)), [(730, 750), (790, 785), (750, 815)], 0)
        if end:
            s += 1
            if end and s >= 120:
                if win:
                    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (450, 350, 500, 150))
                    text_win = font.render('Вы выиграли', True, pygame.Color(0, 0, 0))
                    screen.blit(text_win, (530, 400))
                else:
                    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (450, 350, 500, 150))
                    text_lose = font.render('Вы проиграли', True, pygame.Color(0, 0, 0))
                    screen.blit(text_lose, (530, 400))
                if s >= 360:
                    if win:
                        return 1
                    else:
                        return 0
        clock.tick(60)
        pygame.display.flip()
    return result

