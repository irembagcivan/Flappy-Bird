import pygame
from pygame.locals import *

pygame.init()

clock= pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird")

# Define game variables
ground_scroll = 0 
scroll_speed = 4 

# Load images
bg = pygame.image.load("img/bg.png")
ground_img = pygame.image.load("img/ground.png")

# Game loop 
run = True 
while run:

    clock.tick(fps)

    # draw background
    screen.blit(bg, (0,0))

    #draw and scroll the ground
    screen.blit(ground_img, (ground_scroll,668))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 40:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

