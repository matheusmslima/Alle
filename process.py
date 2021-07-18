import pygame, sys, classes, random


def process(nave, FPS, total_frames, pontos):

    #PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                classes.NaveProjectile.fire = not classes.NaveProjectile.fire
    keys = pygame.key.get_pressed()

    # i = 0
    # two_seconds = FPS * 2
    # if total_frames % two_seconds == 0:
    # 	i = 1


    if keys[pygame.K_d]:
        classes.Nave.going_right = True
        nave.vely = 0
        nave.velx = 3
        nave.image = pygame.image.load("images/nave42right1.png")
    elif keys[pygame.K_a]:
        classes.Nave.going_right = False
        nave.vely = 0
        nave.velx = -3
        nave.image = pygame.image.load("images/nave42left1.png")
    elif keys[pygame.K_w]:
        classes.Nave.going_up = True
        nave.velx = 0
        nave.vely = -3
        nave.image = pygame.image.load("images/nave42up1.png")
    elif keys[pygame.K_s]:
        classes.Nave.going_up = False
        nave.velx = 0
        nave.vely = 3
        nave.image = pygame.image.load("images/nave42down1.png")
    else:
        nave.velx = 0
        nave.vely = 0



    if keys[pygame.K_SPACE]:

        def direction():
            if classes.Nave.going_right:
                p.velx = 8
            else:
                p.velx = -8

        if (classes.NaveProjectile.fire):
            p = classes.NaveProjectile(nave.rect.x, nave.rect.y, False, "images/projectile/projok.png")
            direction()
        else:
            p = classes.NaveProjectile(nave.rect.x, nave.rect.y, True, "images/projectile/fireok.png")
            direction()







    # z = classes.NaveProjectile(nave.rect.x, nave.rect.y, "images/projectile/proj3.png")
    #
    #
    # elif classes.Nave.going_up:
    # 	p.vely = -8
    # elif not:
    # 	p.vely = 8
    # if keys[pygame.K_ENTER]:
    # 	p = classes.NaveProjectile(nave.rect.x, nave.rect.y, "images/projectile/projok.png")

    # 	if classes.Nave.going_up:
    # 		p.vely = -8
    # 	else:
    # 		#p.image = pygame.transform.flip(p.image, True, False)
    # 		p.vely = 8



    def spawn(FPS, total_frames):
        four_seconds = FPS * 4
        if total_frames % four_seconds == 0:
            r = random.randint(1, 2)
            x = 1
            if r == 2:
                x = 640 - 40
            alien = classes.Alien(x, 130, "images/alienok.png")

    #PROCESSING

    def collissions():
        for alien in classes.Alien.List:
            projectiles = pygame.sprite.spritecollide(alien, classes.NaveProjectile.List, True)
            for projectile in projectiles:
                alien.velx = 0
                alien.health = 0
                if projectile.if_this_variable_is_true_then_fire:
                    alien.image = pygame.image.load("images/alienokfire.png")
                else:
                    if alien.velx > 0:
                        alien.image = pygame.image.load("images/alienokfrozen.png")
                    elif alien.vely < 0:
                        alien.image = pygame.image.load("images/alienokfrozen.png")
                        alien.image = pygame.transform.flip(alien.image, True, False)#("images/alienokfrozen.png")



        # for alien in classes.Alien.List:
        # 	if pygame.sprite.spritecollide(alien, classes.NaveProjectile.List, False):
        # 		if classes.NaveProjectile.fire:
        # 			alien.health -= alien.half_health
        # 		else:
        # 			alien.velx = 0
        # 			# alien.image =


        # for proj in classes.NaveProjectile.List:
        # 	if pygame.sprite.spritecollide(proj, classes.Alien.List, False):
        # 		proj.rect.x = 2 * -proj.rect.width
        # 		proj.destroy()

        # for alien in classes.Alien.List:
        # 	alien_proj = pygame.sprite.spritecollide(alien, classes.NaveProjectile.List, True)
        # 	if len(alien_proj) > 0:
        # 		for hit in alien_proj:
        # 			alien.health -= alien.half_health

        # pygame.sprite.groupcollide(G1, G2, dokill, dokill)
    spawn(FPS, total_frames)
    collissions()
