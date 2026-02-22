import pygame
from pygame.locals import *
from src.objects import *
pygame.init()

class Game:

    def __init__(self, screen, dif, score):
        self.screen = screen
        self.difficulty = dif
        self.ball = Ball(self.screen, score)
        self.player = Player(self.difficulty, self.screen)
        self.AI = AI(self.screen, self.difficulty)


    def update(self, events):
        self.player.move(events)
        self.ball.hit(self.player.image, self.AI.image)
        self.screen.fill(BLACK)
        self.player.update()
        self.AI.update(self.ball)
        self.ball.update()