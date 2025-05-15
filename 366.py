import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Рисование прямоугольников")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Настройки рисования
fill_mode = False  # Режим заливки (False - только контур)
drawing = False  # Флаг процесса рисования
start_pos = None  # Начальная точка прямоугольника
rectangles = []  # Список всех нарисованных прямоугольников

# Основной цикл
clock = pygame.time.Clock()
FPS = 60
running = True

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Нажатие левой кнопки мыши - начало рисования
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка
                drawing = True
                start_pos = event.pos

        # Отпускание кнопки - завершение рисования
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                end_pos = event.pos
                # Создаем прямоугольник и добавляем в список
                rect = pygame.Rect(
                    min(start_pos[0], end_pos[0]),
                    min(start_pos[1], end_pos[1]),
                    abs(end_pos[0] - start_pos[0]),
                    abs(end_pos[1] - start_pos[1])
                )
                rectangles.append((rect, fill_mode))
                start_pos = None

        # Обработка нажатия пробела - переключение режима заливки
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fill_mode = not fill_mode

    # Отрисовка
    screen.fill(WHITE)  # Белый фон

    # Рисуем все сохраненные прямоугольники
    for rect, fill in rectangles:
        if fill:
            pygame.draw.rect(screen, RED, rect)  # Залитый
        else:
            pygame.draw.rect(screen, RED, rect, 2)  # Только контур

    # Рисуем текущий прямоугольник (если рисуем)
    if drawing and start_pos:
        current_pos = pygame.mouse.get_pos()
        temp_rect = pygame.Rect(
            min(start_pos[0], current_pos[0]),
            min(start_pos[1], current_pos[1]),
            abs(current_pos[0] - start_pos[0]),
            abs(current_pos[1] - start_pos[1])
        )
        if fill_mode:
            pygame.draw.rect(screen, RED, temp_rect)
        else:
            pygame.draw.rect(screen, RED, temp_rect, 2)

    # Отображение подсказки
    font = pygame.font.SysFont(None, 24)
    hint_text = font.render("Пробел: переключить режим заливки", True, (0, 0, 0))
    screen.blit(hint_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()