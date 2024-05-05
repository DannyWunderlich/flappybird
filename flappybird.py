import pygame
import random
from sys import exit

#TODO: FIX BIRD GRAVITY, ADD SCORE, ADD END GAME SCREEN WHEN YOU DIE, PREVENT BIRD FROM LEAVING SCREEN, ADD SOUND, THEN DO WHATEVER

WIDTH = 288
HEIGHT = 512
PIPE_GAP = 115
BIRD_START_POS = (65,170)

started = False
waiting = True
gravity = 0

def tap_to_start():
    screen.blit(background_surface, (0,0))
    screen.blit(ground_surface_1, ground_rect_1)
    screen.blit(ground_surface_2, ground_rect_2)
    screen.blit(bird_surface,bird_rect)
    screen.blit(start_surface, start_rect)
    ground_motion()

def ground_motion():
     ground_rect_1.left -= 2
     if ground_rect_1.right <= 0:
        ground_rect_1.left = ground_rect_2.right - 2
     ground_rect_2.left -= 2
     if ground_rect_2.right <= 0:
        ground_rect_2.left = ground_rect_1.right - 2

def pipe_reset():
    top_of_bottom = random.randint(165, 350) 
    return top_of_bottom

def pipe_motion():
    pipe_rect_1_bottom.left -= 2
    if pipe_rect_1_bottom.right <= 0:
        pipe_rect_1_bottom.left = pipe_rect_3_bottom.right + 115
        pipe_rect_1_bottom.top = pipe_reset()
    pipe_rect_1_top.left -= 2
    if pipe_rect_1_top.right <= 0:
        pipe_rect_1_top.left = pipe_rect_3_top.right + 115
        pipe_rect_1_top.bottom = pipe_rect_1_bottom.top - 115
    pipe_rect_2_bottom.left -= 2
    if pipe_rect_2_bottom.right <= 0:
        pipe_rect_2_bottom.left = pipe_rect_1_bottom.right + 115
        pipe_rect_2_bottom.top = pipe_reset()
    pipe_rect_2_top.left -= 2
    if pipe_rect_2_top.right <= 0:
        pipe_rect_2_top.left = pipe_rect_1_top.right + 115
        pipe_rect_2_top.bottom = pipe_rect_2_bottom.top - 115
    pipe_rect_3_bottom.left -= 2
    if pipe_rect_3_bottom.right <= 0:
        pipe_rect_3_bottom.left = pipe_rect_2_bottom.right + 115
        pipe_rect_3_bottom.top = pipe_reset()
    pipe_rect_3_top.left -= 2
    if pipe_rect_3_top.right <= 0:
        pipe_rect_3_top.left = pipe_rect_2_top.right + 115
        pipe_rect_3_top.bottom = pipe_rect_3_bottom.top - 115

def bird_motion():
    global gravity
    if gravity < 5:
        gravity += 1
    bird_rect.bottom += 1 + gravity
    if gravity > 0:
        screen.blit(pygame.transform.rotate(bird_surface,-45), bird_rect)
    elif gravity == 0:
        screen.blit(bird_surface, bird_rect)
    elif gravity < 0:
        screen.blit(pygame.transform.rotate(bird_surface,45), bird_rect)

def check_collision():
    rects = [pipe_rect_1_bottom,pipe_rect_2_bottom,pipe_rect_3_bottom,pipe_rect_1_top,pipe_rect_2_top,pipe_rect_3_top]
    if bird_rect.collideobjects(rects) != (None):
        print("Collision")
    else:
        print("No Collision")


pygame.init() #Essential when using Pygame, don't worry about what it does.
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

pipe_1_bottom_start = pipe_reset()
pipe_2_bottom_start = pipe_reset()
pipe_3_bottom_start = pipe_reset()

bird_y_start = 170

background_surface = pygame.image.load('assets/background-night.png').convert_alpha()
ground_surface_1 = pygame.image.load('assets/base.png').convert_alpha()
ground_surface_2 = pygame.image.load('assets/base.png').convert_alpha()
bird_surface = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()
pipe_surface_1_bottom = pygame.image.load('assets/pipe-red.png').convert_alpha()
pipe_surface_1_top = pygame.image.load('assets/pipe-red.png').convert_alpha()
pipe_surface_1_top = pygame.transform.rotate(pipe_surface_1_top,180)
pipe_surface_2_bottom = pygame.image.load('assets/pipe-red.png').convert_alpha()
pipe_surface_2_top = pygame.image.load('assets/pipe-red.png').convert_alpha()
pipe_surface_2_top = pygame.transform.rotate(pipe_surface_2_top,180)
pipe_surface_3_bottom = pygame.image.load('assets/pipe-red.png').convert_alpha()
pipe_surface_3_top = pygame.image.load('assets/pipe-red.png').convert_alpha()
pipe_surface_3_top = pygame.transform.rotate(pipe_surface_3_top,180)
start_surface = pygame.image.load('assets/message.png').convert_alpha()

bird_rect = bird_surface.get_rect(topleft = BIRD_START_POS)
ground_rect_1 = ground_surface_1.get_rect(topleft = (0,400))
ground_rect_2 = ground_surface_2.get_rect(topleft = (336,400))
pipe_rect_1_bottom = pipe_surface_1_bottom.get_rect(topright = (350,pipe_1_bottom_start))
pipe_rect_1_top = pipe_surface_1_top.get_rect(bottomright = (350,pipe_1_bottom_start - PIPE_GAP))  #PIPE GAP IS 115 PIXELS // DISTANCE BETWEEN EACH PIPE IS
pipe_rect_2_bottom = pipe_surface_2_bottom.get_rect(topleft = (465,pipe_2_bottom_start))
pipe_rect_2_top = pipe_surface_2_top.get_rect(bottomleft = (465, pipe_2_bottom_start - PIPE_GAP))
pipe_rect_3_bottom = pipe_surface_1_bottom.get_rect(topleft = (632,pipe_3_bottom_start))
pipe_rect_3_top = pipe_surface_1_top.get_rect(bottomleft = (632,pipe_3_bottom_start - PIPE_GAP))
start_rect = start_surface.get_rect(center = (WIDTH / 2, HEIGHT / 2))

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and waiting == True:
                waiting = False
                started = True
            elif event.key == pygame.K_SPACE and started == True:
                gravity = -10
                bird_rect.bottom -= 13

    if waiting:
        tap_to_start()

    if started:   
        screen.blit(background_surface, (0,0))
        screen.blit(pipe_surface_1_bottom, pipe_rect_1_bottom)
        screen.blit(pipe_surface_1_top, pipe_rect_1_top)
        screen.blit(pipe_surface_2_bottom, pipe_rect_2_bottom)
        screen.blit(pipe_surface_2_top, pipe_rect_2_top)
        screen.blit(pipe_surface_3_bottom, pipe_rect_3_bottom)
        screen.blit(pipe_surface_3_top, pipe_rect_3_top)
        screen.blit(ground_surface_1, ground_rect_1)
        screen.blit(ground_surface_2, ground_rect_2)
        bird_motion()
        check_collision()

        ground_motion()
        if bird_rect.bottom >= 400:
            started = False
            waiting = True
            bird_rect.topleft = BIRD_START_POS
            new_pipe_1_bottom = pipe_reset()
            new_pipe_2_bottom = pipe_reset()
            new_pipe_3_bottom = pipe_reset()
            pipe_rect_1_bottom.topright = (350,new_pipe_1_bottom)
            pipe_rect_1_top.bottomright = (350,new_pipe_1_bottom - PIPE_GAP)
            pipe_rect_2_bottom.topleft = (465,new_pipe_2_bottom)
            pipe_rect_2_top.bottomleft = (465,new_pipe_2_bottom - PIPE_GAP)
            pipe_rect_3_bottom.topleft = (632,new_pipe_3_bottom)
            pipe_rect_3_top.bottomleft = (632,new_pipe_3_bottom - PIPE_GAP)

        pipe_motion()
        

    pygame.display.update()
    clock.tick(60)
