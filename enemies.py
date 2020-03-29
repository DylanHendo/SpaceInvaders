import pygame

class Enemy(object):

    def __init__(self, img, x, y, width, height, velocity, score):
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.score = score
        self.hitbox = (self.x, self.y, self.width, self.height)     # setup hitbox (can remove later)

    def draw_enemy(self, screen):
        screen.blit(self.img, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)     # updates hitbox so moves with enemy
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 1)     # show hitbox around enemies


class EnemyBullets(object):

    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

    def move_projectiles(self):
        self.y -= self.velocity

    def draw_projectiles(self, screen):
        bullet = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (255, 255, 255), bullet)
