import pygame as pg
import time
import random
from sprites import *
pg.init()
bg_img = pg.image.load("apocolypse.jpg")
WIDTH = 1800
screen = pg.display.set_mode((WIDTH,1300))
bg_img = pg.transform.scale(bg_img,(WIDTH,1300))
killcount = 0
score = 0
i = 0
the_end = 0
bosshp = 0
enemy_cap = 20
enemy_sprites = pg.sprite.Group()
all_sprites = pg.sprite.Group()
#    w 
players = pg.sprite.Group()
bosses = pg.sprite.Group()
sheilder = pg.sprite.Group()
wroomba = pg.sprite.Group()
bullets = pg.sprite.Group()
bullets2 = pg.sprite.Group()
Ebullets = pg.sprite.Group()

pg.mixer.music.load('the-final-boss-battle-158700.mp3') 
pg.mixer.music.play(-1) 
 
story = 1500

pattern = 0
pattern_e = 0

playing = True
enemy = Enemy()
enemy2 = Enemy2()
enemy3 = Enemy3()


attack = Bullet(0, 0)

font_cs30 = pg.font.SysFont("Papyrus", 30)
font_cs100 = pg.font.SysFont("Papyrus", 100)
bg_img_apo3 = pg.image.load("apocolypse3.jpg")
bg_img_end = pg.image.load("Ending.jpg")
apo2 = pg.image.load("apocolypse2.jpg")
bg_img_end = pg.transform.scale(bg_img_end,(WIDTH,1300))
bg_img_apo3 = pg.transform.scale(bg_img_apo3,(WIDTH,1300))
bg_img_apo2 = pg.transform.scale(apo2,(WIDTH,1300))





player = Player(all_sprites, bullets, players, bullets2)
all_sprites.add(player)

players.add(player)


bullets.add(attack)

new_enemy = Story()
all_sprites.add(new_enemy)

clock = pg.time.Clock()
pos_x = 100
pos_y = 100
size_x = 50
size_y = 50
box_1_dir = 5
 

BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
PURPLE = (110,50,255)

player_box = pg.Rect(69,420, 50,50)
enemy_box = pg.Rect(40,320, 40,40)



while playing:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            screen = pg.display.set_mode((1000,800))
            time.sleep(0.025)
            screen = pg.display.set_mode((800,600))
            time.sleep(0.025)
            screen = pg.display.set_mode((600,400))
            time.sleep(0.025)
            screen = pg.display.set_mode((400,200))
            time.sleep(0.025)
            screen = pg.display.set_mode((200,100))
            time.sleep(0.025)
            screen = pg.display.set_mode((100,50))
            time.sleep(0.025)
            screen = pg.display.set_mode((50,25))
            time.sleep(0.025)
            screen = pg.display.set_mode((10,5))
            time.sleep(0.025)
            pg.quit()
        
    all_sprites.update()
    enemy_sprites.update()
    bosses.update()
    sheilder.update()
    screen.fill(BLACK)

    
    screen.blit(bg_img,(i,0))
    screen.blit(bg_img,(WIDTH+i,0))
    if (i == -WIDTH):
        screen.blit(bg_img,(WIDTH+i,0))
        i=0
    i-=1
    
    hits = pg.sprite.spritecollide(player, enemy_sprites, True)
    if hits:
        #player.hp -= 1o
        player.take_dmg(10)
    hits = pg.sprite.spritecollide(player, bosses, False)
    if hits:
        #player.hp -= a lot
        player.take_dmg(15)
    hits = pg.sprite.spritecollide(player, sheilder, False)
    if hits:
        #player.hp -= a lot
        player.take_dmg(1)
    
    hits = pg.sprite.groupcollide(bullets, bosses, True, False)
    if hits:
        pass

    hits4 = pg.sprite.groupcollide(bullets, sheilder, True, False)
    if hits4:
        pass
    
    hits2 = pg.sprite.groupcollide(bullets, enemy_sprites, True, True)
    if hits2:
        score = score + 250
    
    hits3 = pg.sprite.groupcollide(bullets2, enemy_sprites, False, True)
    if hits3:
        score = score + 250
    
    if  score == 100000 and not the_end:
        bg_img = bg_img_apo2
        enemy_cap = 15
        pg.mixer.stop()
        the_end = True
        pg.mixer.music.load('hip-hop-main-event-13790.mp3') 
        pg.mixer.music.play(-1) 

    
    if the_end:
        killcount = killcount + 1
        if killcount == 500:
            enemy_cap = 20
        if killcount == 1000:
            enemy_cap = 25
        if killcount == 1500:
            enemy_cap = 30
        if killcount == 2000:
            enemy_cap = 35
        if killcount == 5010:
            the_end = 2
        
        if killcount == 2500:
            bg_img = bg_img_apo3
            enemy_cap = 40

    text = font_cs30.render(f"HP: {player.hp}", False, (RED))
    text2 = font_cs30.render(f" Score: {score}", False, (YELLOW))
    text3 = font_cs100.render(f"FLAWLESS VICTORY", False, (BLUE))
    text5 = font_cs100.render(f"(how)", False, (BLUE))
    text4 = font_cs100.render(f"VICTORY", False, (BLUE))
        
    if the_end == 2 and len(enemy_sprites) == 0:
        bg_img = bg_img_end
        the_end = 3
        pg.mixer.music.load('piano-moment-9835.mp3') 
        pg.mixer.music.play(-1) 
        new_enemy = Story2()
        all_sprites.add(new_enemy)
        
        
    all_sprites.draw(screen)
    enemy_sprites.draw(screen)
    bosses.draw(screen)
    wroomba.draw(screen)
    sheilder.draw(screen)

    keys = pg.key.get_pressed()
    if keys[pg.K_p] and len(bosses) < 1: # oppover
        new_enemy = Enemy12()
        bosses.add(new_enemy)     
        
    if story <= 0:
        if len(enemy_sprites) < enemy_cap:
            if score < 100000:
                if score >= 20000 and score < 40000:
                    randomness = random.randint(1,6) 
                elif score >= 40000 and score < 60000:
                    randomness = random.randint(1,8)
                elif score >= 60000 and score < 80000:
                    randomness = random.randint(1,10)
                elif score >= 80000:
                    enemy_cap = 15
                    randomness = random.randint(6,11)
                    if len(bosses) == 1:
                        randomness = random.randint(6,10)
                else:
                    randomness = random.randint(1,5)
                if randomness == 1:
                    new_enemy = Enemy()
                    enemy_sprites.add(new_enemy)
                if randomness == 2:
                    new_enemy = Enemy2()
                    enemy_sprites.add(new_enemy)
                if randomness == 3:
                    new_enemy = Enemy3()
                    enemy_sprites.add(new_enemy)
                if randomness == 4:
                    new_enemy = Enemy5()
                    enemy_sprites.add(new_enemy)
                if randomness == 5:
                    new_enemy = Enemy6()
                    enemy_sprites.add(new_enemy)
                if randomness == 6:
                    new_enemy = Enemy8()
                    enemy_sprites.add(new_enemy)
                if randomness == 7:
                    new_enemy = Enemy7()
                    enemy_sprites.add(new_enemy)
                if randomness == 8:
                    new_enemy = Enemy9()
                    enemy_sprites.add(new_enemy)
                if randomness == 9:
                    new_enemy = Enemy10()
                    enemy_sprites.add(new_enemy)
                if randomness == 10:
                    new_enemy = Enemy12()
                    sheilder.add(new_enemy)
                if randomness == 11:
                    new_enemy = Enemy11()
                    bosses.add(new_enemy)
            else:
                if the_end < 2:
                    new_enemy = END()
                    enemy_sprites.add(new_enemy)
    else:
        story -= 1
    
   
    screen.blit(text, (11, 11))
    screen.blit(text2, (141, 11))
    if the_end == 3:    
        if player.hp >= 250:
            screen.blit(text3, (200, 100))
            screen.blit(text5, (750, 250))
        elif player.hp > 0:
            screen.blit(text4, (550, 100))
 
    pg.display.update()


