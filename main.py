import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import pygame, json
from src.objects import *
from src.constants import *
from src.game import *
from src.menu import *
pygame.init()

def load_data(selected):
    with open("assets/data/difficulty.json") as f:
        data = json.load(f)

    return data[0][selected]

screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN, vsync=1)
pygame.display.set_caption("PONG!")
clock = pygame.time.Clock()
state = "menu"
dif = "easy"
difficulty = load_data(dif)
menu = Menu(screen)
game = Game(screen, difficulty, score=0)

running = True
while running:
    MOUSE_POS = pygame.mouse.get_pos()
    events = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if menu.quit_rect.collidepoint(MOUSE_POS) and state == "menu":
                    running = False
                if menu.start_rect.collidepoint(MOUSE_POS) and state == "menu":
                    state = "game"
                    game = Game(screen, difficulty, score=0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                state = "menu"
    if menu.quit_rect.collidepoint(MOUSE_POS) and state == "menu":
        menu.quit = FONT_SMALL.render("QUIT", True, GREY)
    elif not menu.quit_rect.collidepoint(MOUSE_POS) and state == "menu":
        menu.quit = FONT_SMALL.render("QUIT", True, WHITE)  
    if menu.start_rect.collidepoint(MOUSE_POS) and state == "menu":
        menu.start = FONT_SMALL.render("START", True, GREY)
    elif not menu.start_rect.collidepoint(MOUSE_POS) and state == "menu":
        menu.start = FONT_SMALL.render("START", True, WHITE)

    if state=="menu":
        menu.update()
    elif state=="game":
        game.update(events)

    pygame.display.flip()
    clock.tick(60)