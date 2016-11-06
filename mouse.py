import pygame, sys
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

mousex = 0
mousey = 0
mouseMoved = False

pygame.init()
screen = pygame.display.set_mode((200, 180), 0, 32)
pygame.display.set_caption('Mouse test')

box = pygame.Surface((32, 32))
box.fill(RED)


screen.blit(box, (84, 74))
pygame.display.update()


def check_mouse(x, y):
    box_rect = pygame.Rect(84, 74, 32, 32)
    if box_rect.collidepoint(x, y):
        print 'Inside the box'

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            mouseMoved = True
    
    if mouseMoved:
        check_mouse(mousex, mousey)
        mouseMoved = False

    clock.tick(30)
