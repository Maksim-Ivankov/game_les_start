# ДОБАВЛЕНИЕ ИГРОКА И АНИМАЦИЯ

import pygame

# sprytesheet - карточка игрока

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618,359)) 


bg = pygame.image.load('it-proger/images/bg.png')
walk_left = [ # для анимации
    pygame.image.load('it-proger/images/player_left/1.png'),
    pygame.image.load('it-proger/images/player_left/2.png'),
    pygame.image.load('it-proger/images/player_left/3.png'),
    pygame.image.load('it-proger/images/player_left/4.png'),
]
walk_right = [
    pygame.image.load('it-proger/images/player_right/1.png'),
    pygame.image.load('it-proger/images/player_right/2.png'),
    pygame.image.load('it-proger/images/player_right/3.png'),
    pygame.image.load('it-proger/images/player_right/4.png'),
]

player_anim_count = 0

running = True
while running:
    
    screen.blit(bg, (0,0))
    screen.blit(walk_right[player_anim_count], (300,250))
    player_anim_count+=1
    if player_anim_count==4: player_anim_count=0
    
   
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            running = False 
    clock.tick(10)