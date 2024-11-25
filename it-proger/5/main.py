# наусчились ходить и прыгать

import pygame



clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618,359)) 

player_speed = 5 # скорость игрока
player_x = 150 # положение игрока
player_y = 250 # положение игрока

is_jump = False
jump_count = 7 # высота прыжка

bg = pygame.image.load('it-proger/images/bg.png')
walk_left = [ 
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

player_anim_count = 0 # переменная для смены кадров ванимации

bg_x = 0 # для переменщения фона


running = True
while running:
    screen.blit(bg, (bg_x,0))
    
    if player_anim_count==4: player_anim_count=0
    if bg_x==-620: bg_x=0 # если смещение вышло за предлы второго фона, обнуляем его
    
    screen.blit(walk_right[player_anim_count], (player_x,player_y))
    
    keys = pygame.key.get_pressed() # кнопка, на которую сейчас нажимает пользователь
    if keys[pygame.K_LEFT] and player_x>50: 
        screen.blit(walk_left[player_anim_count], (player_x,player_y))
        player_x -=player_speed
        player_anim_count+=1
    if keys[pygame.K_RIGHT] and player_x<200: 
        screen.blit(walk_right[player_anim_count], (player_x,player_y))
        player_x +=player_speed
        player_anim_count+=1
    
    
    # логика на прыжок
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