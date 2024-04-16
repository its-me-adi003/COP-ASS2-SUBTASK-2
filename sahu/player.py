import pygame
import csv
import os
import random
pygame.init()
clock=pygame.time.Clock()
fps=60
scroll_limit=200
s_scroll=0
bg_scroll=0
g=0.75
shoot=False
n_row=16
n_col=150
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = SCREEN_WIDTH*0.8
tile_size=SCREEN_HEIGHT//n_row
tiletypes=21
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('player')

images=[]
for x in range(tiletypes):
    temp=pygame.image.load(f'tile/{x}.png')
    temp=pygame.transform.scale(temp,(tile_size,tile_size))
    images.append(temp)


prison=pygame.image.load('prison.png').convert_alpha()
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

def draw_bg():
    screen.fill((255,255,255))
    width=prison.get_width()
    for x in range(4):
        screen.blit(prison,(x*width-bg_scroll*0.5,0))
        # screen.blit(prison,(x*width-s_scroll,0))
    # pygame.draw.line(screen,(255,0,0),(0,400),(SCREEN_WIDTH,400))

class Player(pygame.sprite.Sprite):
    def __init__(self,chart,x,y,scale,vel,ammo):
        # self.x=x
        # self.y=y
        # self.scale=scale
        pygame.sprite.Sprite.__init__(self)
        self.vel=vel
        self.chart=chart
        self.direction=1
        self.zinda=True
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.health = 100
        self.max_health = self.health
        self.jump=False
        self.animationl=[]
        self.idx=0
        self.vely=0
        self.inair=True
        self.move_counter=0
        self.vision = pygame.Rect(0,0,150,20)
        self.idling = False
        self.idling_counter = 0
        self.action=0
        temp=[]
        self.time=pygame.time.get_ticks()
        for i in range(5):
            self.img=pygame.image.load(f'Blue/idle/{i}.png')
            # img=pygame.transform.scale(img,(img.get_width()*scale,img.get_height()*scale))
            self.img=pygame.transform.scale(self.img,(self.img.get_width()*scale,self.img.get_height()*scale))
            temp.append(self.img)
        self.animationl.append(temp)
        temp=[]
        for i in range(6):
            self.img=pygame.image.load(f'Blue/run/{i}.png')
            # img=pygame.transform.scale(img,(img.get_width()*scale,img.get_height()*scale))
            self.img=pygame.transform.scale(self.img,(self.img.get_width()*scale,self.img.get_height()*scale))
            temp.append(self.img)
        self.animationl.append(temp)
        temp=[]
        for i in range(2):
            self.img=pygame.image.load(f'Blue/jump/{i}.png')
            # img=pygame.transform.scale(img,(img.get_width()*scale,img.get_height()*scale))
            self.img=pygame.transform.scale(self.img,(self.img.get_width()*scale,self.img.get_height()*scale))
            temp.append(self.img)
        self.animationl.append(temp)
        temp=[]
        for i in range(8):
            self.img=pygame.image.load(f'Death/{i}.png')
            # img=pygame.transform.scale(img,(img.get_width()*scale,img.get_height()*scale))
            self.img=pygame.transform.scale(self.img,(self.img.get_width()*scale,self.img.get_height()*scale))
            temp.append(self.img)
        self.animationl.append(temp)
        self.img=self.animationl[self.action][self.idx]
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
        self.img=self.animationl[self.action][self.idx]
        if pygame.time.get_ticks()-self.time>100:
            self.time=pygame.time.get_ticks()
            self.idx+=1
        if self.idx>=len(self.animationl[self.action]):
            if self.action==3: #doubt
                self.idx=len(self.animationl[self.action])-1
            else:
                self.idx=0
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
            self.change_action(3)
    def draw(self):
        screen.blit(pygame.transform.flip(self.img,self.flip,False),self.rect)
    def move(self,left,right):
        s_scroll=0
        dx=0
        dy=0
        if left:
            dx=-self.vel
            self.flip=True
            self.direction=-1   
        if right:
            dx=self.vel
            self.flip=False
            self.direction=1
        # if self.jump and self.inair==False:
        if self.jump :
            # print(self.jump)
            self.vely=-11
            # dy=-self.vely
            self.jump=False
            # self.inair=True
        self.vely+=g
        if self.vely>10:
            self.vely=10
        dy+=self.vely

        for i in basement.stoplist:
            if i[1].colliderect(self.rect.x+dx,self.rect.y,self.rect.width,self.rect.height):
                dx=0
            if i[1].colliderect(self.rect.x,self.rect.y+dy,self.rect.width,self.rect.height):
                if self.vely<0:
                    dy=i[1].bottom-self.rect.top
                else:
                    dy=i[1].top-self.rect.bottom
                    self.inair=False
                self.vely=0
        if self.rect.bottom+dy>(SCREEN_HEIGHT-tile_size):
            dy=(SCREEN_HEIGHT-tile_size)-self.rect.bottom
            self.vely=0
        self.rect.x+=dx
        self.rect.y+=dy
        if self.chart=='player':
            if self.rect.left+dx<0 or self.rect.right+dx>SCREEN_WIDTH:
                dx=0
            if (self.rect.right>SCREEN_WIDTH-scroll_limit and bg_scroll<(basement.lev_len*tile_size-SCREEN_WIDTH)) or (self.rect.left<scroll_limit and bg_scroll>abs(dx)):
                self.rect.x-=dx
                s_scroll=-dx
            return s_scroll
                # self.rect.right=SCREEN_WIDTH
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
                self.change_action(0)
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
                    
                    if self.move_counter > tile_size:
                        self.direction *= -1
                        self.move_counter *= -1
                        
                else:
                    self.idling_counter -= 1
                    if self.idling_counter<=0:
                        self.idling = False
        self.rect.x+=s_scroll



class ItemBox(pygame.sprite.Sprite):
    def __init__(self,item_type,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + tile_size // 2,y + (tile_size - self.image.get_height()))

    def update(self):
            # pygame.draw.rect(screen,RED,self.rect)
        self.rect.x+=s_scroll
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
        self.rect.x += (self.direction * self.speed)+s_scroll
        
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        
            
        if pygame.sprite.spritecollide(player1,bullet_group,False):
            if player1.zinda:
                player1.health -= 4
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



item_box_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
class Basement():
    def __init__(self):
        self.stoplist=[]
    def main(self,data):
        self.lev_len=len(data[0])
        for y,row in enumerate(data):
            for x,tile in enumerate(row):
                if tile>=0:
                    temp=images[tile]
                    temp_rect=temp.get_rect()
                    temp_rect.x=x*  tile_size 
                    temp_rect.y=y*  tile_size
                    temp2=(temp,temp_rect)
                    if tile<=8:
                        self.stoplist.append(temp2)
                    elif tile>=9 and tile<=14:
                        pass
                    elif tile==15:
                        myplayer=Player('player',x*tile_size,y*tile_size,1,5,20)
                        # add healthbar
                    elif tile==16:
                        enemy = Player('enemy',x*tile_size,y*tile_size,1,5,20)
                        enemy_group.add(enemy)
                    elif tile==17:
                        # grenade
                        item_box2 = ItemBox('Bullet',x*tile_size,y*tile_size)
                        item_box_group.add(item_box2)
                    elif tile==19:
                        # health
                        item_box = ItemBox('Health',x*tile_size,y*tile_size)
                        item_box_group.add(item_box)
                    elif tile==20:
                        pass
        return myplayer#,healthbar
    def draw(self):
        for i in self.stoplist:
            i[1][0]+=s_scroll
            screen.blit(i[0],i[1])


                        

        



level=0
grid=[]
r=[-1]*n_col
for x in range(n_row):
    grid.append(r.copy())
with open(f'level{level}_data.csv',newline='') as f:
    reader=csv.reader(f,delimiter=',')
    for x,row in enumerate(reader):
        for y,tile in enumerate(row):
            grid[x][y]=int(tile)
# print(grid)   
basement=Basement()
player=basement.main(grid)
bullet_group = pygame.sprite.Group()

player1=Player('player',200,200,1.5,5,20)
health_bar = Heathbar(player1.rect.x,player1.rect.y,player1.health,player1.health)

enemy2 = Player('enemy',300,380,1,2,20)

enemy_group.add(enemy2)


left=False
right=False

run=True
while run:
    clock.tick(fps)
    # screen.blit(player.img,player.rect)
    draw_bg()
    basement.draw()
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
    # player1.animation()
    if player1.zinda:
        if shoot:
            player1.shoot()
        if player1.inair:
            player1.change_action(2)
        elif left or right:
            player1.change_action(1)
        else:
            player1.change_action(0)
        s_scroll=player1.move(left,right)
        bg_scroll-=s_scroll
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
            # if event.key==pygame.K_DOWN:
            #     player.rect.y+=10
            if event.key== pygame.K_SPACE:
                shoot = True
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