import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")
eraser_image = pygame.image.load("eraser.png")
clear_image = pygame.image.load("clear.png")
download_image = pygame.image.load("download.png")
brush_image = pygame.image.load("paint-brush.png")
rectangle_image = pygame.image.load("rectangle.png")
circle_image = pygame.image.load("circle.png")
size_1 = pygame.image.load("size_1.png")
size_2 = pygame.image.load("size_2.png")
size_3 = pygame.image.load("size_3.png")

GREEN = (0, 255, 0)
GRAY = (197, 197, 197)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (107, 104, 99)
PINK = (249, 57, 255)
LIGHT_BLUE = (54, 207, 241)
YELLOW = (255, 241, 73)
ORANGE = (252, 155, 64)
PURPLE = (167, 0, 238)
DARK_GREEN = (58, 158, 73)
BROWN = (85, 46, 46)
PRETTY_BLUE = (0, 238, 195)
WHITE = (255, 255, 255)

green_rect = pygame.Rect(5, 5, 20, 20)
gray_rect = pygame.Rect(30, 5, 20, 20)
black_rect = pygame.Rect(55, 5, 20, 20)
red_rect = pygame.Rect(5, 30, 20, 20)
blue_rect = pygame.Rect(30, 30, 20, 20)
dark_gray_rect = pygame.Rect(55, 30, 20, 20)
pink_rect = pygame.Rect(5, 55, 20, 20)
light_blue_rect = pygame.Rect(30, 55, 20, 20)
yellow_rect = pygame.Rect(55, 55, 20, 20)
orange_rect = pygame.Rect(5, 80, 20, 20)
purple_rect = pygame.Rect(30, 80, 20, 20)
dark_green_rect = pygame.Rect(55, 80, 20, 20)
brown_rect = pygame.Rect(5, 105, 20, 20)
pretty_blue_rect = pygame.Rect(30, 105, 20, 20)
clear_image_rect = pygame.Rect(0, 549, 50, 50)
download_image_rect = pygame.Rect(55, 549, 50, 50)
eraser_image_rect = pygame.Rect(5, 150, 40, 40)
brush_image_rect = pygame.Rect(50, 150, 40, 40)
rectangle_image_rect = pygame.Rect(5, 250, 30, 30)
circle_image_rect = pygame.Rect(40, 250, 30, 30)
size_1_rect = pygame.Rect(5, 200, 30, 30)
size_2_rect = pygame.Rect(37, 205, 20, 20)
size_3_rect = pygame.Rect(59, 210, 10, 10)


screen.fill(WHITE)
save_surface = pygame.Surface((680, 600))

draw = True
brush_size = 10
brush_color = GREEN
border = 1
shape = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONUP:
            draw = False
        if event.type == MOUSEBUTTONDOWN:
            draw = True

    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 120:
        if shape == 0:
            pygame.draw.circle(screen, brush_color, mouse_pos, brush_size)
        if shape == 1:
            pygame.draw.rect(screen, brush_color, [mouse_pos[0], mouse_pos[1], 100, 100], 2)
        if shape == 2:
            pygame.draw.circle(screen, brush_color, mouse_pos, 50, 2)

    if draw:
        if green_rect.collidepoint(mouse_pos):
            brush_color = GREEN
        if gray_rect.collidepoint(mouse_pos):
            brush_color = GRAY
        if blue_rect.collidepoint(mouse_pos):
            brush_color = BLACK
        if red_rect.collidepoint(mouse_pos):
            brush_color = RED
        if blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE
        if dark_gray_rect.collidepoint(mouse_pos):
            brush_color = DARK_GRAY
        if pink_rect.collidepoint(mouse_pos):
            brush_color = PINK
        if light_blue_rect.collidepoint(mouse_pos):
            brush_color = LIGHT_BLUE
        if yellow_rect.collidepoint(mouse_pos):
            brush_color = YELLOW
        if orange_rect.collidepoint(mouse_pos):
            brush_color = ORANGE
        if purple_rect.collidepoint(mouse_pos):
            brush_color = PURPLE
        if dark_green_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN
        if brown_rect.collidepoint(mouse_pos):
            brush_color = BROWN
        if pretty_blue_rect.collidepoint(mouse_pos):
            brush_color = PRETTY_BLUE
        if black_rect.collidepoint(mouse_pos):
            brush_color = BLACK

    if draw:
        if size_1_rect.collidepoint(mouse_pos):
            brush_size = 30
        if size_2_rect.collidepoint(mouse_pos):
            brush_size = 15
        if size_3_rect.collidepoint(mouse_pos):
            brush_size = 5

    if draw:
        if eraser_image_rect.collidepoint(mouse_pos):
            brush_color = WHITE

    if draw:
        if clear_image_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, WHITE, [0, 50, 800, 495])

    if draw:
        if download_image_rect.collidepoint(mouse_pos):
            save_surface.blit(screen, (0, 0), (120, 0, 680, 600))
            pygame.image.save(save_surface, "saved_image.png")

    if draw:
        if rectangle_image_rect.collidepoint(mouse_pos):
            shape = 1
        if circle_image_rect.collidepoint(mouse_pos):
            shape = 2
        if brush_image_rect.collidepoint(mouse_pos):
            shape = 0

    pygame.draw.rect(screen, GREEN, green_rect)
    pygame.draw.rect(screen, GRAY, gray_rect)
    pygame.draw.rect(screen, BLACK, black_rect)
    pygame.draw.rect(screen, RED, red_rect)
    pygame.draw.rect(screen, BLUE, blue_rect)
    pygame.draw.rect(screen, DARK_GRAY, dark_gray_rect)
    pygame.draw.rect(screen, PINK, pink_rect)
    pygame.draw.rect(screen, LIGHT_BLUE, light_blue_rect)
    pygame.draw.rect(screen, YELLOW, yellow_rect)
    pygame.draw.rect(screen, ORANGE, orange_rect)
    pygame.draw.rect(screen, PURPLE, purple_rect)
    pygame.draw.rect(screen, DARK_GREEN, dark_green_rect)
    pygame.draw.rect(screen, BROWN, brown_rect)
    pygame.draw.rect(screen, PRETTY_BLUE, pretty_blue_rect)
    pygame.draw.rect(screen, BLACK, black_rect)
    pygame.draw.line(screen, BLACK, (105, 0), (105, 600), 3)
    screen.blit(brush_image, brush_image_rect)
    screen.blit(eraser_image, eraser_image_rect)
    screen.blit(clear_image, clear_image_rect)
    screen.blit(download_image, download_image_rect)
    screen.blit(rectangle_image, rectangle_image_rect)
    screen.blit(circle_image, circle_image_rect)
    screen.blit(size_1, size_1_rect)
    screen.blit(size_2, size_2_rect)
    screen.blit(size_3, size_3_rect)

    pygame.display.update()

pygame.quit()
