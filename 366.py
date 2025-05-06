import pygame
import math

pygame.init()

BUTTON_COLOR = (0, 191, 255)
HOVER_COLOR = (0, 140, 255)
CLICK_COLOR = (0, 50, 255)
BACKGROUND_COLOR = (255, 255, 255)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BUTTON_RADIUS = 50
BUTTON_CENTER = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Кнопка")

hovering = False
clicking = False

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            if distance(event.pos, BUTTON_CENTER) < BUTTON_RADIUS:
                hovering = True
            else:
                hovering = False
                if clicking:
                    BUTTON_CENTER[0] = event.pos[0]
                    BUTTON_CENTER[1] = event.pos[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and distance(event.pos, BUTTON_CENTER) < BUTTON_RADIUS:
                clicking = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicking = False

    screen.fill(BACKGROUND_COLOR)

    if clicking:
        button_color = CLICK_COLOR
    elif hovering:
        button_color = HOVER_COLOR
    else:
        button_color = BUTTON_COLOR

    pygame.draw.circle(screen, button_color, BUTTON_CENTER, BUTTON_RADIUS)

    pygame.display.update()

pygame.quit()