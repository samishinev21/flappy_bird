import pygame
import pgzero
import os
import random
import pgzrun
from mako.compat import jython

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

game_stop = False

PIPE_GAP = 750
PIPE_SPEED_ORIGIN = 5
PIPE_INTERVAL = 400
PIPE_COUNT = 2

PIPE_SCORE = 0

BIRD_SPEED_UP = 15
BIRD_SPEED_DOWN = 7

current_frame = 0
frame_count = 0
frame_interval = 10

pipes = []
pipe_timer = 0

def set_fullscreen():
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def get_WIDTH_and_HEIGHT():
    info = pygame.display.Info()
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = info.current_w, info.current_h

set_fullscreen()
get_WIDTH_and_HEIGHT()

bird_up = pygame.image.load('images/flappy_bird_up.png')
scaled_bird_up = pygame.transform.scale(bird_up, (125, 125))
pygame.image.save(scaled_bird_up, 'images/flappy_bird_up.png')

bird_up = Actor("flappy_bird_up")
bird_up.pos = WIDTH / 2 - 700, HEIGHT / 2 - 300


bird_down = pygame.image.load('images/flappy_bird_down.png')
scaled_bird_down = pygame.transform.scale(bird_down, (125, 125))
pygame.image.save(scaled_bird_down, 'images/flappy_bird_down.png')

bird_down = Actor("flappy_bird_down")
bird_down.pos = WIDTH / 2 - 700, HEIGHT / 2 - 300

pipe_down = pygame.image.load('images/pipe_down.png')
scaled_pipe_down = pygame.transform.scale(pipe_down, (100, 750))
pygame.image.save(scaled_pipe_down, 'images/pipe_down.png')

pipe_up = pygame.image.load('images/pipe_up.png')
scaled_pipe_up = pygame.transform.scale(pipe_up, (100, 700))
pygame.image.save(scaled_pipe_up, 'images/pipe_up.png')

def add_pipes():
    pipe_height = random.randint(0, HEIGHT - PIPE_GAP)
    top_pipe = Actor("pipe_up", (WIDTH, pipe_height - 250))
    bottom_pipe = Actor("pipe_down", (WIDTH, pipe_height + PIPE_GAP + 110))
    pipes.append((top_pipe, bottom_pipe))

add_pipes()

def recycle_pipe(pipe_pair):
    if not game_stop:
        pipe_height = random.randint(0, HEIGHT - PIPE_GAP)
        top_pipe, bottom_pipe = pipe_pair
        top_pipe.pos = (WIDTH, pipe_height - 250)
        bottom_pipe.pos = (WIDTH, pipe_height + PIPE_GAP + 110)

def check_collision():
    global game_stop
    if not game_stop:
        bird = bird_up if current_frame == 0 else bird_down

        for top_pipe, bottom_pipe in pipes:
            if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):

                game_stop = True

def update():
    if not game_stop:
        global frame_count, current_frame, pipe_timer
        frame_count += 1
        pipe_timer += 1

        if keyboard.space:
            bird_up.y -= BIRD_SPEED_UP
            bird_down.y -= BIRD_SPEED_UP

            if bird_up.angle <= 50 and bird_down.angle <= 50:
                bird_up.angle += 5
                bird_down.angle += 5
        else:
            bird_up.angle = -30
            bird_down.angle = -30

        bird_up.y += BIRD_SPEED_DOWN
        bird_down.y += BIRD_SPEED_DOWN

        if frame_count >= frame_interval:
            frame_count = 0
            current_frame = 1 - current_frame

        for top_pipe, bottom_pipe in pipes:
            top_pipe.x -= PIPE_SPEED_ORIGIN
            bottom_pipe.x -= PIPE_SPEED_ORIGIN

            if top_pipe.right < 0:
                recycle_pipe((top_pipe, bottom_pipe))

        check_collision()

        if len(pipes) > 0 and pipes[0][0].x < -100:
            pipes.pop(0)

        if pipe_timer >= PIPE_INTERVAL:
            pipe_timer = 10


def draw():
    if not game_stop:
        screen.blit("background", (0, 0))

        if current_frame == 0:
            bird_up.draw()
        else:
            bird_down.draw()

        for top_pipe, bottom_pipe in pipes:
            top_pipe.draw()
            bottom_pipe.draw()

pgzrun.go()