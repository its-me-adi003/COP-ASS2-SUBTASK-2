import pygame
import sys
import subprocess
# Initialize Pygame
pygame.init()
# pygame.mixer_music.load('musicpoc.mp3')
# pygame.mixer_music.play(-1)
# Screen dimensions
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

def draw_buttons(selected_button):
    screen.blit(background_image, (0, 0))
    
    if selected_button == 'PLAY':
        pygame.draw.rect(screen,(128,128,128,0), (PLAY_BUTTON_X, PLAY_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(next_button_img, (PLAY_BUTTON_X+BUTTON_BORDER, PLAY_BUTTON_Y+BUTTON_BORDER))
        screen.blit(prev_button_img, (EXIT_BUTTON_X, EXIT_BUTTON_Y))
    elif selected_button == 'EXIT':
        pygame.draw.rect(screen, (128,128,128,0), (EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(prev_button_img, (EXIT_BUTTON_X+BUTTON_BORDER, EXIT_BUTTON_Y+BUTTON_BORDER))
        screen.blit(next_button_img, (PLAY_BUTTON_X, PLAY_BUTTON_Y))

    pygame.display.update()

def main():
    selected_button = 'PLAY'

    while True:
        draw_buttons(selected_button)

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
                        print('Starting the game...')
                        # Add your game starting logic here
                        subprocess.run(["python3", "coverpage.py"])
                        pygame.quit()
                        sys.exit()
                    elif selected_button == 'EXIT':
                        subprocess.run(["python3", "timeline2.py"])
                        # print('Exiting the game...')
                        pygame.quit()
                        sys.exit()

if __name__ == '__main__':
    main()

