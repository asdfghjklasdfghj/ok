# -*- coding: utf-8 -*-
from uagame import Window



#import modules

import pygame

import random

import time

from time import sleep

def collision_with_snake(snake_head):
    #if snake runs into itself restart the game
    if snake_head in snake_position[1:]: 
        return 1
    else:
        return 0

def collision_with_boundaries(snake_head):
    

    # if snake is outside of boundaries restart the game
    if snake_head[0] >= display_width or snake_head[0] < 0 or snake_head[1] >= display_height or snake_head[1] < 0:
        return 1
    else:
        return 0
def generate_snake(snake_head, snake_position, button_direction):
    
    #uses button_direction to decide where snake head will go
    if button_direction == 1:
        snake_head[0] += 10
        snake_end[0] += 10
    elif button_direction == 0:
        snake_head[0] -= 10
        snake_end[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
        snake_end[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10   
        snake_end[1] -= 10
        
    snake_position.insert(0,list(snake_head))
    snake_position.pop()
    
    return snake_position

def display_snake(snake_position):

    #uses list of snake's positions to display snake
    for position in snake_position:
        pygame.draw.rect(display, player_color, pygame.Rect(position[0], position[1], 10, 10))

def play_game(snake_head, snake_position, button_direction):
    score = 0    
    crashed = False
    cancel = 0
    y = random.randint(1, 48)*10
    x = random.randint(1, 48)*10
    while crashed is not True:
        
        for event in pygame.event.get():

            #ends game if you click on X
            if event.type == pygame.QUIT:
                crashed = True
            #sets variable used to move snake using arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if button_direction == 1:
                        button_direction = 1
                    else:
                        button_direction = 0                    
                elif event.key == pygame.K_RIGHT:
                    if button_direction == 0:
                        button_direction = 0
                    else:
                        button_direction = 1
                elif event.key == pygame.K_UP:
                    if button_direction == 2:
                        button_direction = 2
                    else:                    
                        button_direction = 3
                elif event.key == pygame.K_DOWN:
                    if button_direction == 3:
                        button_direction = 3
                    else:                    
                        button_direction = 2
        if snake_head[0] == x and snake_head[1]  == y:
            y = random.randint(1, 48)*10
            x = random.randint(1, 48)*10    
            pygame.draw.rect(display, item_color, pygame.Rect(x, y, 10, 10))
            score += 10
            
            snake_position.append(snake_end)
            snake_position.append(snake_end)
            
        else:
            pygame.draw.rect(display, item_color, pygame.Rect(x, y, 10, 10))        
        #moves snake position
        snake_position = generate_snake(snake_head, snake_position, button_direction)
    
        
        

       
            
        #display background and snake and rectangle
        display.fill(window_color)
        if cancel == 0:
            display_snake(snake_position)
            pygame.draw.rect(display, item_color, pygame.Rect(x, y, 10, 10))
            window.draw_string("Score: " + str(score), 0, 0)
            pygame.display.update()
        

        #ends game loop if snake leaves the boundary
        if collision_with_boundaries(snake_head) == 1:
            cancel = 1
            window.clear()        
            window.set_font_size(30)
            window.set_font_color("red")
            window.draw_string("GAME OVER", 170, 200)
            window.set_font_size(20)
            window.draw_string("Final Score: " + str(score), 170, 240)
            window.set_font_color("white")
            window.set_font_size(15)
            window.draw_string("press the spacebar to quit", 150, 260)
            window.update()
            for key in pygame.event.get():
                if key.type == pygame.KEYDOWN:
                    if key.key == pygame.K_SPACE:
                        crashed = True 
        if collision_with_snake(snake_head) == 1:
            cancel = 1
            window.clear()
            window.set_font_size(30)
            window.set_font_color("red")
            window.draw_string("GAME OVER", 170, 200)
            window.set_font_size(20)
            window.draw_string("Final Score: " + str(score), 170, 240)            
            window.set_font_color("white")
            window.set_font_size(15)
            window.draw_string("press the spacebar to quit", 150, 260)
            window.update()
            for key in pygame.event.get(): 
                if key.type == pygame.KEYDOWN:
                    if key.key == pygame.K_SPACE:
                        crashed = True                  
        clock.tick(20)



if __name__ == "__main__":

    # set variables

    display_width = 500

    display_height = 500

    player_color = (0,255, 50)

    item_color = (255, 0, 0)

    window_color = (0,0,0)

    clock=pygame.time.Clock()

    display = pygame.display.set_mode((display_width,display_height))

    #create the snake

    snake_head = [250,250]
    
    snake_end = [230, 250]
    
    snake_position = [[250,250],[240,250],[230,250]]


    #initialize pygame modules    

    pygame.init()

    

    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game")
    
    pygame.display.update()

    window = Window('Snake Game', 500, 500)
    window.set_font_color("white")
    window.set_font_name("couriernew")
    window.set_font_size(18)   

    #start the game loop

    play_game(snake_head, snake_position, 1)



    pygame.quit()