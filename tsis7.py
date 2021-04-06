import pygame
import math
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pygame.init()
screen = pygame.display.set_mode((1020, 600))
nums = ['-1', '-0.75', '-0.5', '-0.25', '0', '0.25', '0.5', '0.75', '1', '2']
draw = True
while draw:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.fill(white)
    pygame.display.set_caption('sin and cos')
    #radians
    font = pygame.font.Font(None, 37)
    text1 = font.render("-3П   -2,5П   -2П   -1,5П    -П   -0,5П        0      0,5П     П     1,5П     2П     2,5П     3П",True, black)
    screen.blit(text1, (50, 570))
    #numbered
    font = pygame.font.Font(None, 20)
    ln = len(nums) - 2
    for i in range(60, 570, 60):
        text = font.render(nums[ln], True, black)
        screen.blit(text, (2, i))
        ln -= 1
    ln = 0
    pygame.draw.line(screen, black, (30, 30), (990, 30), 4)   #a
    pygame.draw.line(screen, black, (30, 30), (30, 570), 4)   #b
    pygame.draw.line(screen, black, (990, 30), (990, 570), 4) #d
    pygame.draw.line(screen, black, (30, 570), (990, 570), 4) #c
    #X, Y
    pygame.draw.line(screen, black, (30, 300), (990, 300), 4)
    pygame.draw.line(screen, black, (510, 30), (510, 570), 4)
    #нижний, верхний
    pygame.draw.line(screen, black, (30, 60), (990, 60), 2)
    pygame.draw.line(screen, black, (30, 540), (990, 540), 2)
    #левый, правый
    pygame.draw.line(screen, black, (60, 30), (60, 570), 2)
    pygame.draw.line(screen, black, (960, 30), (960, 570), 2)
    for x in range(210, 990, 150):
        pygame.draw.line(screen, black, (x, 30), (x, 570), 2)
    for y in range(60, 570, 60):
        pygame.draw.line(screen, black, (30, y), (990, y))
    #отметки по Х
    for x in range(135, 990, 150):
        pygame.draw.line(screen, black, (x, 30), (x, 50))
        pygame.draw.line(screen, black, (x, 550), (x, 570))
    for x in range(97, 960, 75):
        pygame.draw.line(screen, black, (x, 30), (x, 45))
        pygame.draw.line(screen, black, (x, 555), (x, 570))
    for x in range(78, 510, 37):
        pygame.draw.line(screen, black, (x, 30), (x, 40))
        pygame.draw.line(screen, black, (x, 560), (x, 570))
    for x in range(528, 960, 37):
        pygame.draw.line(screen, black, (x, 30), (x, 40))
        pygame.draw.line(screen, black, (x,560), (x, 570))
    #отметки по У
    for y in range(90, 540, 60):
        pygame.draw.line(screen, black, (30, y), (50, y))
        pygame.draw.line(screen, black, (970, y), (990, y))
    for y in range(75, 540, 30):
       pygame.draw.line(screen, black, (30, y), (45, y))
       pygame.draw.line(screen, black, (975, y), (990, y))
    #график синуса и косинуса
    coscoor, sincoor = [], []
    for x in range(60, 960 + 1):
        xrad = (((x - 510) * math.pi) / 150)
        cosy = (math.cos(xrad) * -240) + 300
        siny = (math.sin(xrad) * -240) + 300
        coscoor.append((x, cosy))
        sincoor.append((x, siny))
    pygame.draw.aalines(screen, red, False, sincoor)
    for point in range(0, len(coscoor) - 1, 2):
        pygame.draw.aaline(screen, blue, coscoor[point], coscoor[point + 1])
    font = pygame.font.Font(None, 30)
    textsin = font.render("sin -", True, red)
    textcos = font.render("cos - -", True, blue)
    screen.blit(textsin, (665, 65))
    screen.blit(textcos, (665, 80))
    
    pygame.display.flip()
