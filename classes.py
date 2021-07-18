from math import sin
from pygame import image, sprite
from random import randint


class BaseClass(sprite.Sprite):
    allsprites = sprite.Group()

    def __init__(self, x, y, image_string):
        sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)

        self.image = image.load(image_string)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def destroy(self, ClassName):
        ClassName.List.remove(self)
        BaseClass.allsprites.remove(self)
        del self


class Nave(BaseClass):
    List = sprite.Group()
    going_right = True
    going_up = True

    def __init__(self, x, y, image_string):

        BaseClass.__init__(self, x, y, image_string)
        Nave.List.add(self)
        self.velx = 0
        self.vely = 0

    def motion(self, SCREENWIDTH, SCREENHEIGHT):
        predicted_location_x = self.rect.x + self.velx
        predicted_location_y = self.rect.y + self.vely

        if predicted_location_x < 0:
            self.velx = 0
        elif predicted_location_x + self.rect.width > SCREENWIDTH:
            self.velx = 0

        if predicted_location_y < 0:
            self.vely = 0
        elif predicted_location_y + self.rect.width > SCREENHEIGHT:
            self.vely = 0

        self.rect.x += self.velx
        self.rect.y += self.vely


class Alien(BaseClass):
    List = sprite.Group()

    def __init__(self, x, y, image_string):
        BaseClass.__init__(self, x, y, image_string)
        Alien.List.add(self)
        self.health = 150
        self.half_health = 50
        self.velx, self.vely = randint(1, 2), 2
        self.amplitude, self.period = randint(20, 140), randint(3, 4) / 100.0

    @staticmethod
    def update_all(SCREENWIDTH, SCREENHEIGHT):
        for alien in Alien.List:
            if alien.health <= 0:
                # if alien.rect.y + alien.rect.height < SCREENHEIGHT:
                # 	alien.rect.y += alien.vely
                # if alien.rect.y + alien.rect.height == SCREENHEIGHT:
                alien = alien.destroy(alien)
            else:
                alien.alien(SCREENWIDTH, SCREENHEIGHT)
            # if alien.health <= 0:
            # 	alien.destroy(Alien)

    def alien(self, SCREENWIDTH, SCREENHEIGHT):
        if self.rect.x + self.rect.width > SCREENWIDTH or self.rect.x < 0:
            self.velx = -self.velx

        self.rect.x += self.velx
        # a * sin (bx + c) + y
        self.rect.y = self.amplitude * sin(self.period * self.rect.x) + 140

    # @staticmethod
    # def movement(SCREENWIDTH, SCREENHEIGHT):
    # 	for alien in Alien.List:
    # 		alien.alien(SCREENWIDTH, SCREENHEIGHT)


class NaveProjectile(sprite.Sprite):
    List = sprite.Group()
    normal_list = []
    normal_listy = []
    fire = True

    def __init__(self, x, y, if_this_variable_is_true_then_fire, image_string):

        sprite.Sprite.__init__(self)
        self.image = image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.if_this_variable_is_true_then_fire = if_this_variable_is_true_then_fire

        try:
            last_element = NaveProjectile.normal_list[-1]
            difference = abs(self.rect.x - last_element.rect.x)
            if difference < self.rect.width:
                return
        except:
            pass

        NaveProjectile.normal_list.append(self)
        NaveProjectile.List.add(self)
        self.velx = 0
        self.vely = 0

    @staticmethod
    def movement():
        for projectile in NaveProjectile.List:
            projectile.rect.x += projectile.velx
            projectile.rect.y += projectile.vely

    def destroy(self):
        NaveProjectile.List.remove(self)
        NaveProjectile.normal_list.remove(self)
        del self






        # try:
        # 	#last_element = NaveProjectile.normal_list[-1]
        # 	last_element = NaveProjectile.normal_listy[-1]

        # 	differencey = abs(self.rect.y - last_element.rect.y)
        # 	#differencey = abs(self.rect.y - last_element.rect.y)
        # 	#if differencex < self.rect.width:
        # 	#	return
        # 	if differencey < self.rect.height:
        # 	 	return

        # except:
        # 	pass
