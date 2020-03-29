# main rules:
#
#   - 1 bullet allowed on screen at once for player
#   - 3 bullets allowed on screen at once for invaders
#   - only lowest invader can shoot (can't shoot if invader beneath it)
#   - 3 lives

#   bonus:
#       - invaders get progressively faster ??
#       - if both bullets collide, they disappear

# TODO:
#   - enemies shoot
#   - shields deteriorate/disappear
#   - game over mode
#   - sounds

import pygame
from spaceship import Spaceship
from spaceship import Bullets
from spaceship import Shields
from enemies import Enemy

pygame.init()

# setup screen
background_colour = (0, 0, 0)
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
score = 0

screen.fill(background_colour)
pygame.display.flip()
pygame.display.set_caption("Space Invaders")


# load spaceship image
ship_img = pygame.image.load('images/ship.png')
ship_width, ship_height = (60, 30)
ship_img = pygame.transform.scale(ship_img, (ship_width, ship_height))

# load shield image
shield_img = pygame.image.load('images/shield.png')
shield_width, shield_height = (100, 75)
shield_img = pygame.transform.scale(shield_img, (shield_width, shield_height))

# load enemy images
enemy_width, enemy_height = (30, 30)
enemy1 = pygame.image.load('images/enemy1.png')
enemy1 = pygame.transform.scale(enemy1, (enemy_width, enemy_height))

enemy2 = pygame.image.load('images/enemy2.png')
enemy2 = pygame.transform.scale(enemy2, (enemy_width, enemy_height))

enemy3 = pygame.image.load('images/enemy3.png')
enemy3 = pygame.transform.scale(enemy3, (enemy_width, enemy_height))

# spaceship object
ship = Spaceship(ship_img, screen_width//2 - ship_width//2, screen_height-50, ship_width, ship_height, 5)

# set up list of enemies
enemies_list_1 = []
enemies_list_2 = []
enemies_list_3 = []
start_x = 50
increment = 50
speed = 2
score_1 = 10
score_2 = 20
score_3 = 30

# create lists for every lvl enemy
for i in range(10):
    enemies_list_3.append(Enemy(enemy3, start_x, 50, enemy_width, enemy_height, speed, score_3))

    enemies_list_2.append(Enemy(enemy2, start_x, 90, enemy_width, enemy_height, speed, score_2))
    enemies_list_2.append(Enemy(enemy2, start_x, 130, enemy_width, enemy_height, speed, score_2))

    enemies_list_1.append(Enemy(enemy1, start_x, 170, enemy_width, enemy_height, speed, score_1))
    enemies_list_1.append(Enemy(enemy1, start_x, 210, enemy_width, enemy_height, speed, score_1))
    start_x += increment


# create list of shields to draw on screen
shield_list = []
shield_x = 60
shield_y = screen_height - 150
shield_increment = screen_width // 4
for i in range(4):
    shield_list.append(Shields(shield_img, shield_x, shield_y, shield_width, shield_height))
    shield_x += shield_increment


# function to write score to screen
font = pygame.font.Font(None, 30)
def write(text, location=(10, 10), color=(255, 255, 255)):
    screen.blit(font.render(text, True, color), location)


def update_enemies():
    """Updates location and velocity of enemies"""
    for en in enemies_list_1:
        en.x += en.velocity
        en.draw_enemy(screen)

    # move and draw every lvl 2 enemy
    for en in enemies_list_2:
        en.x += en.velocity
        en.draw_enemy(screen)

    # move and draw every lvl 3 enemy
    for en in enemies_list_3:
        en.x += en.velocity
        en.draw_enemy(screen)


    # for all lvl 1 enemies
    for e in enemies_list_1:
        if (e.x >= screen_width - e.width) or (e.x <= 2):
            for a in enemies_list_1:
                a.velocity = -a.velocity
                a.y += 30
                a.x += a.velocity

            for b in enemies_list_2:
                b.velocity = -b.velocity
                b.y += 30
                b.x += b.velocity

            for c in enemies_list_3:
                c.velocity = -c.velocity
                c.y += 30
                c.x += c.velocity

    # for all lvl 2 enemies
    for en in enemies_list_2:
        if (en.x >= screen_width - en.width) or (en.x <= 2):
            for a in enemies_list_1:
                a.velocity = -a.velocity
                a.y += 30
                a.x += a.velocity

            for b in enemies_list_2:
                b.velocity = -b.velocity
                b.y += 30
                b.x += b.velocity

            for c in enemies_list_3:
                c.velocity = -c.velocity
                c.y += 30
                c.x += c.velocity

    # for all lvl 3 enemies
    for enem in enemies_list_3:
        if (enem.x >= screen_width - enem.width) or (enem.x <= 2):
            for a in enemies_list_1:
                a.velocity = -a.velocity
                a.y += 30
                a.x += a.velocity

            for b in enemies_list_2:
                b.velocity = -b.velocity
                b.y += 30
                b.x += b.velocity

            for c in enemies_list_3:
                c.velocity = -c.velocity
                c.y += 30
                c.x += c.velocity


# main game loop
bullets = []    # list for bullet objects
running = True
while running:
    screen.fill([0, 0, 0])      # black screen

    # update ship
    ship.move_ship()
    ship.draw_ship(screen)
    write('SCORE: ' + str(score))

    for s in shield_list:
        s.draw_shield(screen)

    # for all events
    for event in pygame.event.get():
        # if quit
        if event.type == pygame.QUIT:           # quit event
            running = False
        # if space button (shoot)
        if event.type == pygame.KEYDOWN:        # shoot event
            if event.key == pygame.K_SPACE:
                # max amount of bullets available on screen at once (only 1)
                if len(bullets) < 1:
                    # create new bullet object, append to list
                    bullets.append(Bullets(ship.x + ship_width // 2 - 1, ship.y, 3, 10, 15))

    # move bullet while still on screen, delete when off screen
    for bullet in bullets:
        # for en in enemies:
        if bullet.y > 0:
            bullet.move_projectiles()
        else:
            bullets.pop(bullets.index(bullet))      # delete bullet from screen

        bullet.draw_projectiles(screen)

    # checks collision between bullets and enemies
    for b in bullets:
        for e in enemies_list_1:
            # if bullet x in between left and right of enemy hitbox
            if (b.x < (e.hitbox[0] + e.hitbox[2])) and b.x > e.hitbox[0]:
                # if bullet y in between bottom and top of hitbox
                if (b.y < e.hitbox[1] + e.hitbox[3]) and b.y > e.hitbox[1]:
                    bullets.pop(bullets.index(b))   # delete bullet from screen
                    enemies_list_1.pop(enemies_list_1.index(e))   # delete enemy from screen
                    score += score_1

        for en in enemies_list_2:
            # if bullet x in between left and right of enemy hitbox
            if (b.x < (en.hitbox[0] + en.hitbox[2])) and b.x > en.hitbox[0]:
                # if bullet y in between bottom and top of hitbox
                if (b.y < en.hitbox[1] + en.hitbox[3]) and b.y > en.hitbox[1]:
                    bullets.pop(bullets.index(b))   # delete bullet from screen
                    enemies_list_2.pop(enemies_list_2.index(en))   # delete enemy from screen
                    score += score_2

        for enem in enemies_list_3:
            # if bullet x in between left and right of enemy hitbox
            if (b.x < (enem.hitbox[0] + enem.hitbox[2])) and b.x > enem.hitbox[0]:
                # if bullet y in between bottom and top of hitbox
                if (b.y < enem.hitbox[1] + enem.hitbox[3]) and b.y > enem.hitbox[1]:
                    bullets.pop(bullets.index(b))   # delete bullet from screen
                    enemies_list_3.pop(enemies_list_3.index(enem))   # delete enemy from screen
                    score += score_3

    update_enemies()
    pygame.display.update()

pygame.quit()
