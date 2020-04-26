import pygame
import tkinter

# Инициализация модулей pygame
pygame.init()

# Задаем количество кадров в секунду для приложения
FPS = 60

# Задаем объекты, создаем главное окно
clock = pygame.time.Clock()
pygame.display.set_mode((600, 400))
pygame.display.set_caption("My first game")


# Функция для бесконечного цикла и обработчика событий
def main():
    # Создаем задержку
    clock.tick(FPS)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
