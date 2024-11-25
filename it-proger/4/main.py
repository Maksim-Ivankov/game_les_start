# ФОН ИДЕТ ВПЕРЕД И ИГРАЕТ МУЗЫКА

import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618,359)) 


bg = pygame.image.load('images/bg.png')
walk_left = [ 
    pygame.image.load('images/player_left/1.png'),
    pygame.image.load('images/player_left/2.png'),
    pygame.image.load('images/player_left/3.png'),
    pygame.image.load('images/player_left/4.png'),
]
walk_right = [
    pygame.image.load('images/player_right/1.png'),
    pygame.image.load('images/player_right/2.png'),
    pygame.image.load('images/player_right/3.png'),
    pygame.image.load('images/player_right/4.png'),
]

player_anim_count = 0 # переменная для смены кадров ванимации

bg_x = 0 # для переменщения фона

bg_sound = pygame.mixer.Sound('sound/bg.mp3')
bg_sound.play(-1) # подрубаем музыку на фон

running = True
while running:
    bg_x-=10 # смещаем фон
    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x+618,0)) # второй задний фон за первым
    screen.blit(walk_right[player_anim_count], (300,250))
    player_anim_count+=1
    if player_anim_count==4: player_anim_count=0
    if bg_x==-620: bg_x=0 # если смещение вышло за предлы второго фона, обнуляем его
    
    
   
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            running = False 
    clock.tick(10)