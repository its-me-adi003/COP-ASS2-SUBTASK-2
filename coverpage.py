import pygame
import sys
import subprocess
# Initialize Pygame
pygame.init()
pygame.mixer_music.load('musicpoc.mp3')
pygame.mixer_music.play(-1)
# Screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1080
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



def fade_out(duration):
    fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade_surface.blit(screen, (0, 0))  # Copy current screen content to fade surface
    for alpha in range(255, 0, -1):  # Decreased step size for slower fade
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(duration // 255)  # Adjusted delay for 255 steps



def draw_buttons(selected_button):
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

def main():
    selected_button = 'PLAY'

    while True:
        draw_buttons(selected_button)

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
                        subprocess.run(["python3", "timeline.py"])
                        pygame.quit()
                        sys.exit()
                    elif selected_button == 'EXIT':
                        print('Exiting the game...')
                        pygame.quit()
                        sys.exit()

if __name__ == '__main__':
    main()

