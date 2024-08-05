import pygame
import pgzero
import os

import pgzrun

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

current_frame = 0
frame_count = 0
frame_interval = 15

background = pygame.image.load('images/background.png')
scaled_background = pygame.transform.scale(background, (2289, 1482))
pygame.image.save(scaled_background, 'images/background.png')

bird_up = pygame.image.load('images/flappy_bird_up.png')
scaled_bird_up = pygame.transform.scale(bird_up, (125, 125))
pygame.image.save(scaled_bird_up, 'images/flappy_bird_up.png')

bird_down = pygame.image.load('images/flappy_bird_down.png')
scaled_bird_down = pygame.transform.scale(bird_down, (125, 125))
pygame.image.save(scaled_bird_down, 'images/flappy_bird_down.png')


def set_fullscreen():
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def get_WIDTH_and_HEIGHT():
    info = pygame.display.Info()

    global WIDTH, HEIGHT
    WIDTH, HEIGHT = info.current_w, info.current_h

    print(f"{WIDTH} {HEIGHT}")


set_fullscreen()
get_WIDTH_and_HEIGHT()

bird_up = Actor("flappy_bird_up")
bird_up.pos = WIDTH / 2 - 700, HEIGHT / 2 - 300
bird_down = Actor("flappy_bird_down")
bird_down.pos = WIDTH / 2 - 700, HEIGHT / 2 - 300


def add_pipe():
    pass


def update():
    global frame_count, current_frame
    frame_count += 1
    if keyboard.space:
        bird_up.y -= 10
        bird_down.y -= 10

        if bird_up.angle <= 50 and bird_down.angle <= 50:
            bird_up.angle += 5
            bird_down.angle += 5
    else:
        bird_up.angle = -30
        bird_down.angle = -30

    bird_up.y += 5
    bird_down.y += 5

    if frame_count >= frame_interval:
        frame_count = 0
        current_frame = 1 - current_frame


def draw():
    screen.blit("background", (0, 0))

    if current_frame == 0:
        bird_up.draw()
    else:
        bird_down.draw()


pgzrun.go()
