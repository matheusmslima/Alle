import pygame, sys, random
from random import randint
from classes import *
from process import process

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("FromHere.ogg")
pygame.mixer.music.play()
pygame.init()

SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
FPS = 60
total_frames = 0
points = 0
pontos = 0
background = pygame.image.load("images/mapas/mapa" + str(random.randrange(1,10)) + "ok.png")
nave = Nave(randint(0,SCREENWIDTH-55), randint(0,SCREENHEIGHT-55), "images/nave42right1.png")

# alien  = Alien(randint(0,SCREENWIDTH-55), randint(0,SCREENHEIGHT-55), 40, 40, "images/alienok.png")
# alien1 = Alien(randint(0,SCREENWIDTH-55), randint(0,SCREENHEIGHT-55), 40, 40, "images/alienok.png")
# alien2 = Alien(randint(0,SCREENWIDTH-55), randint(0,SCREENHEIGHT-55), 40, 40, "images/alienok.png")
# alien3 = Alien(randint(0,SCREENWIDTH-55), randint(0,SCREENHEIGHT-55), 40, 40, "images/alienok.png")
# alien4 = Alien(randint(0,SCREENWIDTH-55), randint(0,SCREENHEIGHT-55), 40, 40, "images/alienok.png") 

#heart = pygame.image.load("images/heart.gif")

# -------------- Main Program Loop -----------------#

while True:
    process(nave, FPS, total_frames, pontos)
    nave.motion(SCREENWIDTH, SCREENHEIGHT)
    Alien.update_all(SCREENWIDTH, SCREENHEIGHT)
    NaveProjectile.movement()
    total_frames += 1


    #draw

        #RGB
    #screen.fill((255,255,255))
    #print(classes.Alien.cont)
    screen.blit(background, (0,0))
    #screen.blit(, (100,100))

    BaseClass.allsprites.draw(screen)
    NaveProjectile.List.draw(screen)
    #pygame.draw.rect(screen, (255, 255, 255), (5,5,50,25))
    pygame.display.flip()
    #draw

    clock.tick(FPS)










#brilho = pygame.draw.circle(screen, (0,255,0), (100,100), 5, 5)
# i=0
# while True:
# 	i += 8
# 	while i > 255:
# 		i%=255
# 	brilho = pygame.draw.circle(screen, (0,i,0), (100,100), 5, 5)
