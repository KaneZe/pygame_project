import pygame
import tkinter

pygame.init()

# Создание окна 600х400 пикселей
pygame.display.set_mode((600, 400))

# Создание бесконечно цикла
while 1:
    for event in pygame.event.get():
        # При нажатии на Х, выходим из программы
        if event.type == pygame.QUIT:
            pygame.quit()
