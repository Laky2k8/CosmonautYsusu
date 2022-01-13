import pygame
import os
import pygame.display

WIDTH = 900
HEIGHT = 500


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 60
VEL = 5

SPACESHIP_W = 100
SPACESHIP_H = 80

ship1_img = pygame.image.load(os.path.join('Assets', 'ship1.png'))
ship2_img = pygame.image.load(os.path.join('Assets', 'ship2.png'))
bg = pygame.image.load(os.path.join('Assets', 'bg.jpg'))

ship1_translImg = pygame.transform.scale(ship1_img, (SPACESHIP_W, SPACESHIP_H))
ship1_translImg = pygame.transform.rotate(ship1_translImg, 270)

ship2_translImg = pygame.transform.scale(ship2_img, (SPACESHIP_W, SPACESHIP_H))
ship2_translImg = pygame.transform.rotate(ship2_translImg, 90)

ship1_x = 100
ship1_y = 300

ship2_x = 700
ship2_y = 300

running = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Cosmonaut: YSusu")

ship1 = pygame.Rect(ship1_x,ship1_y, SPACESHIP_W, SPACESHIP_H)
ship2 = pygame.Rect(ship2_x,ship2_y, SPACESHIP_W, SPACESHIP_H)



def ship_control(keys_pressed, ship):
    if keys_pressed[pygame.K_a]:
        ship.x -= VEL
    if keys_pressed[pygame.K_d]:
        ship.x += VEL

    if keys_pressed[pygame.K_w]:
        ship.y -= VEL
    if keys_pressed[pygame.K_s]:
        ship.y += VEL

def drawShips():
    screen.blit(ship1_translImg, ship1)
    screen.blit(ship2_translImg, ship2)

def drawWin():
    screen.fill(BLACK)
    screen.blit(bg, (0,0))
    drawShips()

    pygame.display.update()
    pygame.display.flip()

def main():


    clock = pygame.time.Clock()
    global running
    global screen


    while (running):

        clock.tick(FPS)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0

        keys = pygame.key.get_pressed()

        ship_control(keys, ship1)

        drawWin()




if __name__ == "__main__":
    main()