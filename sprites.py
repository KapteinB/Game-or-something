from typing import Any
import pygame as pg
import random


player_image = pg.image.load("peter.png")
bobm_image = pg.image.load("bobm2.png")
player_image1 = pg.image.load("canon.png")
player_image2 = pg.image.load("petah.png")
player_image3 = pg.image.load("doors.png")
player_image4 = pg.image.load("attac.png")
enemy_image = pg.image.load("Ben.png")
END_image = pg.image.load("END.png")
enemy2_image = pg.image.load("DEATH3.png")
enemy3_image = pg.image.load("Death4.png")
bullet_image = pg.image.load("TNT.png")
bullet2_image = pg.image.load("doomer.png")
bullet3_image = pg.image.load("door.png")
bullet3_image2 = pg.image.load("door2.png")
bullet3_image3 = pg.image.load("door3.png")
bullet3_image4 = pg.image.load("door4.png")
enemy_1_image = pg.image.load("ben2.png")
enemy2_1_image = pg.image.load("DEATH3.png")
boss1_image = pg.image.load("DEATH7.png")
boss1_image2 = pg.image.load("boss1.png")
enemy4_image = pg.image.load("bot1.png")
enemy4_image2 = pg.image.load("bot2.png")
enemy5_image = pg.image.load("dEATH2.png")
enemy5_image2 = pg.image.load("cuttr.png")
enemy6_image = pg.image.load("Death12.png")
enemy6_image2 = pg.image.load("mimic2.png")
enemy6_image3 = pg.image.load("mimic3.png")
enemy7_image = pg.image.load("boomer1.png")
enemy7_image2 = pg.image.load("boomer2.png")
enemy8_image = pg.image.load("walker1.png")
enemy9_image = pg.image.load("Death13.png")
enemy8_image2 = pg.image.load("walker2.png")
enemy10_image = pg.image.load("agony.png")
enemy10_image2 = pg.image.load("agony2.png")
enemy11_image = pg.image.load("Death5.png")
enemy12_image = pg.image.load("bobm1.png")
enemy11_image2 = pg.image.load("Missile.png")
Ebullet1_image = pg.image.load("ebullet1.jpg")
bullet_particle1 = pg.image.load("tnt1.png")
bullet_particle2 = pg.image.load("tnt2.png")

story1 = pg.image.load("story1.png")
story2 = pg.image.load("story2.png")
story3 = pg.image.load("story3.png")
story4 = pg.image.load("story4.png")
story5 = pg.image.load("story5.png")
story6 = pg.image.load("story6.png")
story7 = pg.image.load("story7.png")
story8 = pg.image.load("story8.png")
story9 = pg.image.load("story9.png")
story10 = pg.image.load("story10.png")
story11 = pg.image.load("story11.png")

story1 = pg.transform.scale(story1,(1400,950))
story2 = pg.transform.scale(story2,(1400,950))
story3 = pg.transform.scale(story3,(1400,950))
story4 = pg.transform.scale(story4,(1400,950))
story5 = pg.transform.scale(story5,(1400,950))
story6 = pg.transform.scale(story6,(1400,950))
story7 = pg.transform.scale(story7,(1400,950))
story8 = pg.transform.scale(story8,(1400,950))
story9 = pg.transform.scale(story9,(1400,950))
story10 = pg.transform.scale(story10,(1400,950))
story11 = pg.transform.scale(story11,(1400,950))

player_image = pg.transform.scale(player_image,(125,110))
bobm_image = pg.transform.scale(bobm_image,(400,300))
player1_image = pg.transform.scale(player_image1,(125,110))
player2_image = pg.transform.scale(player_image2,(125,110))
player3_image = pg.transform.scale(player_image3,(125,110))
player4_image = pg.transform.scale(player_image4,(125,110))
enemy2_image = pg.transform.scale(enemy2_image,(200,200))
enemy3_image = pg.transform.scale(enemy3_image,(100,200))
enemy2_1_image = pg.transform.scale(enemy2_1_image,(200,190))
boss1_image = pg.transform.scale(boss1_image,(1200,950))
boss1_image2 = pg.transform.scale(boss1_image2,(1200,950))
enemy4_image = pg.transform.scale(enemy4_image,(400,200))
enemy4_image2 = pg.transform.scale(enemy4_image2,(400,200))
enemy7_image = pg.transform.scale(enemy7_image,(200,200))
enemy7_image2 = pg.transform.scale(enemy7_image2,(200,200))
enemy5_image = pg.transform.scale(enemy5_image,(400,200))
enemy9_image = pg.transform.scale(enemy9_image,(400,200))
enemy5_image1 = pg.transform.scale(enemy5_image2,(400,200))
enemy8_image = pg.transform.scale(enemy8_image,(150,250))
enemy8_image2 = pg.transform.scale(enemy8_image2,(200,200))
enemy6_image = pg.transform.scale(enemy6_image,(400,200))
enemy6_image2 = pg.transform.scale(enemy6_image2,(600,300))
enemy10_image = pg.transform.scale(enemy10_image,(200,200))
enemy10_image2 = pg.transform.scale(enemy10_image2,(200,200))
enemy11_image = pg.transform.scale(enemy11_image,(400,400))
enemy11_image2 = pg.transform.scale(enemy11_image2,(800,400))
enemy12_image = pg.transform.scale(enemy12_image,(800,700))
enemy6_image3 = pg.transform.scale(enemy6_image3,(800,400))
Ebullet1_image = pg.transform.scale(Ebullet1_image,(100,100))
bullet2_image = pg.transform.scale(bullet2_image,(300,300))
bullet3_image = pg.transform.scale(bullet3_image,(50,50))
bullet3_image2 = pg.transform.scale(bullet3_image2,(50,50))
bullet3_image3 = pg.transform.scale(bullet3_image3,(50,50))
bullet3_image4 = pg.transform.scale(bullet3_image4,(50,50))
END_image = pg.transform.scale(END_image,(50,100))



class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites, bullets, players, bullets2,):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 0
        self.pos_y = 400
        self.speed = 20
        self.mode = 1
        self.cooldown = 0
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.players = players
        self.bullets2 = bullets2
        self.ammo = 100
        self.hp = 250
    
    def take_dmg(self, dmg):
        self.hp -= dmg
        self.pain = pg.mixer.Sound("error.mp3")
        pg.mixer.Sound.play(self.pain)
        if self.hp <= 0:
            self.kill()


    def attec(self):
        if self.ammo > 0:
            if self.mode == 1 and self.ammo > 99:   #tnt canon
                attack = Bullet(self.pos_x, self.pos_y)
                attack.add(self.all_sprites)
                attack.add(self.bullets)
                attack = Bullet2(self.pos_x, self.pos_y)
                attack.add(self.all_sprites)
                attack.add(self.bullets)
                attack = Bullet3(self.pos_x, self.pos_y)
                attack.add(self.all_sprites)
                attack.add(self.bullets)
                self.ammo -= 100
            if self.mode == 2 and self.ammo > 599:  #roomba of death
                attack = Bullet4(self.pos_x, self.pos_y)
                attack.add(self.all_sprites)
                attack.add(self.bullets2)
                self.image = player4_image
                self.ammo = 0
            if self.mode == 3 and self.ammo > 699:  #DOORang
                attack = Bullet5(self.pos_x, self.pos_y)
                attack.add(self.all_sprites)
                attack.add(self.bullets2)
                self.ammo -= 700
                self.image = player4_image
    

    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]: # oppover
            self.pos_y -= self.speed
            if self.pos_y <= 0:
                self.pos_y = 0
        if keys[pg.K_s]: # nedover
            self.pos_y += self.speed
            if self.pos_y >= 1200:
                self.pos_y = 1200
        if keys[pg.K_a]: # venstre
            self.pos_x -= self.speed
            if self.pos_x <= 0:
                self.pos_x = 0
        if keys[pg.K_d]: # høyre
            self.pos_x += self.speed
            if self.pos_x >= 1800:
                self.pos_x = 1800
        if keys[pg.K_SPACE]:
            self.attec()
        if keys[pg.K_e]:
            if self.cooldown < 1:       #mode 1  is the basic tnt canon, mode 2 is the roomba death machine, mode 3 is the door boomerang.
                if self.mode == 1:
                    self.mode = 2
                    self.image = player2_image
                    self.ammo *= 4
                elif self.mode == 3:
                    self.mode = 1
                    self.image = player_image
                    self.ammo = 100
                elif self.mode == 2:
                    self.mode = 3
                    self.image = player3_image
                    self.ammo = 700
                self.cooldown = 50
        if keys[pg.K_q]:
            if self.cooldown < 1:
                if self.mode == 3:
                    self.mode = 2
                    self.image = player2_image
                    self.ammo *= 4
                elif self.mode == 2:
                    self.mode = 1
                    self.image = player_image
                    self.ammo = 100
                elif self.mode == 1:
                    self.mode = 3
                    self.image = player3_image
                    self.ammo = 700
                self.cooldown = 50
        
        if self.ammo <= 700:
            self.ammo += 5
            if self.mode == 1 and self.ammo > 99:
                self.ammo = 100
            if self.ammo == 100:
                self.image = player_image
            if self.mode == 1 and self.ammo > 99:
                self.image = player1_image
            if self.mode == 2 and self.ammo > 600:
                self.image = player2_image
            if self.mode == 3 and self.ammo == 700:
                self.image = player3_image
        self.cooldown -= 1

class END(pg.sprite.Sprite): # The end has come
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = END_image
        self.rect = self.image.get_rect()
        self.pos_x = random.randint(0,1800)
        self.pos_y = -50
        self.speed = random.randint(15,16)
       

    def update(self):

        self.pos_y += self.speed
        self.speed = random.randint(3,4)
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        
        if self.pos_y > 1300:
            self.kill()

class Bullet(pg.sprite.Sprite): # bobm
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
         
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.speed = 20
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        self.pos_x += self.speed

class Bullet4(pg.sprite.Sprite): # Wroomba Construct
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.chainsaw_sound = pg.mixer.Sound("chainsaw-05.mp3") 
        self.image = bullet2_image
        self.rect = self.image.get_rect()
        self.pos_x = x - 100
        self.pos_y = y - 100
        self.speed = 1
        self.hp = 5
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        pg.mixer.Sound.play(self.chainsaw_sound)
        

    def hi(self):
        self.hp -= 1
        if self.hp < 1:
            self.kill

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.speed += random.randint(2,3)
        self.pos_x += self.speed

class Bullet5(pg.sprite.Sprite): # boomeranga
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet3_image
        self.rect = self.image.get_rect()
        self.pos_x = x
        self.pos_y = y - 50
        self.speed = 13
        self.hp = 5
        self.counter = 50
        self.direction = 0
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.current_frame = 0   
        self.last_update = 0
        self.standing_frames = [bullet3_image, bullet3_image2, bullet3_image4, bullet3_image3]

    def hi(self):
        self.hp -= 1
        if self.hp < 1:
            self.kill

    def update(self):
        self.animate()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.counter -= 1
        if self.counter == 0:
            self.direction = 1
        if self.direction == 0:
            self.pos_x += self.speed
        if self.direction == 1:
            self.pos_x -= self.speed
    
    def animate(self):
        now = pg.time.get_ticks()   # på starten av animate henter vi hvilken "tick" eller frame vi er på 1 tick er 1 FPS
 
                   
        if now - self.last_update > 50:   # her sørger vi for at vi bytte bilde kun hver 350 tick, lavere tall animerer fortere
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()
    
class Bullet2(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet_particle1
        self.rect = self.image.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.counter = 5
        self.speed = 40
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
       

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        self.pos_x += self.speed
        self.pos_y += self.speed
        self.counter -= 1
        if self.counter == 0:
            self.kill()

class Enemy10(pg.sprite.Sprite): # look down :)
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy10_image
        self.rect = self.image.get_rect()
        self.pos_x = random.randint(0,1800)
        self.pos_y = 1300
        self.speed = random.randint(12,13)
        self.current_frame = 0   
        self.last_update = 0
        self.standing_frames = [enemy10_image, enemy10_image2]

    def update(self):
        self.animate()
        self.pos_y -= self.speed
        self.speed = random.randint(3,4)
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.pos_y < -50:
            self.kill()

    def animate(self):
        now = pg.time.get_ticks() 
 
                   
        if now - self.last_update > 200:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()

class Bullet3(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet_particle2
        self.rect = self.image.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.counter = 5
        self.speed = 40
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.current_frame = 0   
        self.last_update = 0
        self.standing_frames = [enemy8_image, enemy8_image2]

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        self.pos_x += self.speed
        self.pos_y -= self.speed
        self.counter -= 1
        if self.counter == 0:
            self.kill()

class Enemy(pg.sprite.Sprite): #basic guy
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos_x = 1900
        self.pos_y = random.randint(10,1200)
        self.speed = random.randint(3,5)
        self.current_frame = 0  
        self.last_update = 0
        self.standing_frames = [enemy_image, enemy_1_image]

    def update(self):
        self.animate()
        self.pos_x -= self.speed
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.pos_x < -100:
            self.kill()
        

    def animate(self):
        now = pg.time.get_ticks()  
 
                   
        if now - self.last_update > 100:   
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()
    
    def boomer(self):
        self.kill()

class Enemy12(pg.sprite.Sprite): #big guy
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos_x = 1900
        self.pos_y = 700
        self.speed = 1
        self.current_frame = 0  
        self.last_update = 0
        self.standing_frames = [boss1_image, boss1_image2]

    def update(self):
        self.animate()
        self.pos_x -= self.speed
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.pos_x < -100:
            self.kill()
        

    def animate(self):
        now = pg.time.get_ticks()  
 
                   
        if now - self.last_update > 100:   
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()
    
    def boomer(self):
        self.kill()



class Enemy2(pg.sprite.Sprite): # fast one
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy2_image
        self.rect = self.image.get_rect()
        self.pos_x = 1900
        self.pos_y = random.randint(10,1200)
        self.speed = random.randint(12,13)
        self.current_frame = 0   
        self.last_update = 0
        self.standing_frames = [enemy2_image, enemy2_1_image]

    def update(self):
        self.animate()
        self.pos_x -= self.speed
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.pos_x < -100:
            self.kill()

    def animate(self):
        now = pg.time.get_ticks()   
 
                   
        if now - self.last_update > 200:  
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()

class Enemy5(pg.sprite.Sprite): # slow guy
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy5_image
        self.rect = self.image.get_rect()
        self.pos_x = 1900
        self.pos_y = random.randint(10,1200)
        self.speed = random.randint(12,13)
        self.current_frame = 0  
        self.last_update = 0
        self.standing_frames = [enemy5_image, enemy5_image1]

    def update(self):
        self.animate()
        self.pos_x -= self.speed
        self.speed = random.randint(1,2)
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.pos_x < -100:
            self.kill()

    def animate(self):
        now = pg.time.get_ticks()   
 
                   
        if now - self.last_update > 200: 
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()

class Enemy9(pg.sprite.Sprite): # :)
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy9_image
        self.rect = self.image.get_rect()
        self.pos_x = 1900
        self.direction = random.randint(0,1)
        self.pos_y = random.randint(10,1200)
        self.speed = random.randint(12,13)
        
    def update(self):
        
        self.pos_x -= self.speed
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.direction == 0:
            self.pos_y -= self.speed
        elif self.direction == 1:
            self.pos_y += self.speed
        if self.pos_y < 50:
            self.direction = 1
        elif self.pos_y > 1150:
            self.direction = 0
        
        if self.pos_x < -100:
            self.kill()

class Enemy6(pg.sprite.Sprite): # R E A C H
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy5_image
        self.rect = self.image.get_rect()
        self.pos_x = 1900
        self.pos_y = random.randint(10,1200)
        self.speed = random.randint(12,13)
        self.current_frame = 0   
        self.last_update = 0
        self.standing_frames = [enemy6_image, enemy6_image2, enemy6_image3, enemy6_image2]

    def update(self):
        self.animate()
        self.pos_x -= self.speed
        self.speed = random.randint(3,4)
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.pos_x < -100:
            self.kill()

    def animate(self):
        now = pg.time.get_ticks()  
 
                   
        if now - self.last_update > 200:   
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()

class Enemy7(pg.sprite.Sprite): # BOMBS ARE DROPPING FROM THE SKY!!
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy7_image
        self.rect = self.image.get_rect()
        self.pos_x = random.randint(0,1800)
        self.pos_y = -50
        self.speed = random.randint(15,16)
       

    def update(self):
        self.pos_y += self.speed
        self.speed = random.randint(3,4)
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        
        if self.pos_y > 1300:
            self.kill()

class Enemy11(pg.sprite.Sprite): #Missiles
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy11_image
        self.rect = self.image.get_rect()
        self.pos_x = 1800
        self.pos_y = random.randint(10,1200)
        self.speed = 0
        self.beep_sound = pg.mixer.Sound("beep-warning-6387.mp3") 
        self.tick = 80
        

    def update(self):
        self.pos_x -= self.speed
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.tick -= 1
        if self.tick == 79:    
            pg.mixer.Sound.play(self.beep_sound)
        if self.tick == 0:
            self.image = enemy11_image2
            self.speed = 100
        if self.pos_x < -100:
            self.kill()
        

   
    
    def boomer(self):
        self.kill()

  


class Enemy8(pg.sprite.Sprite): # R U N
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy8_image
        self.rect = self.image.get_rect()
        self.pos_x = 1900
        self.pos_y = random.randint(10,1200)
        self.speed = random.randint(10,11)
        self.current_frame = 0  
        self.last_update = 0
        self.standing_frames = [enemy8_image, enemy8_image2]

    def update(self):
        self.animate()
        self.pos_x -= self.speed
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.pos_x < -100:
            self.speed = -10
        if self.pos_x > 2000:
            self.kill()

    def animate(self):
        now = pg.time.get_ticks()   
 
                   
        if now - self.last_update > 200: 
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()

class Enemy3(pg.sprite.Sprite): # stupid drone thing
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy3_image
        self.rect = self.image.get_rect()
        self.pos_x = 1900
        self.isgoup = 0
        self.pos_y = random.randint(10,1200)
        self.speed = random.randint(3,6)
    
    def update(self):
        
        self.pos_y = self.pos_y + random.randint(-50,50)
        if self.pos_y < 0:
            self.pos_y = 0
        if self.pos_y > 1300:
            self.pos_y = 1300
        self.pos_x -= self.speed
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.pos_x < -100:
            self.kill()

class Story(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = story1
        self.rect = self.image.get_rect()
        self.pos_x = 900
        self.pos_y = 600
        self.tick = 0
    
    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.tick += 1
        if self.tick == 200:
            self.tick = 0
            if self.image == story1:
                self.image = story2
            elif self.image == story2:
                self.image = story3
            elif self.image == story3:
                self.image = story4
            elif self.image == story4:
                self.image = story5
            elif self.image == story5:
                self.image = story6
            else:
                self.kill()

class Story2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = story7
        self.rect = self.image.get_rect()
        self.pos_x = 900
        self.pos_y = 600
        self.tick = 0
    
    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.tick += 1
        if self.tick == 350:
            self.tick = 0
            if self.image == story7:
                self.image = story8
            elif self.image == story8:
                self.image = story9
            elif self.image == story9:
                self.image = story10
            elif self.image == story10:
                self.image = story11
            else:
                self.kill()