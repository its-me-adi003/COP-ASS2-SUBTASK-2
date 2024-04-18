import pygame
import button
import csv
clock=pygame.time.Clock()
FPS=60
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
# SCREEN_HEIGHT,SCREEN_WIDTH=pygame.display.Info().current_h,pygame.display.Info().current_w
LOWER_MARGIN=100
SIDE_MARGIN=300
# SIDE_MARGIN=300
# screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT+LOWER_MARGIN))
screen=pygame.display.set_mode((SCREEN_WIDTH+SIDE_MARGIN,SCREEN_HEIGHT+LOWER_MARGIN))
tiletype=27
scroll_left=False
scroll_right=False
scroll=0
current_tile=0
rows=16
max_cols=150
level=0
tile_size=SCREEN_HEIGHT//rows
save=pygame.image.load('save_btn.png').convert_alpha()
savebutton=button.Button(SCREEN_WIDTH//2,SCREEN_HEIGHT+LOWER_MARGIN-50,save,1)
load=pygame.image.load('load_btn.png').convert_alpha()
loadbutton=button.Button(SCREEN_WIDTH//2+200,SCREEN_HEIGHT+LOWER_MARGIN-50,load,1)
pygame.display.set_caption('Level Editor')

prison=pygame.image.load('prison.png').convert_alpha()

imglist=[]
for x in range(tiletype):
    img=pygame.image.load(f'tile/{x}.png')
    img=pygame.transform.scale(img,(tile_size,tile_size))
    imglist.append(img)

#tile list
grid=[]
r=[-1]*max_cols
for x in range(rows):
    grid.append(r.copy())
#for tile in range(max_cols):
   # grid[rows-1][tile]=0
# with open("grid.txt", "w") as file:
    # for row in grid:
    #     file.write(" ".join(map(str, row)) + "\n")

#create groung

def draw_world():
    for y,row in enumerate(grid):
        for x,tile in enumerate(row):
            if tile>=0:
                screen.blit(imglist[tile],(x*tile_size-scroll,y*tile_size))

def drawbg():
    screen.fill((255,255,255))
    width=prison.get_width()
    for x in range(4):
        screen.blit(prison,(x*width-scroll,0))
       

def draw_grid():
    for c in range(max_cols+1):
        pygame.draw.line(screen,(0,0,0),(c*tile_size-scroll,0),(c*tile_size-scroll,SCREEN_HEIGHT))
    for c in range(rows+1):
        pygame.draw.line(screen,(0,0,0),(0,c*tile_size),(SCREEN_WIDTH,c*tile_size))

button_list=[]
button_row=0
button_col=0
for i in range(len(imglist)):
    tile_button=button.Button(SCREEN_WIDTH+50+button_col*75,50+button_row*75,imglist[i],1)
    button_list.append(tile_button)
    button_col+=1
    if button_col==3:
        button_row+=1
        button_col=0

def draw_text(text,font,color,x,y):
    textobj=font.render(text,1,color)
    screen.blit(textobj,(x,y))

run = True
while run:
    clock.tick(FPS)
    drawbg()
    draw_grid()
    draw_world()
    draw_text(f'Level: {level}',pygame.font.SysFont('comicsans',30),(200,25,25),10,SCREEN_HEIGHT+LOWER_MARGIN-90)
    draw_text('Press up or down to change level',pygame.font.SysFont('comicsans',30),(200,25,25),10,SCREEN_HEIGHT+LOWER_MARGIN-60)
    if savebutton.draw(screen):
        with open(f'level{level}_data.csv','w',newline='') as csvfile:
            writer=csv.writer(csvfile,delimiter=',')
            for row in grid:
                writer.writerow(row)
    if loadbutton.draw(screen):
        scroll=0
        with open(f'level{level}_data.csv',newline='') as csvfile:
            reader=csv.reader(csvfile,delimiter=',')
            for x,row in enumerate(reader):
                for y,tile in enumerate(row):
                    grid[x][y]=int(tile)
        
    pygame.draw.rect(screen,(255,255,255),(SCREEN_WIDTH,0,SIDE_MARGIN,SCREEN_HEIGHT))
    button_count=0
    for button_count,i in enumerate(button_list):
        if i.draw(screen):
            current_tile=button_count
    pygame.draw.rect(screen,(200,25,25),button_list[current_tile].rect,3)
    # print(current_tile)
    if scroll_left==True and scroll>0:
        scroll-=5
    if scroll_right==True and scroll<4*SCREEN_WIDTH:
        scroll+=5

    # adding tile
    position=pygame.mouse.get_pos()
    x=(position[0]+scroll)//tile_size
    y=position[1]//tile_size
    if position[0]<SCREEN_WIDTH and position[1]<SCREEN_HEIGHT:
        if pygame.mouse.get_pressed()[0]==1:
            grid[y][x]=current_tile
        if pygame.mouse.get_pressed()[2]==1:
            grid[y][x]=-1
        
    # print(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                level+=1
            if event.key==pygame.K_DOWN and level>0:
                level-=1
            if event.key==pygame.K_LEFT:
                scroll_left=True
                scroll_right=False
            if event.key==pygame.K_RIGHT:
                scroll_right=True
                scroll_left=False
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                scroll_left=False
            if event.key==pygame.K_RIGHT:
                scroll_right=False
                
    pygame.display.update()

pygame.quit()
