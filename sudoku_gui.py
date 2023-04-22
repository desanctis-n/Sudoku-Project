import pygame
import sys
from sudoku_generator import *

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
RED = (255, 0, 0)
BG_COLOR = (192, 192, 192)
LINE_COLOR_MAIN = (125, 125, 125)
CIRCLE_COLOR = (155, 155, 155)
CROSS_COLOR = (66, 66, 66)
CHIP_FONT = 300
GAME_OVER_FONT = 40
COLOR_1 = (0, 1, 250)
COLOR_2 = (1, 127, 1)
COLOR_3 = (241, 0, 7)
COLOR_4 = (5, 0, 138)
COLOR_5 = (119, 4, 1)
COLOR_6 = (0, 129, 127)
COLOR_7 = (10, 10, 10)
COLOR_8 = (128, 128, 128)
COLOR_9 = (241, 241, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweedoku")
screen.fill(BG_COLOR)
chip_font = pygame.font.Font(None, CHIP_FONT)


def draw_grid():
    # horizontal
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR_MAIN, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

    # vertical
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR_MAIN, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH), LINE_WIDTH)


def draw_chips():

    chip_1_surf = chip_font.render('1', 0, COLOR_1)
    chip_1_rect = chip_1_surf.get_rect(center=(100, 100))
    screen.blit(chip_1_surf, chip_1_rect)

    chip_2_surf = chip_font.render('2', 0, COLOR_2)
    chip_2_rect = chip_2_surf.get_rect(center=(300, 100))
    screen.blit(chip_2_surf, chip_2_rect)

    chip_3_surf = chip_font.render('3', 0, COLOR_3)
    chip_3_rect = chip_3_surf.get_rect(center=(500, 100))
    screen.blit(chip_3_surf, chip_3_rect)

    chip_4_surf = chip_font.render('4', 0, COLOR_4)
    chip_4_rect = chip_4_surf.get_rect(center=(100, 300))
    screen.blit(chip_4_surf, chip_4_rect)

    chip_5_surf = chip_font.render('5', 0, COLOR_5)
    chip_5_rect = chip_5_surf.get_rect(center=(300, 300))
    screen.blit(chip_5_surf, chip_5_rect)

    chip_6_surf = chip_font.render('6', 0, COLOR_6)
    chip_6_rect = chip_6_surf.get_rect(center=(500, 300))
    screen.blit(chip_6_surf, chip_6_rect)

    chip_7_surf = chip_font.render('7', 0, COLOR_7)
    chip_7_rect = chip_7_surf.get_rect(center=(100, 500))
    screen.blit(chip_7_surf, chip_7_rect)

    chip_8_surf = chip_font.render('8', 0, COLOR_8)
    chip_8_rect = chip_8_surf.get_rect(center=(300, 500))
    screen.blit(chip_8_surf, chip_8_rect)

    chip_9_surf = chip_font.render('9', 0, COLOR_9)
    chip_9_rect = chip_9_surf.get_rect(center=(500, 500))
    screen.blit(chip_9_surf, chip_9_rect)






    draw_grid()
draw_chips()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()

