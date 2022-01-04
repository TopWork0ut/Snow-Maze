import pygame
import sys
import time

pygame.init()

pygame.display.set_caption("Гра")
wikno = pygame.display.set_mode((600,600))

playzone = pygame.Surface((600,600))

clock = pygame.time.Clock()

def terminate():
    pygame.quit()
    sys.exit()


def load_image(name):
    fullname = "images"+"/"+name
    try:
        image = pygame.image.load(fullname).convert()
    except:
        print("can not  load image", name)
        raise SystemExit()
    return image


all_sprites = pygame.sprite.Group()
block_box_group = pygame.sprite.Group()
block_ice_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
flower_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()
theend_group = pygame.sprite.Group()


class theend(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__(all_sprites,theend_group)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.add(theend_group)



class Flower(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__(all_sprites,flower_group)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.add(flower_group)

class Fire(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__(all_sprites,fire_group)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.add(fire_group)


class block_ice(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__(all_sprites,block_ice_group)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.add(block_ice_group)



class block_box(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__(all_sprites,block_box_group)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.add(block_box_group)


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__(all_sprites,player_group)


        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



        self.add(all_sprites)
    

    def move_up(self):
            self.rect = self.rect.move(0 ,-50)

    def move_down(self):
            self.rect = self.rect.move(0 , 50)

    def move_right(self):
            self.rect= self.rect.move(50,0)

    def move_left(self):
            self.rect = self.rect.move(-50,0)


level = ["...###......",
         "..##.#.####.",
         ".##..###..#.",
         "##........#.",
         "#......#..#.",
         "###..###..#.",
         "..#..#....#.",
         ".##.##...##.",
         ".#......##..",
         ".#.....##...",
         ".#######....",
         "............"]

def level_1():
    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == ".":
                ice = block_ice(x,y,"ice.png")


            if col == "#":
                box = block_box(x,y,"box.png")




            x += 50
        y+= 50
        x = 0



    fire = Fire(200,250,"fire2.png")
    flower = Flower(350,350,"flower2.png")
    player = Player(150,150,"snowman2.png")
    true = True

    while true :
        for najatie in pygame.event.get():
            if najatie.type == pygame.QUIT:
                terminate()
            if najatie.type == pygame.KEYDOWN:
                #if not pygame.sprite.groupcollide(player_group,block_box_group,False,False) :
                if  pygame.sprite.groupcollide(player_group,block_ice_group,False,False) :


                    if najatie.key == pygame.K_RIGHT:
                        player.move_right()
                    if najatie.key == pygame.K_LEFT:
                        player.move_left()
                    if najatie.key == pygame.K_UP:
                        player.move_up()
                    if najatie.key == pygame.K_DOWN:
                        player.move_down()

                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_RIGHT:
                    player.move_left()
                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_LEFT:
                    player.move_right()
                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_UP:
                    player.move_down()
                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_DOWN:
                    player.move_up()



        clock.tick(120)

        wikno.blit(playzone,(0,0))

        playzone.fill((0,0,0))

        block_ice_group.draw(playzone)
        block_box_group.draw(playzone)
        fire_group.draw(playzone)
        player_group.draw(playzone)
        flower_group.draw(playzone)
        theend_group.draw(playzone)

        all_sprites.update()

        if pygame.sprite.groupcollide(player_group,flower_group,False,False):
            all_sprites.empty()
            block_ice_group.empty()
            block_box_group.empty()
            player_group.empty()
            flower_group.empty()
            fire_group.empty()
            return

        pygame.display.flip()

        if pygame.sprite.groupcollide(player_group,fire_group,False,False) :
                thend = theend(100,300,"gameover.png")
                time.s


level2 = ["######......",
            "#..#.#.####.",
            "#....###..#.",
            "##.....#..#.",
            "#......#..#.",
            "###.......#.",
            "..#..#....#.",
            ".##......##.",
            ".#.##.####..",
            ".#.....##...",
            ".#######....",
            "............"]







def level_2():
    x = 0
    y = 0
    for row in level2:
        for col in row:
            if col == ".":
                ice = block_ice(x,y,"ice.png")


            if col == "#":
                box = block_box(x,y,"box.png")




            x += 50
        y+= 50
        x = 0



    flower = Flower(100,400,"flower2.png")
    player = Player(150,150,"snowman2.png")
    fire = Fire(200,350,"fire2.png")
    true = True

    while true :
        for najatie in pygame.event.get():
            if najatie.type == pygame.QUIT:
                terminate()
            if najatie.type == pygame.KEYDOWN:
                #if not pygame.sprite.groupcollide(player_group,block_box_group,False,False) :
                if  pygame.sprite.groupcollide(player_group,block_ice_group,False,False) :


                    if najatie.key == pygame.K_RIGHT:
                        player.move_right()
                    if najatie.key == pygame.K_LEFT:
                        player.move_left()
                    if najatie.key == pygame.K_UP:
                        player.move_up()
                    if najatie.key == pygame.K_DOWN:
                        player.move_down()





                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_RIGHT:
                    player.move_left()
                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_LEFT:
                    player.move_right()
                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_UP:
                    player.move_down()
                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_DOWN:
                    player.move_up()


        clock.tick(60)

        wikno.blit(playzone,(0,0))

        playzone.fill((0,0,0))

        block_ice_group.draw(playzone)
        block_box_group.draw(playzone)
        player_group.draw(playzone)
        flower_group.draw(playzone)
        fire_group.draw(playzone)

        if pygame.sprite.groupcollide(player_group,flower_group,False,False):
            all_sprites.empty()
            block_ice_group.empty()
            block_box_group.empty()
            player_group.empty()
            flower_group.empty()
            fire_group.empty()
            return

        pygame.display.flip()




level3 = [".........####",
            "#########..#",
            "###.......##",
            "##....###..#",
            "#...##.#..##",
            "#.......#..#",
            "#...##.....#",
            "#.####...#.#",
            "#..##.###..#",
            "#........###",
            "#.....######",
            "#######....."]

def level_3():
    x = 0
    y = 0
    for row in level3:
        for col in row:
            if col == ".":
                ice = block_ice(x,y,"ice.png")


            if col == "#":
                box = block_box(x,y,"box.png")




            x += 50
        y+= 50
        x = 0


    fire = Fire(500,300,"fire2.png")
    flower = Flower(250,500,"flower2.png")
    player = Player(500,50,"snowman2.png")
    true = True

    while true :
        for najatie in pygame.event.get():
            if najatie.type == pygame.QUIT:
                terminate()
            if najatie.type == pygame.KEYDOWN:
                #if not pygame.sprite.groupcollide(player_group,block_box_group,False,False) :
                if  pygame.sprite.groupcollide(player_group,block_ice_group,False,False) :


                    if najatie.key == pygame.K_RIGHT:
                        player.move_right()
                    if najatie.key == pygame.K_LEFT:
                        player.move_left()
                    if najatie.key == pygame.K_UP:
                        player.move_up()
                    if najatie.key == pygame.K_DOWN:
                        player.move_down()

                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_RIGHT:
                    player.move_left()
                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_LEFT:
                    player.move_right()
                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_UP:
                    player.move_down()
                if pygame.sprite.groupcollide(player_group,block_box_group,False,False) and najatie.key == pygame.K_DOWN:
                    player.move_up()

                if pygame.sprite.groupcollide(player_group,fire_group,False,False) :
                    thend = theend(100,300,"gameover.png")



        clock.tick(60)

        wikno.blit(playzone,(0,0))

        playzone.fill((0,0,0))

        block_ice_group.draw(playzone)
        block_box_group.draw(playzone)
        player_group.draw(playzone)
        flower_group.draw(playzone)
        fire_group.draw(playzone)

        if pygame.sprite.groupcollide(player_group,flower_group,False,False):
            terminate()

        pygame.display.flip()

level_1()
level_2()
level_3()
