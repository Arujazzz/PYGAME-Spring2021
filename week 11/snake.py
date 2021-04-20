import pygame
import random
import time
import pickle

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
wall_image = pygame.image.load("wall.png")
eating_food_sound = pygame.mixer.Sound("eating food.mp3")
eating_food_sound.set_volume(0.1)
gameover_sound = pygame.mixer.Sound("gameover.mp3")

def show_background():
    for x in range(0, 600):
        for y in range(0, 600):
            if (x + y)%2 == 0:
                pygame.draw.rect(screen, (93,216,228), [x*20, y*20, 20, 20])
            else:
                pygame.draw.rect(screen, (84,194,205), [x*20, y*20, 20, 20])
    for x in range(0, 600, 20):
        for y in range(0, 600, 20):
            screen.blit(wall_image, (x, 0))
            screen.blit(wall_image, (x, 580))
            screen.blit(wall_image, (0, y))
            screen.blit(wall_image, (580, y))

class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]
        self.dx = 0
        self.dy = 0
        self.color = (0, 0, 0)
        self.is_add = False
        self.score = 0
        self.speed = 30

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, self.color, [element[0], element[1], 20, 20])

    def add_to_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size%3 == 0:
            self.speed += 10

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def eat(self, food_x, food_y):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if food_x - 19 <= x <= food_x + 19 and food_y - 19 <= y <= food_y + 19:
            return True
        return False

class Food:
    def __init__(self):
        self.x = random.randrange(20, 580, 20)
        self.y = random.randrange(20, 580, 20)
        self.color = (223, 163, 49)

    def new_food(self):
        self.x = random.randrange(20, 580, 20)
        self.y = random.randrange(20, 580, 20)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 20, 20))

snake1 = Snake(100, 100)
snake2 = Snake(160, 100)
snakes = (snake1, snake2)
food = Food()
d = 20
choose = False
FILE_NAME = 'snakes_saved.data'

def show_score_snake1(x, y):
    myfont = pygame.font.SysFont("Times new roman", 20)
    score_text = myfont.render('Score_1: ' + str(snake1.score), True, (0, 0, 0))
    screen.blit(score_text, (x, y))

def show_score_snake_2(x, y):
    myfont = pygame.font.SysFont("Times new roman", 20)
    score_text = myfont.render('Score_2: ' + str(snake2.score), True, (0, 0, 0))
    screen.blit(score_text, (x, y))

def game_over():
    screen.fill((255, 0, 0))
    gameover_sound.play()
    font = pygame.font.SysFont("Times new roman", 25)
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    my_score = font.render('Total score: ' + str(snake1.score + snake2.score), True, (255, 255, 255))
    screen.blit(game_over_text, (250, 250))
    screen.blit(my_score, (240, 350))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

def is_in_walls():
    if snake1.elements[0][0] > 560 or snake1.elements[0][0] < 20 or snake1.elements[0][1] > 560 or snake1.elements[0][1] < 20 or snake2.elements[0][0] > 560 or snake2.elements[0][0] < 20 or snake2.elements[0][1] > 560 or snake2.elements[0][1] < 20:
        return True
    return False

def second_snake():
    if snake1.score > 5:
        snake2.draw()
        snake2.move()
        show_score_snake_2(480, 0)
        font = pygame.font.SysFont("Times new roman", 20)
        text = font.render("Second level", True, (0, 0, 255))
        screen.blit(text, (250, 0))

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False

        font = pygame.font.SysFont('Times new roman', 25)
        paused_text = font.render("Paused! Press enter to continue", True, (0, 0, 0))
        screen.blit(paused_text, (150, 250))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            paused = False
        pygame.display.update()

game = True
while game:
    clock.tick(snake1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            if event.key == pygame.K_d and snake2.dx != -d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a and snake2.dx != d:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w and snake2.dy != d:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s and snake2.dy != -d:
                snake2.dx = 0
                snake2.dy = d
            if event.key == pygame.K_SPACE:
                pause()
            if event.key == pygame.K_ESCAPE:
                with open("saved_snakes.data", 'wb') as f:
                    pickle.dump(snakes, f)
                with open("saved_snakes.data", 'rb') as f:
                    new_snakes = pickle.load(f)
                game = False
                pygame.quit()


    if snake1.eat(food.x, food.y):
        snake1.is_add = True
        eating_food_sound.play()
        food.new_food()

    if snake2.eat(food.x, food.y):
        snake2.is_add = True
        eating_food_sound.play()
        food.new_food()

    if is_in_walls():
        game_over()
        game = False

    show_background()
    snake1.move()
    snake1.draw()
    food.draw()
    second_snake()
    show_score_snake1(20, 0)
    pygame.display.flip()

pygame.quit()
