import pygame
import sys
import subprocess
import cv2
import player
from moviepy.editor import VideoFileClip
# Initialize Pygame
pygame.init()
pygame.mixer_music.load('musicpoc.mp3')
pygame.mixer_music.play(-1)
# Screen dimensions



def playvideo(video_path):
    clip = VideoFileClip(video_path)
    clip.preview()
    clip.close()
def level():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    # SCREEN_WIDTH_SAHU = 1000
    # SCREEN_HEIGHT_SAHU = 800
    # SCREEN_HEIGHT,SCREEN_WIDTH=pygame.display.Info().current_h,pygame.display.Info().current_w
    background_image = pygame.image.load('levelbg1.png')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Game Cover Page')
    screen.blit(background_image, (0, 0)) 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    pygame.quit()
                    subprocess.run(['python3', 'player.py'])
                    sys.exit()
                    # call game 
        pygame.display.update()
def level1():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    # background_image = pygame.image.load('levelbg.jpg')
    background_image = pygame.image.load('levelbg1.png')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    button_sound=pygame.mixer.Sound('clickbutton.mp3')
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BUTTON_WIDTH = 0.08*SCREEN_WIDTH
    BUTTON_HEIGHT = SCREEN_HEIGHT/12
    BUTTON_BORDER = 5
    PLAY_BUTTON_X = (0) 
    PLAY_BUTTON_Y = SCREEN_HEIGHT/1.5+1.25*(BUTTON_HEIGHT+BUTTON_BORDER)
    EXIT_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH)
    EXIT_BUTTON_Y = (SCREEN_HEIGHT/1.5)+1.25*(BUTTON_HEIGHT+BUTTON_BORDER)
    level1_button_x=(SCREEN_WIDTH-BUTTON_WIDTH)//2
    level1_button_y=(SCREEN_HEIGHT//2-2*BUTTON_HEIGHT)
    level2_button_x=(SCREEN_WIDTH-BUTTON_WIDTH)//2
    level2_button_y=(SCREEN_HEIGHT//2-BUTTON_HEIGHT)
    level3_button_x=(SCREEN_WIDTH-BUTTON_WIDTH)//2
    level3_button_y=(SCREEN_HEIGHT//2)
    level4_button_x=(SCREEN_WIDTH-BUTTON_WIDTH)//2
    level4_button_y=(SCREEN_HEIGHT//2+BUTTON_HEIGHT)
    level5_button_x=(SCREEN_WIDTH-BUTTON_WIDTH)//2
    level5_button_y=(SCREEN_HEIGHT//2+2*BUTTON_HEIGHT)
    next_button_img = pygame.image.load('prev1.png')
    level1_img = pygame.image.load('level1.png')
    level2_img = pygame.image.load('level2.png')
    level3_img = pygame.image.load('level3.png')
    level4_img = pygame.image.load('level4.png')
    level5_img = pygame.image.load('level5.png')
    prev_button_img = pygame.image.load('next1.png')
    

    # Scale button images
    # next_button_img = pygame.transform.scale(next_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    # prev_button_img = pygame.transform.scale(prev_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    # level1_img = pygame.transform.scale(level1_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    # level2_img = pygame.transform.scale(level2_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    # level3_img = pygame.transform.scale(level3_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    # level4_img = pygame.transform.scale(level4_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    # level5_img = pygame.transform.scale(level5_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Game Cover Page')
    screen.blit(background_image, (0, 0))    
    selected_button = 'LEVEL1'
    
    while True:
        # draw_buttons(selected_button,screen,background_image,PLAY_BUTTON_X,PLAY_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT,next_button_img,BUTTON_BORDER,prev_button_img,EXIT_BUTTON_X,EXIT_BUTTON_Y)
        # draw_buttons1(selected_button,screen,background_image,PLAY_BUTTON_X,PLAY_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT,next_button_img,BUTTON_BORDER,prev_button_img,EXIT_BUTTON_X,EXIT_BUTTON_Y,level1_img,level1_button_x,level1_button_y,level2_img,level2_button_x,level2_button_y,level3_img,level3_button_x,level3_button_y,level4_img,level4_button_x,level4_button_y,level5_img,level5_button_x,level5_button_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()
                # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #     button_sound.play()
                #     if selected_button=='LEVEL1' and event.key == pygame.K_RIGHT:
                #         selected_button = 'EXIT'
                #     elif selected_button=='LEVEL2' and event.key == pygame.K_RIGHT:
                #         selected_button = 'EXIT'
                #     elif selected_button=='LEVEL3' and event.key == pygame.K_RIGHT:
                #         selected_button = 'EXIT'
                #     elif selected_button=='LEVEL4' and event.key == pygame.K_RIGHT:
                #         selected_button = 'EXIT'
                #     elif selected_button=='LEVEL5' and event.key == pygame.K_RIGHT:
                #         selected_button = 'EXIT'
                #     if selected_button=='LEVEL1' and event.key == pygame.K_LEFT:
                #         selected_button = 'PLAY'
                #     elif selected_button=='LEVEL2' and event.key == pygame.K_LEFT:
                #         selected_button = 'PLAY'
                #     elif selected_button=='LEVEL3' and event.key == pygame.K_LEFT:
                #         selected_button = 'PLAY'
                #     elif selected_button=='LEVEL4' and event.key == pygame.K_LEFT:
                #         selected_button = 'PLAY'
                #     elif selected_button=='LEVEL5' and event.key == pygame.K_LEFT:
                #         selected_button = 'PLAY'
                #     elif selected_button == 'PLAY' and event.key == pygame.K_RIGHT:
                #         selected_button = 'LEVEL1'
                #     elif selected_button == 'EXIT' and event.key == pygame.K_LEFT:
                #         selected_button = 'LEVEL1'
                #     # selected_button = 'EXIT' if selected_button == 'PLAY' else 'PLAY'
                # elif event.key == pygame.K_RETURN:
                #     if selected_button == 'PLAY':
                #         timeline3()
                #     elif selected_button == 'EXIT':
                #         # call game
                #         pygame.quit()
                #         sys.exit()
                #     elif selected_button == 'LEVEL1':
                #         # level1
                #         print('level 1')
                #     elif selected_button == 'LEVEL2':
                #         print('level 2')
                #     elif selected_button == 'LEVEL3':
                #         print('level 3')
                #     elif selected_button == 'LEVEL4':
                #         print('level 4')
                #     elif selected_button == 'LEVEL5':
                #         print('level 5')
                # elif event.key == pygame.K_UP:
                #     button_sound.play()
                #     if selected_button == 'LEVEL1':
                #         selected_button = 'LEVEL5'
                #     elif selected_button == 'LEVEL2':
                #         selected_button = 'LEVEL1'
                #     elif selected_button == 'LEVEL3':
                #         selected_button = 'LEVEL2'
                #     elif selected_button == 'LEVEL4':
                #         selected_button = 'LEVEL3'
                #     elif selected_button == 'LEVEL5':
                #         selected_button = 'LEVEL4'
                # elif event.key == pygame.K_DOWN:
                #     button_sound.play()
                #     if selected_button == 'LEVEL1':
                #         selected_button = 'LEVEL2'
                #     elif selected_button == 'LEVEL2':
                #         selected_button = 'LEVEL3'
                #     elif selected_button == 'LEVEL3':
                #         selected_button = 'LEVEL4'
                #     elif selected_button == 'LEVEL4':
                #         selected_button = 'LEVEL5'
                #     elif selected_button == 'LEVEL5':
                #         selected_button = 'LEVEL1'
        pygame.display.update()


def draw_buttons1(selected_button,screen,background_image,PLAY_BUTTON_X,PLAY_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT,play_button_img,BUTTON_BORDER,exit_button_img,EXIT_BUTTON_X,EXIT_BUTTON_Y,level1_img,level1_button_x,level1_button_y,level2_img,level2_button_x,level2_button_y,level3_img,level3_button_x,level3_button_y,level4_img,level4_button_x,level4_button_y,level5_img,level5_button_x,level5_button_y):
    screen.blit(background_image, (0, 0))
    if selected_button == 'LEVEL1':
        pygame.draw.rect(screen, (128,128,128,0), (level1_button_x, level1_button_y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(level1_img, (level1_button_x+BUTTON_BORDER, level1_button_y+BUTTON_BORDER))
        screen.blit(level2_img, (level2_button_x, level2_button_y))
        screen.blit(level3_img, (level3_button_x, level3_button_y))
        screen.blit(level4_img, (level4_button_x, level4_button_y))
        screen.blit(level5_img, (level5_button_x, level5_button_y))
        screen.blit(exit_button_img, (EXIT_BUTTON_X, EXIT_BUTTON_Y))
        screen.blit(play_button_img, (PLAY_BUTTON_X, PLAY_BUTTON_Y))
    elif selected_button == 'LEVEL2':
        pygame.draw.rect(screen, (128,128,128,0), (level2_button_x, level2_button_y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(level2_img, (level2_button_x+BUTTON_BORDER, level2_button_y+BUTTON_BORDER))
        screen.blit(level1_img, (level1_button_x, level1_button_y))
        screen.blit(level3_img, (level3_button_x, level3_button_y))
        screen.blit(level4_img, (level4_button_x, level4_button_y))
        screen.blit(level5_img, (level5_button_x, level5_button_y))
        screen.blit(exit_button_img, (EXIT_BUTTON_X, EXIT_BUTTON_Y))
        screen.blit(play_button_img, (PLAY_BUTTON_X, PLAY_BUTTON_Y))
    elif selected_button == 'LEVEL3':
        pygame.draw.rect(screen, (128,128,128,0), (level3_button_x, level3_button_y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(level3_img, (level3_button_x+BUTTON_BORDER, level3_button_y+BUTTON_BORDER))
        screen.blit(level2_img, (level2_button_x, level2_button_y))
        screen.blit(level1_img, (level1_button_x, level1_button_y))
        screen.blit(level4_img, (level4_button_x, level4_button_y))
        screen.blit(level5_img, (level5_button_x, level5_button_y))
        screen.blit(exit_button_img, (EXIT_BUTTON_X, EXIT_BUTTON_Y))
        screen.blit(play_button_img, (PLAY_BUTTON_X, PLAY_BUTTON_Y))
    elif selected_button == 'LEVEL4':
        pygame.draw.rect(screen, (128,128,128,0), (level4_button_x, level4_button_y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(level4_img, (level4_button_x+BUTTON_BORDER, level4_button_y+BUTTON_BORDER))
        screen.blit(level2_img, (level2_button_x, level2_button_y))
        screen.blit(level3_img, (level3_button_x, level3_button_y))
        screen.blit(level1_img, (level1_button_x, level1_button_y))
        screen.blit(level5_img, (level5_button_x, level5_button_y))
        screen.blit(exit_button_img, (EXIT_BUTTON_X, EXIT_BUTTON_Y))
        screen.blit(play_button_img, (PLAY_BUTTON_X, PLAY_BUTTON_Y))
    elif selected_button == 'LEVEL5':
        pygame.draw.rect(screen, (128,128,128,0), (level5_button_x, level5_button_y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(level5_img, (level5_button_x+BUTTON_BORDER, level5_button_y+BUTTON_BORDER))
        screen.blit(level2_img, (level2_button_x, level2_button_y))
        screen.blit(level3_img, (level3_button_x, level3_button_y))
        screen.blit(level4_img, (level4_button_x, level4_button_y))
        screen.blit(level1_img, (level1_button_x, level1_button_y))
        screen.blit(exit_button_img, (EXIT_BUTTON_X, EXIT_BUTTON_Y))
        screen.blit(play_button_img, (PLAY_BUTTON_X, PLAY_BUTTON_Y))
    elif selected_button == 'PLAY':
        pygame.draw.rect(screen,(128,128,128,0), (PLAY_BUTTON_X, PLAY_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(play_button_img, (PLAY_BUTTON_X+BUTTON_BORDER, PLAY_BUTTON_Y+BUTTON_BORDER))
        screen.blit(exit_button_img, (EXIT_BUTTON_X, EXIT_BUTTON_Y))
        screen.blit(level1_img, (level1_button_x, level1_button_y))
        screen.blit(level2_img, (level2_button_x, level2_button_y))
        screen.blit(level3_img, (level3_button_x, level3_button_y))
        screen.blit(level4_img, (level4_button_x, level4_button_y))
        screen.blit(level5_img, (level5_button_x, level5_button_y))
    elif selected_button == 'EXIT':
        pygame.draw.rect(screen, (128,128,128,0), (EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(exit_button_img, (EXIT_BUTTON_X+BUTTON_BORDER, EXIT_BUTTON_Y+BUTTON_BORDER))
        screen.blit(play_button_img, (PLAY_BUTTON_X, PLAY_BUTTON_Y))
        screen.blit(level1_img, (level1_button_x, level1_button_y))
        screen.blit(level2_img, (level2_button_x, level2_button_y))
        screen.blit(level3_img, (level3_button_x, level3_button_y))
        screen.blit(level4_img, (level4_button_x, level4_button_y))
        screen.blit(level5_img, (level5_button_x, level5_button_y))
    pygame.display.update()

def draw_buttons(selected_button,screen,background_image,PLAY_BUTTON_X,PLAY_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT,play_button_img,BUTTON_BORDER,exit_button_img,EXIT_BUTTON_X,EXIT_BUTTON_Y):
    screen.blit(background_image, (0, 0))
    
    if selected_button == 'PLAY':
        pygame.draw.rect(screen,(128,128,128,0), (PLAY_BUTTON_X, PLAY_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(play_button_img, (PLAY_BUTTON_X+BUTTON_BORDER, PLAY_BUTTON_Y+BUTTON_BORDER))
        screen.blit(exit_button_img, (EXIT_BUTTON_X, EXIT_BUTTON_Y))
    elif selected_button == 'EXIT':
        pygame.draw.rect(screen, (128,128,128,0), (EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(exit_button_img, (EXIT_BUTTON_X+BUTTON_BORDER, EXIT_BUTTON_Y+BUTTON_BORDER))
        screen.blit(play_button_img, (PLAY_BUTTON_X, PLAY_BUTTON_Y))
    
    pygame.display.update()

def timeline3():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    # SCREEN_HEIGHT,SCREEN_WIDTH=pygame.display.Info().current_h,pygame.display.Info().current_w
    # Load background image
    background_image = pygame.image.load('timeline3bg.jpg')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    button_sound=pygame.mixer.Sound('clickbutton.mp3')
    # Colors
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    # Button dimensions

    # BUTTON_WIDTH = 200
    BUTTON_WIDTH = 0.08*SCREEN_WIDTH
    # BUTTON_HEIGHT = 50
    BUTTON_HEIGHT = SCREEN_HEIGHT/12
    BUTTON_BORDER = 5
    # Button positions
    PLAY_BUTTON_X = (0) 
    PLAY_BUTTON_Y = SCREEN_HEIGHT/1.5+1.25*(BUTTON_HEIGHT+BUTTON_BORDER)
    # PLAY_BUTTON_Y = 50
    EXIT_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH)
    EXIT_BUTTON_Y = (SCREEN_HEIGHT/1.5)+1.25*(BUTTON_HEIGHT+BUTTON_BORDER)
    # EXIT_BUTTON_Y = 110

    # Load button images
    next_button_img = pygame.image.load('prev1.png')
    # play_button_img = pygame.image.load('play_button.png')
    prev_button_img = pygame.image.load('next1.png')
    # exit_button_img = pygame.image.load('exit_button.png')

    # Scale button images
    next_button_img = pygame.transform.scale(next_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    prev_button_img = pygame.transform.scale(prev_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))

    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Game Cover Page')
    selected_button = 'PLAY'

    while True:
        # draw_buttons(selected_button)
        draw_buttons(selected_button,screen,background_image,PLAY_BUTTON_X,PLAY_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT,next_button_img,BUTTON_BORDER,prev_button_img,EXIT_BUTTON_X,EXIT_BUTTON_Y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    button_sound.play()
                    selected_button = 'EXIT' if selected_button == 'PLAY' else 'PLAY'
                elif event.key == pygame.K_RETURN:
                    if selected_button == 'PLAY':
                        # print('Starting the game...')
                        # Add your game starting logic here
                        # subprocess.run(["python3", "timeline2.py"])
                        timeline2()
                        # pygame.quit()
                        # sys.exit()
                    elif selected_button == 'EXIT':
                        # video = cv2.VideoCapture('timetravel.mp4')
                        # subprocess.run(["python3", "levels.py"])
                        # print('Exiting the game...')
                        pygame.mixer_music.pause()
                        playvideo('timetravel2.mp4')
                        pygame.mixer_music.unpause()
                        level()
                        # pygame.quit()
                        # sys.exit()


def timeline2():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    SCREEN_HEIGHT,SCREEN_WIDTH=pygame.display.Info().current_h,pygame.display.Info().current_w
    # Load background image
    background_image = pygame.image.load('timeline2bg.jpg')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    button_sound=pygame.mixer.Sound('clickbutton.mp3')
    # Colors
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    # Button dimensions

    # BUTTON_WIDTH = 200
    BUTTON_WIDTH = 0.08*SCREEN_WIDTH
    # BUTTON_HEIGHT = 50
    BUTTON_HEIGHT = SCREEN_HEIGHT/12
    BUTTON_BORDER = 5
    # Button positions
    PLAY_BUTTON_X = (0) 
    PLAY_BUTTON_Y = SCREEN_HEIGHT/1.5+1.25*(BUTTON_HEIGHT+BUTTON_BORDER)
    # PLAY_BUTTON_Y = 50
    EXIT_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH)
    EXIT_BUTTON_Y = (SCREEN_HEIGHT/1.5)+1.25*(BUTTON_HEIGHT+BUTTON_BORDER)
    # EXIT_BUTTON_Y = 110

    # Load button images
    next_button_img = pygame.image.load('prev1.png')
    # play_button_img = pygame.image.load('play_button.png')
    prev_button_img = pygame.image.load('next1.png')
    # exit_button_img = pygame.image.load('exit_button.png')

    # Scale button images
    next_button_img = pygame.transform.scale(next_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    prev_button_img = pygame.transform.scale(prev_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))

    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Game Cover Page')
    selected_button = 'PLAY'

    while True:
        draw_buttons(selected_button,screen,background_image,PLAY_BUTTON_X,PLAY_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT,next_button_img,BUTTON_BORDER,prev_button_img,EXIT_BUTTON_X,EXIT_BUTTON_Y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    button_sound.play()
                    selected_button = 'EXIT' if selected_button == 'PLAY' else 'PLAY'
                elif event.key == pygame.K_RETURN:
                    if selected_button == 'PLAY':
                        # print('Starting the game...')
                        # Add your game starting logic here
                        # subprocess.run(["python3", "timeline.py"])
                        timeline()
                        # pygame.quit()
                        # sys.exit()
                    elif selected_button == 'EXIT':
                        # subprocess.run(["python3", "timeline3.py"])
                        timeline3()
                        # print('Exiting the game...')
                        # pygame.quit()
                        # sys.exit()


def timeline():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    # SCREEN_HEIGHT,SCREEN_WIDTH=pygame.display.Info().current_h,pygame.display.Info().current_w
    # Load background image
    background_image = pygame.image.load('timelinebg.jpg')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    button_sound=pygame.mixer.Sound('clickbutton.mp3')
    # Colors
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    # Button dimensions

    # BUTTON_WIDTH = 200
    BUTTON_WIDTH = 0.08*SCREEN_WIDTH
    # BUTTON_HEIGHT = 50
    BUTTON_HEIGHT = SCREEN_HEIGHT/12
    BUTTON_BORDER = 5
    # Button positions
    PLAY_BUTTON_X = (0) 
    PLAY_BUTTON_Y = SCREEN_HEIGHT/1.5+1.25*(BUTTON_HEIGHT+BUTTON_BORDER)
    # PLAY_BUTTON_Y = 50
    EXIT_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH)
    EXIT_BUTTON_Y = (SCREEN_HEIGHT/1.5)+1.25*(BUTTON_HEIGHT+BUTTON_BORDER)
    # EXIT_BUTTON_Y = 110

    # Load button images
    next_button_img = pygame.image.load('prev1.png')
    # play_button_img = pygame.image.load('play_button.png')
    prev_button_img = pygame.image.load('next1.png')
    # exit_button_img = pygame.image.load('exit_button.png')

    # Scale button images
    next_button_img = pygame.transform.scale(next_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    prev_button_img = pygame.transform.scale(prev_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))

    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Game Cover Page')
    selected_button = 'PLAY'

    while True:
        draw_buttons(selected_button,screen,background_image,PLAY_BUTTON_X,PLAY_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT,next_button_img,BUTTON_BORDER,prev_button_img,EXIT_BUTTON_X,EXIT_BUTTON_Y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    button_sound.play()
                    selected_button = 'EXIT' if selected_button == 'PLAY' else 'PLAY'
                elif event.key == pygame.K_RETURN:
                    if selected_button == 'PLAY':
                        # print('Starting the game...')
                        coverpage()
                        # Add your game starting logic here
                        # subprocess.run(["python3", "coverpage.py"])
                        # pygame.quit()
                        # sys.exit()
                    elif selected_button == 'EXIT':
                        # subprocess.run(["python3", "timeline2.py"])
                        timeline2()
                        # print('Exiting the game...')
                        # pygame.quit()
                        # sys.exit()

def coverpage():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    # SCREEN_HEIGHT,SCREEN_WIDTH=pygame.display.Info().current_h,pygame.display.Info().current_w
    # Load background image
    background_image = pygame.image.load('bg.jpg')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    button_sound=pygame.mixer.Sound('clickbutton.mp3')
    # Colors
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    # Button dimensions

    # BUTTON_WIDTH = 200
    BUTTON_WIDTH = 0.25*SCREEN_WIDTH
    # BUTTON_HEIGHT = 50
    BUTTON_HEIGHT = SCREEN_HEIGHT/12
    BUTTON_BORDER = 5
    # Button positions
    PLAY_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
    PLAY_BUTTON_Y = SCREEN_HEIGHT/1.5
    # PLAY_BUTTON_Y = 50
    EXIT_BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
    EXIT_BUTTON_Y = (SCREEN_HEIGHT/1.5)+1.25*(BUTTON_HEIGHT+BUTTON_BORDER)
    # EXIT_BUTTON_Y = 110

    # Load button images
    play_button_img = pygame.image.load('play.png')
    # play_button_img = pygame.image.load('play_button.png')
    exit_button_img = pygame.image.load('exit.png')
    # exit_button_img = pygame.image.load('exit_button.png')

    # Scale button images
    play_button_img = pygame.transform.scale(play_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
    exit_button_img = pygame.transform.scale(exit_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))

    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Game Cover Page')
    selected_button = 'PLAY'

    while True:
        draw_buttons(selected_button,screen,background_image,PLAY_BUTTON_X,PLAY_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT,play_button_img,BUTTON_BORDER,exit_button_img,EXIT_BUTTON_X,EXIT_BUTTON_Y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    button_sound.play()
                    selected_button = 'EXIT' if selected_button == 'PLAY' else 'PLAY'
                elif event.key == pygame.K_RETURN:
                    # fade_out(500)
                    if selected_button == 'PLAY':
                        print('Starting the game...')
                        # Add your game starting logic here
                        # subprocess.run(["python3", "timeline.py"])
                        timeline()
                        # pygame.quit()
                        # sys.exit()
                    elif selected_button == 'EXIT':
                        print('Exiting the game...')
                        pygame.quit()
                        sys.exit()

def main():
    coverpage()
   

if __name__ == '__main__':
    main()

