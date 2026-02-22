import pygame
from src.constants import *


class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.start = FONT_SMALL.render("START", True, WHITE)
        self.quit = FONT_SMALL.render("QUIT", True, WHITE)
        self.start_rect = self.start.get_rect(center=(WIDTH//2, HEIGHT//2-30))
        self.quit_rect = self.quit.get_rect(center=(WIDTH//2, HEIGHT//2+30))

    def update(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.start, self.start_rect)
        self.screen.blit(self.quit, self.quit_rect)