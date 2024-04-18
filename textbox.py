import pygame
import sys
import pygame_gui
import pygame_gui.ui_manager
pygame.init()
height=400
width=400
screen=pygame.display.set_mode((width,height))
clk=pygame.time.Clock()
manager=pygame_gui.UIManager((width,height))
input=pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((100,100),(200,50)),manager=manager,object_id='#main_text_entry')
def show_text(text):
      while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("white")

        new_text = pygame.font.SysFont("bahnschrift", 100).render(f"{text}", True, "black")
        new_text_rect = new_text.get_rect(center=(width/2, height/2))
        screen.blit(new_text, new_text_rect)

        clk.tick(60)

        pygame.display.update()
def get_text():
    while True:
        UI_REFRESH_RATE = clk.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                show_text(event.text)
            
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        screen.fill("white")

        manager.draw_ui(screen)

        pygame.display.update()

get_text()