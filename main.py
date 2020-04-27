import pygame

# Инициализируем модуль pygame
pygame.init()

# Создаем необходимые константы
FPS = 60
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 200
CIRCLE_COLOR = (0, 255, 127)
BG_COLOR = (0, 0, 0)
speed_x = 10
x = 55
y = 100
R = 50
RIGHT = "right"
LEFT = "left"
STOP = "stop"
motion = STOP

# Создаем главное окно и объект класса Clock
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()


# Главная функция
def main():
    global x, speed_x, motion
    run = True
    while run:
        # Заполняем главное окно белым цветом
        display.fill(BG_COLOR)

        pygame.draw.circle(display, CIRCLE_COLOR, (x, y), R, 5)

        for event in pygame.event.get():
            # Обработчик для нажатия на крестик
            if event.type == pygame.QUIT:
                return

        # Берем кортеж клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x += speed_x
        elif keys[pygame.K_LEFT]:
            x -= speed_x

        # Обновляем дисплей для отображения круга
        pygame.display.update()

        # С какой частотой кадров в секунду будет работать программа
        clock.tick(FPS)


if __name__ == "__main__":
    main()
