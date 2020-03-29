import pygame

class Spaceship(object):

    def __init__(self, image, x, y, width, height, velocity):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

    def move_ship(self):
        key = pygame.key.get_pressed()

        if (key[pygame.K_LEFT]) and (self.x >= self.velocity):
            self.x -= self.velocity
        if (key[pygame.K_RIGHT]) and (self.x < (1000 - self.width)):
            self.x += self.velocity

    def draw_ship(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Bullets(object):

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


class Shields(object):

    def __init__(self, img, x, y, width, height):
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_shield(self, screen):
        screen.blit(self.img, (self.x, self.y))
