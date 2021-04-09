import pygame
import random
import time
pygame.init()
backimage = pygame.image.load("background.png")
playerimage = pygame.image.load("Player.png")
enemyimage = pygame.image.load("Enemy.png")
coinsimage1 = pygame.image.load("coins1.png")
coinsimage2 = pygame.image.load("coins2.png")

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
red = (255, 0, 0)
black = (0, 0, 0)

player_x = 160
player_y = 504
player_dx = 4

enemy_x = 40
enemy_y = 30
enemy_dy = 5

coins_x1 = 150
coins_y1= 0
coins_dy = 5
coins_x2 = 350
coins_y2 = 0
score = 0
def show_player(x, y):
    screen.blit(playerimage, (player_x, player_y))

def show_enemy(x, y):
    screen.blit(enemyimage, (enemy_x, enemy_y))

def show_coins1(x, y):
    screen.blit(coinsimage1, (coins_x1, coins_y1))

def show_coins2(x, y):
    screen.blit(coinsimage2, (coins_x2, coins_y2))

def isCollision(player_x, player_y, enemy_x, enemy_y):
    if player_x in range(enemy_x - 44, enemy_x + 48) and player_y - enemy_y <= 93:
        return True
    return False

def isCollisioncoins1Player(player_x, player_y, coins_x1, coins_y1):
    if coins_x1 in range (player_x - 25, player_x + 44) and coins_y1 in range (player_y, player_y + 93):
        return True
    return False

def isCollisioncoins2Player(player_x, player_y, coins_x2, coins_2):
    if coins_x2 in range (player_x - 25, player_x + 44) and coins_y2 in range (player_y, player_y + 93):
        return True
    return False

def show_score(x, y):
    font = pygame.font.SysFont('Times new roman', 20)
    sc = font.render("Score: " + str(score), True, black)
    screen.blit(sc, (x, y))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
       
    screen.blit(backimage, (0, 0))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player_x -= player_dx
    if pressed[pygame.K_RIGHT]:
        player_x += player_dx

    enemy_y += enemy_dy
    if enemy_y > 600:
        enemy_y = 0
        enemy_dy = random.randint(1, 5)
        enemy_x = random.randint(40, 360)

    coins_y1 += coins_dy
    if coins_y1 > 600:
        coins_y1 = 0
        coins_dy = random.randint(1, 5)
        coins_x1 = random.randint(40, 375)

    coins_y2 += coins_dy
    if coins_y2 > 600:
        coins_y2 = 0
        coins_dy = random.randint(1, 5)
        coins_x2 = random.randint(40, 375)

    isCol = isCollision(player_x, player_y, enemy_x, enemy_y)
    if isCol:
        enemy_dy = 0
        player_dx = 0
        coins_dy = 0
        screen.fill(red)
        font = pygame.font.SysFont('Times new roman', 40)
        text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(text, (100, 300))

    isColcoins1Player = isCollisioncoins1Player(player_x, player_y, coins_x1, coins_y1)
    if isColcoins1Player:
        coins_x1 = random.randint(25, 375)
        coins_y1 = 0
        score += 1

    isColcoins2Player = isCollisioncoins2Player(player_x, player_y, coins_x2, coins_y2)
    if isColcoins2Player:
        coins_x2 = random.randint(25, 375)
        coins_y2 = 0
        score += 1

    show_player(player_x, player_y)
    show_enemy(enemy_x, enemy_y)
    show_coins1(coins_x1, coins_y1)
    show_coins2(coins_x2, coins_y2)
    show_score(320, 50)
    clock.tick(60)
    pygame.display.update()

