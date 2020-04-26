import pygame
import tkinter

# Инициализация модулей pygame
pygame.init()

# Задаем количество кадров в секунду для приложения
FPS = 60

# Задаем необходимые цвета
LIGHTGREEN = (0, 255, 127)

# Задаем объекты, создаем главное окно
clock = pygame.time.Clock()
display = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My first game")


# Создаем фигуры
pygame.draw.rect(display, LIGHTGREEN, (50, 50, 100, 100))
pygame.display.update()


# Функция для бесконечного цикла и обработчика событий
def main():
    run = True
    while run:
        # Создаем задержку
        clock.tick(FPS)
        # Обработчик для нажатия на Х
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
