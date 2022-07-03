import pygame
import sys
import os
from random import randint
from konfig import *

pygame.init()


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


def draw_field(x, y, width, height, enemy):
    if not enemy:
        for i in range(10):
            for j in range(10):
                pygame.draw.rect(screen, pygame.Color((0, 0, 0)),
                                 pygame.Rect(x + width * i, y + height * j, width, height),
                                 2)
                pygame.draw.rect(screen, pygame.Color((255, 255, 255)),
                                 pygame.Rect(x + width * i + 2, y + height * j + 2, width - 4, height - 4),
                                 0)
                if myfield[i][j] == 3:
                    pygame.draw.rect(screen, pygame.Color((0, 0, 0)),
                                     pygame.Rect(x + width // 4 + width * i, y + height // 4 + height * j, width // 2,
                                                 height // 2), 2)
                elif myfield[i][j] == 2:
                    pygame.draw.line(screen, pygame.Color((0, 0, 0)),
                                     (x + width * i, y + height * j), (x + width * (i + 1), y + height * (j + 1)), 2)
                    pygame.draw.line(screen, pygame.Color((0, 0, 0)),
                                     (x + width * (i + 1), y + height * j), (x + width * i, y + height * (j + 1)), 2)
                elif myfield[i][j] == 1:
                    pygame.draw.circle(screen, pygame.Color((0, 0, 0)),
                                       (x + width // 2 + width * i, y + height // 2 + height * j), height // 4, 0)
                elif myfield[i][j] == 4:
                    pygame.draw.line(screen, pygame.Color((255, 0, 0)),
                                     (x + width * (i + 0.25), y + height * (j + 0.25)),
                                     (x + width * (i + 0.75), y + height * (j + 0.75)), 2)
                    pygame.draw.line(screen, pygame.Color((255, 0, 0)),
                                     (x + width * (i + 0.75), y + height * (j + 0.25)),
                                     (x + width * (i + 0.25), y + height * (j + 0.75)), 2)
    else:
        for i in range(10):
            for j in range(10):
                pygame.draw.rect(screen, pygame.Color((0, 0, 0)),
                                 pygame.Rect(x + width * i, y + height * j, width, height),
                                 2)
                pygame.draw.rect(screen, pygame.Color((255, 255, 255)),
                                 pygame.Rect(x + width * i + 2, y + height * j + 2, width - 4, height - 4),
                                 0)
                if botfield[i][j] == 3:
                    pygame.draw.rect(screen, pygame.Color((0, 0, 0)),
                                     pygame.Rect(x + width // 4 + width * i, y + height // 4 + height * j, width // 2,
                                                 height // 2), 2)
                if botfield[i][j] == 2:
                    pygame.draw.line(screen, pygame.Color((0, 0, 0)),
                                     (x + width * i, y + height * j), (x + width * (i + 1), y + height * (j + 1)), 2)
                    pygame.draw.line(screen, pygame.Color((0, 0, 0)),
                                     (x + width * (i + 1), y + height * j), (x + width * i, y + height * (j + 1)), 2)


def end_game():
    for i in range(10):
        for j in range(10):
            myfield[i][j] = 0
            botfield[i][j] = 0
    font2 = pygame.font.Font(None, 70)
    text2 = font2.render('Играть снова', True, pygame.Color((0, 0, 0)))
    text3 = font2.render('Выйти в меню', True, pygame.Color((0, 0, 0)))
    font = pygame.font.Font(None, 90)
    fon = pygame.transform.scale(load_image('ship.jpg'), (width, height))
    if myships == 0:
        text = font.render('Вы проиграли', True, pygame.Color((0, 0, 0)))
    else:
        text = font.render('Вы выиграли!', True, pygame.Color((0, 0, 0)))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                t_x, t_y = event.pos
                if t_x in range(200, 651) and t_y in range(700, 801):
                    flag = False
                    running = False
                if t_x in range(850, 1301) and t_y in range(700, 801):
                    flag = True
                    running = False
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, pygame.Color((237, 135, 44)), (200, 700, 450, 100), 0)
        pygame.draw.rect(screen, pygame.Color((237, 135, 44)), (850, 700, 450, 100), 0)
        screen.blit(text2, (270, 725))
        screen.blit(text3, (900, 725))
        screen.blit(text, (700, 100))
        clock.tick(60)
        pygame.display.flip()
    if myships == 0:
        result = -1
    else:
        result = 1
    return flag, result


def put_ships():
    global botships, myships
    counter = 0
    while True:
        k1, k2 = randint(0, 9), randint(0, 9)
        flag = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if k1 + i >= 0 and k2 + j >= 0:
                        if botfield[k1 + i][k2 + j] == 1:
                            flag = False
                            break
                except IndexError:
                    pass
            if not flag:
                break
        if flag:
            botfield[k1][k2] = 1
            counter += 1
        if counter == 10:
            break
    botships = 10
    text = pygame.font.Font(None, 76).render('Выберите куда хотите поставить корабли', True,
                                             pygame.Color((237, 135, 44)))
    fon = pygame.transform.scale(load_image('ship.jpg'), (width, height))
    clock = pygame.time.Clock()
    zapoln = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                t_x, t_y = event.pos
                if t_x in range(450, 450 + 60 * 10) and t_y in range(200, 200 + 60 * 10):
                    t_i, t_j = (t_x - 450) // 60, (t_y - 200) // 60
                    if myfield[t_i][t_j] != 1 and myfield[t_i][t_j] != 4:
                        myfield[t_i][t_j] = 1
                        zapoln += 1
                        for sdi in range(-1, 2):
                            for sdj in range(-1, 2):
                                if not sdi and not sdj:
                                    continue
                                try:
                                    if t_i + sdi >= 0 and t_j + sdj >= 0:
                                        myfield[t_i + sdi][t_j + sdj] = 4
                                except IndexError:
                                    pass

        if zapoln >= 10:
            myships = 10
            running = False
            for i in range(10):
                for j in range(10):
                    if myfield[i][j] == 4:
                        myfield[i][j] = 0
        screen.blit(fon, (0, 0))
        screen.blit(text, (240, 50))
        draw_field(450, 200, 60, 60, False)
        clock.tick(60)
        pygame.display.flip()
    return


def game():
    global botships, myships
    font = pygame.font.Font(None, 70)
    text1 = font.render("Твое поле", True, pygame.Color((0, 255, 0)))
    text2 = font.render("Поле противника", True, pygame.Color((0, 255, 0)))
    text3 = font.render("Твой ход", True, pygame.Color((0, 255, 0)))
    text4 = font.render("Ход противника", True, pygame.Color((0, 255, 0)))
    text5 = pygame.font.Font(None, 35).render('Кораблей:' + str(botships), True, pygame.Color((0, 0, 0)))
    fon = pygame.transform.scale(load_image('sea2.jpg'), (width, height))
    clock = pygame.time.Clock()
    hod = 1
    sec = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hod:
                    t_x, t_y = event.pos
                    if t_x in range(900, 900 + 50 * 10) and t_y in range(200, 200 + 50 * 10):
                        t_i, t_j = (t_x - 900) // 50, (t_y - 200) // 50
                        if botfield[t_i][t_j] != 2 and botfield[t_i][t_j] != 3:
                            if botfield[t_i][t_j] == 0:
                                botfield[t_i][t_j] = 3
                                hod = 0
                            elif botfield[t_i][t_j] == 1:
                                botfield[t_i][t_j] = 2
                                botships -= 1
                                text5 = pygame.font.Font(None, 30).render('Кораблей:' + str(botships), True,
                                                                          pygame.Color((0, 0, 0)))
                                if botships == 0:
                                    running = False
                                for i in range(-1, 2):
                                    for j in range(-1, 2):
                                        if i + t_i >= 0 and j + t_j >= 0 and (i != 0 or j != 0):
                                            try:
                                                botfield[i + t_i][j + t_j] = 3
                                            except IndexError:
                                                pass
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, pygame.Color((0, 0, 0)), (150, 70, 400, 80), 0)
        pygame.draw.rect(screen, pygame.Color((0, 0, 0)), (905, 70, 490, 80), 0)
        screen.blit(text1, (220, 90))
        screen.blit(text2, (955, 90))
        draw_field(100, 200, 50, 50, False)
        draw_field(900, 200, 50, 50, True)
        screen.blit(text5, (1260, 720))
        if hod:
            pygame.draw.rect(screen, pygame.Color((0, 0, 0)), (610, 730, 260, 80), 0)
            screen.blit(text3, (630, 750))
        else:
            sec += 1
            pygame.draw.rect(screen, pygame.Color((0, 0, 0)), (550, 730, 410, 80), 0)
            screen.blit(text4, (560, 750))
        if sec >= 120:
            i, j = randint(0, 9), randint(0, 9)
            while myfield[i][j] == 2 or myfield[i][j] == 3:
                i, j = randint(0, 9), randint(0, 9)
            if myfield[i][j] == 0:
                myfield[i][j] = 3
                hod = 1
            elif myfield[i][j] == 1:
                myfield[i][j] = 2
                myships -= 1
                if myships == 0:
                    running = False
                for t_i in range(-1, 2):
                    for t_j in range(-1, 2):
                        if i + t_i >= 0 and j + t_j >= 0 and (t_i != 0 or t_j != 0):
                            try:
                                myfield[i + t_i][j + t_j] = 3
                            except IndexError:
                                pass
            sec = 0
        clock.tick(60)
        pygame.display.flip()


def sea_battle_game(win, lose):
    result = 0
    while True:
        put_ships()
        game()
        flag, t_result = end_game()
        result += t_result
        if flag:
            return result

