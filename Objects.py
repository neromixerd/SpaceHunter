import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKBLUE = (0, 0, 139)
DARKRED = (176, 16, 48)

def comedelay(time, delay):
    timer = time
    if timer == -1:
        timer += 1
        return timer
    elif timer < delay:
        timer += 1
        return timer
    elif timer >= delay:
        timer = -1
        return timer


class Rating(object):
    def __init__(self, Score, Name):
        self.score = Score
        self.name = Name


class Enemy1(pygame.sprite.Sprite):

    def __init__(self, surface, x, y, hp, group, stat):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surface
        self.hitpoints = hp
        self.iso = pygame.image.load(r"Images\Enemy1.1.jpg")
        self.rect = self.iso.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.add(group)
        self.direction = 'none'
        self.status = stat
        self.score = 0

    def update(self, shoots, ships):
        self.score = 0
        ship = ships
        shoot = shoots
        if self.rect.left == 0:
            self.direction = 'right'
        if self.rect.right == 400:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += 2
        if self.direction == 'left':
            self.rect.x -= 2

        if pygame.sprite.groupcollide(ship, shoot, False, False) != {}:
            if self.hitpoints != 0:
                pygame.sprite.groupcollide(ship, shoot, False, True)
                self.hitpoints -= 50
            elif self.hitpoints <= 0:
                self.rect.x = -50
                self.rect.y = -50
                self.status = 0
                self.score += 100
                pygame.sprite.groupcollide(ship, shoot, True, True)

        self.surf.blit(self.iso, self.rect)

    def recteate(self, x, y, hp, stat, group):
        self.rect = self.iso.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.status = stat
        self.hitpoints = hp
        self.add(group)


class MyShip(pygame.sprite.Sprite):

    def __init__(self, surface, x, y, group, hp):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surface
        self.hitpoints = hp
        self.iso = pygame.image.load(r"Images\Ship.1.jpg")
        self.add(group)
        self.rect = self.iso.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.old_rect = [0, 0]
        self.count = -1
        self.Bcount = -1
        self.boom = [pygame.image.load(r"Images\Boom1.1.jpg"), pygame.image.load(r"Images\Boom2.1.jpg"),
                     pygame.image.load(r"Images\Boom3.1.jpg")]

    def update(self, ships, met, shoots):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 3
        elif keys[pygame.K_d]:
            self.rect.x += 3
        elif keys[pygame.K_w]:
            self.rect.y -= 3
        elif keys[pygame.K_s]:
            self.rect.y += 3
        self.surf.blit(self.iso, self.rect)
        meteors = met
        ship = ships
        if pygame.sprite.groupcollide(ship, meteors, False, False) != {}:
            self.hitpoints -= 50
            pygame.sprite.groupcollide(ship, meteors, False, True)
        if pygame.sprite.groupcollide(ship, shoots, False, False) != {}:
            self.hitpoints -= 100
            pygame.sprite.groupcollide(ship, shoots, False, True)
        if self.hitpoints <= 0:
            if self.old_rect[0] == 0 and self.old_rect[1] == 0:
                self.old_rect[0] = self.rect.x
                self.old_rect[1] = self.rect.y
            self.rect.x = -50
            self.rect.y = -50

            if self.count < 40:
                boom = self.boom[0]
                self.surf.blit(boom, (self.old_rect[0] + 20, self.old_rect[1] + 15))
            elif (self.count >= 40) and (self.count < 160):
                self.Bcount = comedelay(self.Bcount, 40)
                if self.Bcount < 20:
                    boom = self.boom[1]
                    self.surf.blit(boom, (self.old_rect[0], self.old_rect[1]))
                elif (self.Bcount >= 20) and (self.Bcount <= 40):
                    boom = self.boom[2]
                    self.surf.blit(boom, (self.old_rect[0] + 5, self.old_rect[1]))
            self.count += 1


class Shoot1(pygame.sprite.Sprite):

    def __init__(self, surface, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surface
        self.iso = pygame.image.load(r"Images\Shoot1.1.png")
        self.rect = self.iso.get_rect()
        self.add(group)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 4
        if self.rect.y <= 65:
            self.kill()
        self.surf.blit(self.iso, self.rect)


class Shoot2(pygame.sprite.Sprite):

    def __init__(self, surface, rect, group):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surface
        self.iso = pygame.image.load(r"Images\Shoot2.png")
        self.rect = self.iso.get_rect()
        self.add(group)
        self.rect.x = rect[0]
        self.rect.y = rect[1]

    def update(self):
        self.rect.y += 4
        if self.rect.y >= 610:
            self.kill()
        self.surf.blit(self.iso, self.rect)


class Rating_Space(pygame.sprite.Sprite):

    def __init__(self, surface, rect):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surface
        self.iso = pygame.image.load(r"Images\RatingSpace.png")
        self.rect = self.iso.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]


class Menu_Button(pygame.sprite.Sprite):

    def __init__(self, surface, rect):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surface
        self.iso = pygame.image.load(r"Images\MenuButton.png")
        self.rect = self.iso.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]


class meteor(pygame.sprite.Sprite):

    def __init__(self, surface, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surface
        self.count = -1
        self.hitpoints = 50
        self.comet = [pygame.image.load(r"Images\Meteor1.1.jpg"), pygame.image.load(r"Images\Meteor2.1.jpg")]
        self.add(group)
        self.rect = self.comet[0].get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, shoots, mets):
        shoots = shoots
        mets = mets
        self.count = comedelay(self.count, 80)
        if self.count < 40:
            comet = self.comet[0]
        elif (self.count >= 40) and (self.count <= 80):
            comet = self.comet[1]

        self.surf.blit(comet, self.rect)
        if pygame.sprite.groupcollide(shoots, mets, False, False) != {}:
            if self.hitpoints != 0:
                pygame.sprite.groupcollide(shoots, mets, True, False)
                self.hitpoints -= 50
            elif self.hitpoints == 0:
                pygame.sprite.groupcollide(shoots, mets, True, True)

        if self.rect.y > 640:
            self.kill()
        else:
            self.rect.y += 2




