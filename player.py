import pygame
from pygame import mixer
import csv
import os
import random
import pygame_gui.ui_manager
import sys
from pgu import gui
import time
pygame.init()
clock=pygame.time.Clock()
fps=60
pygame.mixer.music.load('sahu_music.mp3')
pygame.mixer.music.set_volume(0.05)  # Set volume to 50%
pygame.mixer.music.play(loops=-1)  # Play music indefinitely
scroll_limit=200
s_scroll=0
bg_scroll=0
g=0.75
shoot=False
n_row=16
n_col=150
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = SCREEN_WIDTH*0.8
# SCREEN_WIDTH = pygame.display.Info().current_w
# SCREEN_HEIGHT = pygame.display.Info().current_h
# screen = pygame.display.set_mode((screen_width, screen_height))
shootsound=pygame.mixer.Sound('shot.wav')
bonussound=pygame.mixer.Sound('bonus.wav')
explosionsound = pygame.mixer.Sound('explosionsound.mp3')
shootsound.set_volume(0.2)
bonussound.set_volume(0.1)
tile_size=SCREEN_HEIGHT//n_row
tiletypes=27
gcnt = 0
dead_by_explosion = False
paused=False
game_over = 0
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('player')
question1=pygame.image.load('question1.png')
question2=pygame.image.load('question2.png')
question3=pygame.image.load('question3.png')
question4=pygame.image.load('question4.png')
correct_ans=pygame.image.load('correct.png')
wrong_ans=pygame.image.load('wrong.png')
gameoverimg=pygame.image.load('gameover.png')
gamefinishimg=pygame.image.load('victory.png')
question_images=[]
question_images.append(question1)
question_images.append(question2)   
question_images.append(question3)
question_images.append(question4)
answers=[]
answer1="B"
answer2="D"
answer3="80"
answer4="A"
answers.append(answer1)
answers.append(answer2)
answers.append(answer3)
answers.append(answer4)
question_idx=0
images=[]
for x in range(tiletypes):
    temp=pygame.image.load(f'tile/{x}.png')
    temp=pygame.transform.scale(temp,(tile_size,tile_size))
    images.append(temp)
prison=pygame.image.load('prison.png').convert_alpha()
bullet_imgage = pygame.image.load("bullet.png")
health_box_img = pygame.image.load('health.png')
bullet_box_img = pygame.image.load('ammo_box.png')
question_img=pygame.image.load('question.png')
endpoint_img=pygame.image.load('endpoint.png')
item_boxes = {
    'Health' : health_box_img,
    "Bullet" : bullet_box_img,
    'Question':question_img,
    'Endpoint':endpoint_img

}

font  = pygame.font.SysFont('Futura',30)

def show_gameover():
    start_time = time.time()
                   
    while time.time() - start_time < 1: 
    #     # print(time.time())                      
        screen.blit(gameoverimg,(SCREEN_WIDTH//2-gameoverimg.get_width()//2,SCREEN_HEIGHT//2-gameoverimg.get_height()//2))                        
        pygame.display.update()
        # pass
    
    # screen.fill((255, 255, 255))  # Remove the image by filling the screen with white color
    # pygame.display.update()
    return

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
            # s_scroll=0
            self.health = 0
            self.speed = 0
            self.zinda = False
            self.change_action(3)
            # show_gameover()

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
        if self.jump and self.inair==False:
        # if self.jump :
            # print(self.jump)
            self.vely=-11
            # dy=-self.vely
            self.jump=False
            self.inair=True
        self.vely+=g
        if self.vely>10:
            self.vely=10
        if self.vely >= 10:
            self.inair = False
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
        if self.rect.bottom+dy>(SCREEN_HEIGHT):
            dy=(SCREEN_HEIGHT)-self.rect.bottom
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
            shootsound.play()
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
# def do_something(text):
def show_gamefinished():
    start_time = time.time()
                   
    while time.time() - start_time < 5: 
    #     # print(time.time())                      
        screen.blit(gamefinishimg,(SCREEN_WIDTH//2-gamefinishimg.get_width()//2,SCREEN_HEIGHT//2-gamefinishimg.get_height()//2))                        
        pygame.display.update()
        # pass
    
    # screen.fill((255, 255, 255))  # Remove the image by filling the screen with white color
    # pygame.display.update()
    return

def show_wrongans():
    start_time = time.time()
                   
    while time.time() - start_time < 1: 
        # print(time.time())                      
        screen.blit(wrong_ans,(SCREEN_WIDTH//2-wrong_ans.get_width()//2,SCREEN_HEIGHT//2-wrong_ans.get_height()//2))                        
        pygame.display.update()
        # pass
    
    # screen.fill((255, 255, 255))  # Remove the image by filling the screen with white color
    pygame.display.update()
    return
    
def get_text(self):
    global game_over
    global question_idx
    global dead_by_explosion
    height=400
    width=400
    global paused
    showquestion=True
    # temp_screen=pygame.display.set_mode((width,height))
    count=0
    # screen.blit(question1,(self.rect.x-question1.get_width()//3,self.rect.y-question1.get_height()))
    screen.blit(question_images[question_idx],(self.rect.x-question1.get_width()//(1.5),self.rect.y-question1.get_height()//(1.5)))
    manager=pygame_gui.UIManager((width,height))
    input=pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((100,100),(200,50)),manager=manager,object_id='#main_text_entry')
    while paused:
        # if showquestion:
        #     screen.blit(question1,(self.rect.x-question1.get_width()//3,self.rect.y-question1.get_height()))
        timebar.update2()
        # timebar.draw() 
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#main_text_entry'):
                # show_text(event.text)
                # do something(event.text,)
                print("given input")
                # if event.text==answer1:
                if event.text==answers[question_idx]:
                        print("correct answer")
                        question_idx+=1
                        count =0
                        player1.speed=0
                        start_time = time.time()
                        while time.time() - start_time < 2:
                            screen.blit(correct_ans,(SCREEN_WIDTH//2-correct_ans.get_width()//2,SCREEN_HEIGHT//2-correct_ans.get_height()//2))
                            pygame.display.update()
                            pass
                        paused = False
                        return
                elif count==1:
                    print("incorrect attempt")
                        #explosion
                    game_over = 1
                    explosionsound.play()
                    explosion=Explosion(self.rect.x+40,self.rect.y+60,6)
                    explosion_group.add(explosion)
                    # player1.zinda=False
                    player1.health=-1
                    dead_by_explosion = True
                    paused=False
                    return
                else:
                        # Empty the input by the user

                    event.text = ""
                    input.set_text("")
                    count+=1
                    # show_wrongans()
                    # print("rakshit")
                    


            
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        # temp_screen.fill("white")

        manager.draw_ui(screen)

        pygame.display.update()

class ItemBox(pygame.sprite.Sprite):
    def __init__(self,item_type,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + tile_size // 2,y + (tile_size - self.image.get_height()))

    def update(self):
        global paused
            # pygame.draw.rect(screen,RED,self.rect)
        self.rect.x+=s_scroll
        if pygame.sprite.collide_rect(self, player1):
            if self.item_type == 'Health':
                player1.health += 25
                bonussound.play()
                # print(player1.health)
                if player1.health > player1.max_health:
                    player1.health = player1.max_health
            if self.item_type == 'Bullet':
                player1.ammo += 5
                bonussound.play()
                # print(player1.health)
                # if player1.health > player1.max_health:
                #     player1.health = player1.max_health
            if self.item_type=='Question':
                print("question aaya")
                bonussound.play()
                print(paused)
                paused=True
                print(paused)
                player1.speed=0
                # while paused:
                #     screen.blit(question1,(self.rect.x-question1.get_width()//3,self.rect.y-question1.get_height()))
                get_text(self)
            if self.item_type=='Endpoint':
                print("endpoint")
                show_gamefinished()
                print("level completed")

                
                                    
                            
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


class Explosion (pygame.sprite.Sprite):
    def __init__(self,x,y,scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range (1,31):
            img = pygame.image.load(f"explode/{num}.png").convert_alpha()
            img = pygame.transform.scale(img,(img.get_width()*scale,img.get_height()*scale))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
    def update(self):
        explosion_speed = 1
        self.counter += 1
        if self.counter >= explosion_speed:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
                self.kill()
            else:
                self.image = self.images[self.index]
class Timebar():
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        # self.x-=s_scroll
        self.max_length = 300
        self.length = length
        self.last_update_time = pygame.time.get_ticks()
    def update(self):
        global game_over
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time >= 1000:
            self.length -= 1
            if self.length <0 :
                # print("decrease")
                player1.health = -1
                game_over=1
                explosionsound.play()
                explosion = Explosion(player1.rect.x + 40,player1.rect.y + 60,4)
                explosion_group.add_internal(explosion)
            self.last_update_time = current_time

    def update2(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time >= 1000:
            self.length -= 1
            self.last_update_time = current_time

    def draw(self):
        ratio = self.length/self.max_length
        
        for item in timebar_group:
            item.x += s_scroll
            pygame.draw.rect(screen,(255,255,0),(item.x + 30 ,item.y,40*ratio,5))

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
timebar_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
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
                    if tile==25 or tile==2 or (tile>=11 and tile<=24) or tile==0:
                        self.stoplist.append(temp2)
                    # elif (tile>=11 and tile<=24) or tile==0:
                    #     pass
                    elif tile==7:
                        myplayer=Player('player',x*tile_size,y*tile_size,1,5,20)
                        # add healthbar
                    elif tile==8:
                        enemy = Player('enemy',x*tile_size,y*tile_size,1,5,20)
                        enemy_group.add(enemy)
                    elif tile==9:
                        # grenade
                        item_box2 = ItemBox('Bullet',x*tile_size,y*tile_size)
                        item_box_group.add(item_box2)
                        
                    elif tile==10:
                        # health
                        item_box = ItemBox('Health',x*tile_size,y*tile_size)
                        item_box_group.add(item_box)
                        # bonussound.play()
                    elif tile==5:
                        # question
                        item_box = ItemBox('Question',x*tile_size,y*tile_size)
                        item_box_group.add(item_box)
                    if tile==0 or tile==15 or  tile==17:
                        timebar = Timebar(x*tile_size,y*tile_size,300)
                        timebar_group.add_internal(timebar)
                    if tile==26:
                        endpoint = ItemBox('Endpoint',x*tile_size,y*tile_size)
                        item_box_group.add(endpoint)
                        # display game complete
                        # pass
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
timebar=Timebar(100,100,300)
# enemy2 = Player('enemy',300,380,1.5,2,20)

# enemy_group.add(enemy2)


left=False
right=False
def main():
    global game_over
    global paused
    global shoot
    global left
    global right
    global bg_scroll
    global s_scroll
    global player1
    global timebar
    global question_idx
    global gcnt
    global dead_by_explosion
    run=True
    while run:
        clock.tick(fps)
        # screen.blit(player.img,player.rect)
        draw_bg()
        basement.draw()
        health_bar.draw(player1.health)
        draw_text(f'SHELLS: ',font,(255,255,0),10,35)
        for x in range(player1.ammo):
            screen.blit(bullet_imgage,(90 + (x*10),40))
        player1.draw()
        bullet_group.draw(screen)
        item_box_group.draw(screen)
        player1.update()
        if (game_over<2):
            timebar.draw()
            timebar.update()
        item_box_group.update()
        if player1.health < 1 and gcnt == 0 and (dead_by_explosion==False):
            show_gameover()
            gcnt =1
        if game_over<32 and game_over>0 :
            explosion_group.draw(screen)
            explosion_group.update()
            game_over += 1
            if game_over >= 32:
                start_time = time.time()
                while True:
                    
                    if time.time() - start_time >= 2:
                        screen.blit(gameoverimg, (SCREEN_WIDTH // 2 - gameoverimg.get_width() // 2, SCREEN_HEIGHT // 2 - gameoverimg.get_height() // 2))
                        pygame.display.update()
                        
                        if time.time() - start_time >=6 :
                            paused = True
                            break

        bullet_group.update()
        
        for enemy in enemy_group:
            if paused==False:
                enemy.ai()
                enemy.update()
            enemy.draw()
        
        # player1.animation()
        if player1.zinda and paused==False:
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
                if event.key==pygame.K_ESCAPE:
                    paused=not paused
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

if __name__ == '__main__':
    main()
pygame.quit()