import pygame
import sqlite3
import sys
import os
from azino777 import game777
from sea_battle import sea_battle_game
from konfig import *
from tic_tac_toe_for_kazino_main.main import tic_tac_toe
from blackjack.main import main


def get_name(name, evt):
    name1 = name
    if evt.type == pygame.KEYDOWN:
        if evt.unicode.isalpha():
            name1 += evt.unicode
        elif evt.key == pygame.K_BACKSPACE:
            name1 = name1[:-1]
        if evt.key == pygame.K_SPACE:
            name1 += ' '
    return name1


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


def end_game(name, result):
    global conn, cursor

    # вариант проигрыша
    if result < 0:
        cursor.execute("""
            UPDATE player
                SET lose = lose + 1
            WHERE name = '{}';
        """.format(name))
    else:  # вариант выигрыша
        cursor.execute("""
            UPDATE player
                SET win = win + 1
            WHERE name = '{}';
        """.format(name))

    # измняем общую статистику выигрыша/проигрыша
    cursor.execute("""
        UPDATE player
            SET list = list + ({})
        WHERE name = '{}';
    """.format(result, name))

    # отправляем измененные данные
    conn.commit()

    return main_menu()


def draw_games():
    fon_game_1 = pygame.transform.scale(load_image('fon1.png'), (200, 150))
    fon_game_2 = pygame.transform.scale(load_image('ship.jpg'), (240, 150))
    fon_game_3 = pygame.transform.scale(load_image('tic_tac_toe.png'), (220, 150))
    fon_game_5 = pygame.transform.scale(load_image('blackjack.png', -1), (240, 150))
    # ЗАгружаем фоны для всех игр
    pygame.draw.rect(screen, pygame.Color((255, 255, 255)), (80, 200, 240, 150))
    pygame.draw.rect(screen, pygame.Color((255, 255, 255)), (380, 200, 240, 150))
    pygame.draw.rect(screen, pygame.Color((255, 255, 255)), (680, 200, 240, 150))
    pygame.draw.rect(screen, pygame.Color((255, 255, 255)), (380, 500, 240, 150))
    screen.blit(fon_game_1, (100, 200))
    screen.blit(fon_game_2, (380, 200))
    screen.blit(fon_game_3, (690, 200))
    screen.blit(fon_game_5, (380, 500))


def puk_games(pos):
    global name
    t_x, t_y = pos

    player_data = cursor.execute("""
                SELECT * FROM player WHERE name = '{}';
            """.format(name)).fetchall()
    if t_x in range(100, 301) and t_y in range(200, 351):
        end_game(name, game777(player_data[0][2], player_data[0][3]))
    if t_x in range(400, 601) and t_y in range(200, 351):
        end_game(name, sea_battle_game(player_data[0][2], player_data[0][3]))
    if t_x in range(700, 901) and t_y in range(200, 351):
        end_game(name, tic_tac_toe(player_data[0][2], player_data[0][3]))
    if t_x in range(400, 601) and t_y in range(500, 651):
        end_game(name, main(player_data[0][2], player_data[0][3]))


def main_menu():
    global conn, cursor, name

    # накатываем миграции, если их нет
    cursor.execute \
        ("""CREATE TABLE IF NOT EXISTS player(
            id INT PRIMARY KEY,
            "name" TEXT,
            win INT,
            lose INT,
            list INT);
        """)
    conn.commit()
    entering_name = True
    name_been_entered = False
    focus = False
    rect_enter_name = pygame.Rect(500, 50, 1000, 80)
    font = pygame.font.Font(None, 70)
    text = font.render("Введите свое имя", True, pygame.Color((255, 0, 0)))
    name = ''
    main_fon = pygame.transform.scale(load_image('main_fon.jpg'), (width, height))
    text_name = pygame.font.Font(None, 60).render(name, True, pygame.Color((120, 230, 40)))
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                entering_name = False
            if entering_name and focus:
                name = get_name(name, event)
                text_name = pygame.font.Font(None, 60).render(name, True, pygame.Color((120, 230, 40)))
            if event.type == pygame.MOUSEBUTTONDOWN and name_been_entered:
                puk_games(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_enter_name.collidepoint(event.pos):
                    focus = True
                else:
                    focus = False
        if not entering_name and not name_been_entered:
            result = cursor.execute \
                ("""SELECT * FROM player 
                WHERE "name" = '{}';""".format(name)).fetchall()
            if len(result) == 0:
                user_registration(name)
            name_been_entered = True
        screen.blit(main_fon, (0, 0))
        draw_games()
        pygame.draw.rect(screen, pygame.Color((200, 50, 20)), rect_enter_name, 3)
        screen.blit(text_name, (510, 70))
        screen.blit(text, (40, 60))
        pygame.display.flip()
        clock.tick()


def user_registration(name):
    global conn, cursor

    # создаем пользователя
    cursor.execute("""
        INSERT INTO player("name", win, lose, list) VALUES ('{}', 0, 0, 0);
    """.format(name))

    conn.commit()

    return name


# запускаем игру
if __name__ == '__main__':
    main_menu()
