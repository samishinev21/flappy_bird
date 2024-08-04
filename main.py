import pygame
import pgzero
import os

import pgzrun

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

WIDTH = 2289  # Scale to 50x50 pixels
HEIGHT = 1148

background = pygame.image.load('images/background.png')
scaled_background = pygame.transform.scale(background, (2289, 1482))
pygame.image.save(scaled_background, 'images/background.png')

bird_up = pygame.image.load('images/flappy_bird_up.png')
scaled_bird_up = pygame.transform.scale(bird_up, (125, 125))
pygame.image.save(scaled_bird_up, 'images/flappy_bird_up.png')

bird_down = pygame.image.load('images/flappy_bird_down.png')
scaled_bird_down = pygame.transform.scale(bird_down, (125, 125))
pygame.image.save(scaled_bird_down, 'images/flappy_bird_down.png')

bird_up = Actor("flappy_bird_up")
bird_up.pos = 150, 500

bird_down = Actor("flappy_bird_down")
bird_down.pos = 150, 500

bird = Actor("flappy_bird_up")

pipes = []


def add_pipes():
    gap_start = random.randint(100, 100)

    pipe_up = Actor("pipe_up")
    pipe_down = Actor("pipe_down")

    top_pipe.pos = WIDTH, gap_start - top_pipe.height // 2
    bottom_pipe.pos = WIDTH, gap_start + GAP + bottom_pipe.height // 2
    pipes.append(pipe_up, pipe_down)


def draw_pipes():
    for pipe_pair in pipes:
        pipe_pair[0].draw()
        pipe_pair[1].draw()


def update_pipes():
    global pipes
    for pipe_pair in pipes:
        pipe_pair[0].x -= 5
        pipe_pair[1].x -= 5
    pipes = [pipe_pair for pipe_pair in pipes if pipe_pair[0].right > 0]


def update():
    if keyboard.space:
        bird.y -= 5
    bird.y += 3
    update_pipes()


def draw():
    screen.blit("background", (0, 0))
    bird.draw()


pgzrun.go()
