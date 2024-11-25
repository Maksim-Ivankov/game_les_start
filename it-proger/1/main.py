# НАЧАЛО

import pygame

pygame.init()
screen = pygame.display.set_mode((600,300)) # размер окна

running = True
screen.fill((114,157,224)) # красим фон

while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # если нажали на крест
            pygame.quit() # закрываем окно
            running = False # схлопываем бесконечный цикл
        if event.type == pygame.KEYDOWN: # если нажали на кнопку
            if event.key == pygame.K_a: # конкретно на кнопку а
                screen.fill((70,44,133)) # красим фон в дургой цвет




    





















































































