# добавляем стрельбу

import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618,359)) 

player_speed = 5
player_x = 150 
player_y = 250 

is_jump = False
jump_count = 7

gameplay = True 

bg = pygame.image.load('images/bg.png').convert()

ghost = pygame.image.load('images/prizrak.png').convert_alpha()
ghost_x = 620


label = pygame.font.Font('fonts/ofont.ru_Roboto.ttf',40)
lose_label = label.render('Вы проиграли!', False, (193,196,199))
restart_label = label.render('Вернуться и отомстить', False, (115,132,148))
restart_label_rect = restart_label.get_rect(topleft=(110,200))

# делаем снаряд
bulet = pygame.image.load('images/paintball.png').convert_alpha()
bulet = pygame.transform.scale(bulet,(20,20))
bulets = []


ghost_list_in_game = [] 

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer,4000)

walk_left = [ 
    pygame.image.load('images/player_left/1.png').convert_alpha(),
    pygame.image.load('images/player_left/2.png').convert_alpha(),
    pygame.image.load('images/player_left/3.png').convert_alpha(),
    pygame.image.load('images/player_left/4.png').convert_alpha(),
]
walk_right = [
    pygame.image.load('images/player_right/1.png').convert_alpha(),
    pygame.image.load('images/player_right/2.png').convert_alpha(),
    pygame.image.load('images/player_right/3.png').convert_alpha(),
    pygame.image.load('images/player_right/4.png').convert_alpha(),
]
player_anim_count = 0 
bg_x = 0 


running = True
while running:

    screen.blit(bg, (bg_x,0))
   
    if gameplay: 
        player_rect = walk_left[0].get_rect(topleft=(player_x,player_y))

        if ghost_list_in_game:
            for (i,el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x-=10
                

                if el.x < -10: ghost_list_in_game.pop(i)
        
                if player_rect.colliderect(el): 
                    gameplay = False
        
        
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
        
        # делаем логику на выстрел
        if keys[pygame.K_b]:
            bulets.append(bulet.get_rect(topleft=(player_x+30,player_y+20))) # вместо добавления картинки всегда добавляем ее хитбокс
        # отрисовка выстрела
        if bulets: # если список не пустой
            for (i,el) in enumerate(bulets):
                # отрисовывыаем снаряд и он летит
                screen.blit(bulet,(el.x,el.y))
                el.x+=4
        #         # отччстка при выходе за пределы
                if el.x>630:bulets.pop(i)
        #         # логика на попадание в призрак
                if ghost_list_in_game:
                    for(index,ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            bulets.pop(i)

            
        
    else: 
        screen.fill((87,88,89))
        screen.blit(lose_label, (180,100)) 
        screen.blit(restart_label, restart_label_rect) 
    
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0 ]:
            gameplay = True
            ghost_list_in_game[:] = []
            bulets[:] = [] # отчищаем снаряды при перезапуске
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            running = False 
        if event.type == ghost_timer:   
            ghost_list_in_game.append(ghost.get_rect(topleft=(620,250)))
            
            
            
            
    clock.tick(10)