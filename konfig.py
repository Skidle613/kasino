import sqlite3
import pygame
import ctypes

conn = sqlite3.connect('players.db')
cursor = conn.cursor()
pygame.init()
width, height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
screen = pygame.display.set_mode((width, height))
myfield = []  #морской бой
botfield = []  #морской бой
myships = 0  #морской бой
botships = 0  #морской бой
for i in range(10):  #морской бой
    myfield.append([])  #морской бой
    botfield.append([])  #морской бой
    for j in range(10):  #морской бой
        myfield[i].append(0)  #морской бой
        botfield[i].append(0)  #морской бой
name = ''
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)
