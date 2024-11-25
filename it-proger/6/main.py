# добавили призрака и конвертируем изображения

import pygame



clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618,359)) 

player_speed = 5 
player_x = 150 
player_y = 250 

is_jump = False
jump_count = 7 # высота прыжка

bg = pygame.image.load('it-proger/images/bg.png').convert()
# .convert() - конвертация картинки в удобный для библиотеки формат. Для непрозрачных картинок

# призрак
ghost = pygame.image.load('it-proger/images/prizrak.png').convert_alpha()
# .convert_alpha() - Тоже самое, но для прозрачных картинок
ghost_x = 620


walk_left = [ 
    pygame.image.load('it-proger/images/player_left/1.png').convert_alpha(),
    pygame.image.load('it-proger/images/player_left/2.png').convert_alpha(),
    pygame.image.load('it-proger/images/player_left/3.png').convert_alpha(),
    pygame.image.load('it-proger/images/player_left/4.png').convert_alpha(),
]
walk_right = [
    pygame.image.load('it-proger/images/player_right/1.png').convert_alpha(),
    pygame.image.load('it-proger/images/player_right/2.png').convert_alpha(),
    pygame.image.load('it-proger/images/player_right/3.png').convert_alpha(),
    pygame.image.load('it-proger/images/player_right/4.png').convert_alpha(),
]

player_anim_count = 0 

bg_x = 0 


running = True
while running:

    screen.blit(bg, (bg_x,0))
    
    # добавили призрака и он ходит
    screen.blit(ghost, (ghost_x,250))
    ghost_x-=10
    if ghost_x<0: ghost_x=620
    
    
    if player_anim_count==4: player_anim_count=0
    if bg_x==-620: bg_x=0 
    
    screen.blit(walk_right[player_anim_count], (player_x,player_y))
    
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and player_x>50: 
        screen.blit(walk_left[player_anim_count], (player_x,player_y))
        player_x -=player_speed
        player_anim_count+=1
    if keys[pygame.K_RIGHT] and player_x<200: 
        screen.blit(walk_right[player_anim_count], (player_x,player_y))
        player_x +=player_speed
        player_anim_count+=1
    
    
    
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count>= -7:
            if jump_count>0:
                player_y -= (jump_count**2)/2
            else:
                player_y += (jump_count**2)/2
            jump_count-=1
        else:
            is_jump = False
            jump_count=7
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            running = False 
    clock.tick(10)