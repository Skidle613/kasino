import pygame
import time
import random
from pygame.locals import *
from .utils import *
from .buttons import *
from .ai import *


class Board:
    scores = {'X': 0, '0': 0, 'tie': 0}
    player = 'X'

    def __init__(self):
        self.font = pygame.font.SysFont("comicsansms", 20)
        pygame.display.set_caption("Tic Tac Toe")

    def reset(self):
        w = .6 * game_w
        h = .6 * game_h
        self.board = pygame.Surface((w, h))
        ## vertical
        pygame.draw.line(self.board, white, [w / 3, 0], [w / 3, h], 5)
        pygame.draw.line(self.board, white, [2 * w / 3, 0], [2 * w / 3, h], 5)
        ## horizontal
        pygame.draw.line(self.board, white, [0, h / 3], [w, h / 3], 5)
        pygame.draw.line(self.board, white, [0, 2 * h / 3], [w, 2 * h / 3], 5)
        self.grid = [[None, None, None], [None, None, None], [None, None, None]]
        self.text = self.font.render(
            "Player X: %d    Player O: %d    Ties: %d" % (self.scores['X'], self.scores['0'], self.scores['tie']), True,
            white)
        self.player = 'X'
        self.remaining = 9

    def show(self):
        screen.fill((0, 0, 0))
        screen.blit(self.board, (.2 * game_w, .2 * game_h))
        screen.blit(self.text, (.01 * game_w, 0))
        pygame.display.flip()

    def check(self):

        (row, col) = pygame.mouse.get_pos()
        (row, col) = make_relative(row, col)

        if row < 0 or row > 2 or col < 0 or col > 2:
            return

        if self.grid[row][col] == None:
            self.make_move(row, col)

    def make_move(self, row, col):
        centerX, centerY = int(.1 * game_w + row * (.2 * game_w)), int(.1 * game_h + col * (.2 * game_h))
        if self.player == 'X':
            pygame.draw.line(self.board, yellow, [centerX - .05 * game_w, centerY - .05 * game_h],
                             [centerX + .05 * game_w, centerY + .05 * game_h], 3)
            pygame.draw.line(self.board, yellow, [centerX + .05 * game_w, centerY - .05 * game_h],
                             [centerX - .05 * game_w, centerY + .05 * game_h], 3)
        else:
            pygame.draw.circle(self.board, blue, [centerX, centerY], int(.05 * game_w), 3)
        sound.play()
        self.grid[row][col] = self.player
        self.remaining -= 1

        last_player = self.player
        self.player = 'X' if self.player == '0' else '0'
        self.check_win(last_player)

    def has_won(self, whom):
        self.show()
        time.sleep(2)
        self.scores[whom] += 1
        self.reset()

    def check_win(self, player):
        if self.remaining == 0:
            return self.has_won('tie')

        if wins(self.grid, player):
            return self.has_won(player)


def tic_tac_toe(wins, loses):
    mirasiki = 1
    pygame.init()

    game_mode = 0

    done = False
    intro = True
    game_board = Board()

    intro = False
    game_mode = MODE_AI
    game_board.reset()
    game_board.show()
    while not done:
        for e in pygame.event.get():
            if e.type == QUIT:
                done = True
            elif e.type == MOUSEBUTTONUP and intro == False:
                if game_mode == MODE_VS or game_board.player == 'X':
                    game_board.check()

        if game_mode != MODE_VS and game_board.player == '0':
            move(game_board, game_mode)

        game_board.show()

        if game_board.scores["tie"] > 2:
            return 0
        if game_board.scores["X"] > 2:
            return 1
        if game_board.scores["0"] > 2:
            return -1

    pygame.quit()

