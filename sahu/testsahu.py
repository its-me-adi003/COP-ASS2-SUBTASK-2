import pygame
import os
import random
# from pygame.sprite import Group

pygame.init()
clock=pygame.time.Clock()
fps=60
TILE_SIZE = 40
g=0.75

RED = (255,0,0)
shoot = False

SCREEN_WIDTH = 800
SCREEN_HEIGHT = SCREEN_WIDTH*0.8
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('player')

def draw_bg():
    screen.fill((255,255,255))
    pygame.draw.line(screen,(255,0,0),(0,400),(SCREEN_WIDTH,400))

bullet_imgage = pygame.image.load("bullet.png")
health_box_img = pygame.image.load('health.png')
bullet_box_img = pygame.image.load('ammo_box.png')

item_boxes = {
    'Health' : health_box_img,
    "Bullet" : bullet_box_img
}

font  = pygame.font.SysFont('Futura',30)

def draw_text(text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))


class Player(pygame.sprite.Sprite):
    def __init__(self,chart,x,y,scale,vel,ammo):
        
        pygame.sprite.Sprite.__init__(self)
        self.vel=vel
        self.chart=chart
        self.direction=1
        self.zinda=True
        self.ammo = ammo
        self.start_ammo = ammo
        self.jump=False
        self.shoot_cooldown = 0
        self.health = 100
        self.max_health = self.health
        self.animationl=[]
        self.animation_sets = {
            "Idle": [],
            "Run": [],
            "Death":[]
        }
        self.idx=0
        self.vely=0
        self.action="Idle"
        
        self.move_counter=0
        self.vision = pygame.Rect(0,0,150,20)
        self.idling = False
        self.idling_counter = 0
        # temp=[]
        self.time=pygame.time.get_ticks()
        for i in range(5):  # Load all images for animation
            image_path = os.path.join("Idle", f"{i}.png")
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            self.animation_sets["Idle"].append(image)
            
        for i in range(6):  # Load all images for animation
            image_path = os.path.join("Run", f"{i}.png")
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            self.animation_sets["Run"].append(image)
            
        for i in range(8):  # Load all images for animation
            image_path = os.path.join("Death", f"{i}.png")
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            self.animation_sets["Death"].append(image)
            
        self.img=self.animation_sets[self.action][self.idx]
        self.flip=False
        # if self.chart=='player':
        #     self.img=pygame.image.load(f'Blue/idle/{i}.png')
        # else:
        #     self.img=pygame.image.load('Blue/Gunner_Blue_Idle.png')
        self.rect=self.img.get_rect()
        self.rect.center=(x,y)
        
    def update(self):
        self.animation()
        self.check_zinda()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        
        
            
    def animation(self):
        if pygame.time.get_ticks()-self.time>100:
            self.time=pygame.time.get_ticks()
            self.idx+=1
            if self.idx>=len(self.animation_sets[self.action]):
                if self.action == "Death":
                    self.idx = len(self.animation_sets[self.action]) -1
                else:
                    self.idx=0
            self.img=self.animation_sets[self.action][self.idx]
    def change_action(self,action):
        if action!=self.action:
            self.action=action
            self.idx=0
            self.time=pygame.time.get_ticks()
            
    def check_zinda(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.zinda = False
            self.change_action("Death")
    def draw(self):
        screen.blit(pygame.transform.flip(self.img,self.flip,False),self.rect)
    def move(self,left,right):
        dx=0
        dy=0
        if left:
            dx=-self.vel
            self.direction=-1 
            if self.direction == 1:
                self.flip = False
            else:
                self.flip = True  
        if right:
            dx=self.vel
            self.direction=1
            if self.direction == 1:
                self.flip = False
            else:
                self.flip = True  
        if self.jump:
            # print(self.jump)
            self.vely=-11
            # dy=-self.vely
            self.jump=False
        self.vely+=g
        if self.vely>10:
            self.vely=10
        dy+=self.vely

        #--------------------------------
        if self.rect.bottom+dy>400:
            dy=400-self.rect.bottom
            self.vely=0
        self.rect.x+=dx
        self.rect.y+=dy
     #----------------------- this is not in mine
    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown =20
            bullet = Bullet(self.rect.centerx + (self.direction * 0.75 * self.rect.size[0]),self.rect.centery,self.direction)
            bullet_group.add(bullet)
             
            self.ammo -= 1


    def ai(self):
        if self.zinda and player1.zinda:
            if self.idling==False and random.randint(1,100) == 1:
                # self.change_action("Idle")
                self.idling = True
                self.idling_counter = 50
                
                
            if self.vision.colliderect(player1.rect):
                self.change_action("Idle")
                self.shoot()
            else:   
                if self.idling == False:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left,ai_moving_right)
                    # self.change_action("Run")
                    self.move_counter += 1
                    self.vision.center = (self.rect.centerx + 75*self.direction,self.rect.centery)
                    # pygame.draw.rect(screen,RED,self.vision)
                    
                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                        
                else:
                    self.idling_counter -= 1
                    if self.idling_counter<=0:
                        self.idling = False
    
    
    
class ItemBox(pygame.sprite.Sprite):
    def __init__(self,item_type,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2,y + (TILE_SIZE - self.image.get_height()))

    def update(self):
            # pygame.draw.rect(screen,RED,self.rect)
        if pygame.sprite.collide_rect(self, player1):
            if self.item_type == 'Health':
                player1.health += 25
                print(player1.health)
                if player1.health > player1.max_health:
                    player1.health = player1.max_health
            if self.item_type == 'Bullet':
                player1.ammo += 5
                # print(player1.health)
                # if player1.health > player1.max_health:
                #     player1.health = player1.max_health
        #delete the item box
        
            self.kill()

    
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_imgage
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        
    def update(self):
        self.rect.x += (self.direction * self.speed)
        
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        
            
        if pygame.sprite.spritecollide(player1,bullet_group,False):
            if player1.zinda:
                player1.health -= 10
                self.kill()
            
        
        for enemy in enemy_group:
            if enemy.health > 0:
                if pygame.sprite.spritecollide(enemy, bullet_group, False):
                    if enemy.zinda:
                        enemy.health -= 25
                        self.kill()
                
        

class Heathbar():
    def __init__(self,x,y,health,max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
    def draw(self,health):
        self.health = health
        ratio = self.health / self.max_health
        # pygame.draw.rect(screen, RED,(self.x,self.y,150,20))
        pygame.draw.rect(screen, (0,255,0),(player1.rect.x,player1.rect.y,40*ratio,5))
        
        for enemy in enemy_group:
            r = enemy.health / self.max_health
            pygame.draw.rect(screen, (255,0,0),(enemy.rect.x,enemy.rect.y,40*r,5))

bullet_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
       
# cordinmates of player
# x=200
# y=200
# scale=1
# img=pygame.image.load('Blue/Gunner_Blue_Idle.png')
# img=pygame.transform.scale(img,(img.get_width()*scale,img.get_height()*scale))
# rect=img.get_rect()
# rect.center=(x,y)
player1=Player('player',200,200,1,5,20)
health_bar = Heathbar(player1.rect.x,player1.rect.y,player1.health,player1.health)
enemy = Player('enemy',200,380,1,2,20)
enemy2 = Player('enemy',300,380,1,2,20)
enemy_group.add(enemy)
enemy_group.add(enemy2)
item_box = ItemBox('Health',500,380)
item_box2 = ItemBox('Bullet',600,380)
item_box_group.add(item_box)
item_box_group.add(item_box2)
left=False
right=False

run=True
while run:
    clock.tick(fps)
    
    # screen.blit(player.img,player.rect)
    draw_bg()
    # draw_text(f'HEALTH:{player1.health}',font,RED,10,60)
    health_bar.draw(player1.health)
    draw_text(f'AMMO: ',font,(0,255,255),10,35)
    for x in range(player1.ammo):
        screen.blit(bullet_imgage,(90 + (x*10),40))
        
    player1.draw()
    player1.update()
    
    item_box_group.update()
    item_box_group.draw(screen)
    
    for enemy in enemy_group:
        enemy.ai()
        enemy.update()
        enemy.draw()
    
    
    bullet_group.update()
    bullet_group.draw(screen)
    
    
    if player1.zinda:
        if shoot:
            player1.shoot()
        if left or right:
            player1.change_action("Run")
        else:
            player1.change_action("Idle")
        player1.move(left,right)
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                # player.rect.x-=10
                left=True
            if event.key==pygame.K_RIGHT:
                # player.rect.x+=10
                right=True
            if event.key==pygame.K_UP and player1.zinda:
                # player1.rect.y-=10
                # print('jump')
                player1.jump=True
            if event.key== pygame.K_SPACE:
                shoot = True
            # if event.key==pygame.K_DOWN:
            #     player.rect.y+=10
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                # player.rect.x-=10
                left=False
            if event.key==pygame.K_RIGHT:
                # player.rect.x+=10
                right=False
            if event.key== pygame.K_SPACE:
                shoot = False
            
    pygame.display.update()


pygame.quit()