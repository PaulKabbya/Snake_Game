#Snake game
import pygame as py
from random import randrange

WINDOW = 800
TILE_SIZE = 40
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
rand_pos = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = py.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = rand_pos()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, step_time = 0, 110
food = snake.copy()
food.center = rand_pos()
screen = py.display.set_mode([WINDOW]*2)
clock = py.time.Clock()
directions = {py.K_w: True, py.K_s: True, py.K_a: True, py.K_d: True}

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                exit()
            if event.key == py.K_w and directions[py.K_w]:
                snake_dir = (0, -TILE_SIZE)
                directions = {py.K_w: True, py.K_s: False, py.K_a: True, py.K_d: True}
            if event.key == py.K_s and directions[py.K_s]:
                snake_dir = (0, TILE_SIZE)
                directions = {py.K_w: False, py.K_s: True, py.K_a: True, py.K_d: True}
            if event.key == py.K_a and directions[py.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                directions = {py.K_w: True, py.K_s: True, py.K_a: True, py.K_d: False}
            if event.key == py.K_d and directions[py.K_d]:
                snake_dir = (TILE_SIZE, 0)
                directions = {py.K_w: True, py.K_s: True, py.K_a: False, py.K_d: True}
            if event.key == py.K_UP and directions[py.K_w]:
                snake_dir = (0, -TILE_SIZE)
                directions = {py.K_w: True, py.K_s: False, py.K_a: True, py.K_d: True}
            if event.key == py.K_DOWN and directions[py.K_s]:
                snake_dir = (0, TILE_SIZE)
                directions = {py.K_w: False, py.K_s: True, py.K_a: True, py.K_d: True}
            if event.key == py.K_LEFT and directions[py.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                directions = {py.K_w: True, py.K_s: True, py.K_a: True, py.K_d: False}
            if event.key == py.K_RIGHT and directions[py.K_d]:
                snake_dir = (TILE_SIZE, 0)
                directions = {py.K_w: True, py.K_s: True, py.K_a: False, py.K_d: True}

    screen.fill('black')
    #Border patrol and overlap
    overlap = py.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or overlap:
        snake.center, food.center = rand_pos(), rand_pos()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]
    #Eat food
    if snake.center == food.center:
        food.center = rand_pos()
        length+=1
    #Food spawn
    py.draw.rect(screen, 'red', food)
    #Start the snake
    [py.draw.rect(screen, 'green', segment) for segment in segments]
    #Move the snake
    current_time = py.time.get_ticks()
    if current_time - time > step_time:
        time = current_time
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    py.display.flip()
    clock.tick(60)