import pygame, src.constants, math, random
from pygame.locals import *
from src.constants import *


class Player:

    def __init__(self, difficulty, screen):
        self.screen = screen
        self.speed = difficulty["speed"]
        self.y = HEIGHT//2
        self.x = WIDTH-100
        self.image = pygame.draw.rect(self.screen, WHITE, (self.x, self.y, 30, 200))

    def update(self):
        self.image = pygame.draw.rect(self.screen, WHITE, (self.x, self.y, 30, 200))

    def move(self, event):
        if event[K_UP]:
            self.y-=self.speed
        elif event[K_DOWN]:
            self.y+=self.speed


class Ball:

    def __init__(self, screen, score):
        self.score = score
        self.screen = screen
        self.speed = 20
        self.y = HEIGHT//2
        self.x = WIDTH//2
        self.angle = math.radians(0)
        self.vx = math.cos(self.angle) * self.speed
        self.vy = math.sin(self.angle) * self.speed
        self.image = pygame.draw.rect(self.screen, WHITE, (self.x, self.y, 30, 30))
        self.direction = True

    def update(self):
        if self.direction:
            self.vx = math.cos(self.angle) * self.speed
            self.vy = math.sin(self.angle) * self.speed
        else:
            self.vx = -math.cos(self.angle) * self.speed
            self.vy = -math.sin(self.angle) * self.speed
        self.x += self.vx
        self.y += self.vy
        if self.y >= HEIGHT:
            self.y = 0
        if self.y <= 0:
            self.y = HEIGHT
        if self.x >= WIDTH or self.x <= 0:
            self.x = WIDTH//2
            self.y = HEIGHT//2
            self.angle = math.radians(0)
            self.score+=1
        self.image = pygame.draw.rect(self.screen, WHITE, (self.x, self.y, 30, 30))

    def hit(self, paddle1, paddle2):
        if self.image.colliderect(paddle1) or self.image.colliderect(paddle2):
            self.direction = not self.direction
            self.angle = math.radians(random.choice([20, 0, -20, 15, -15, 10, -10, 25, -25]))

    
class AI:

    def __init__(self, screen, difficulty):
        self.screen = screen
        self.speed = difficulty["speed"]
        self.x = 100
        self.y = HEIGHT // 2
        self.offset = 0
        self.reactionTimer = 0
        self.image = pygame.draw.rect(self.screen, WHITE, (self.x, self.y, 30, 200))

    def update(self, ball):

        if ball.vx < 0:

            self.reactionTimer -= 1

            if self.reactionTimer <= 0:

                self.offset = random.choice([-40, -20, 0, 20, 40])

                if random.randint(1, 100) <= 5:
                    self.offset = random.choice([-150, 150])

                self.reactionTimer = 10

            targetY = ball.y + self.offset

            if self.y < targetY:
                self.y += self.speed
            elif self.y > targetY:
                self.y -= self.speed

        self.image = pygame.draw.rect(self.screen, WHITE, (self.x, self.y, 30, 200))