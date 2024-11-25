# ДОБАВЛЕНИЕ КАРТИНОК И ФИГУР

import pygame

pygame.init()
screen = pygame.display.set_mode((600,300)) 

running = True

square = pygame.Surface((50,170)) # создали квадрат
square.fill('Blue') # раскрасили квадрат
 
player = pygame.image.load('it-proger/images/cwsa.jpg') # подгружаем картинку

while running:
    
    screen.blit(player, (0,0)) # добавли картинку на экран
    screen.blit(square, (20,20)) # добавли квадрат на экран
    
    pygame.draw.circle(screen, 'red', (20,20), 30) # либо рисуем круг разом
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            running = False 
