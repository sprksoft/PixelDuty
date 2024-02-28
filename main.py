import pygame
import sys
import time
# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_WIDTH = 600
GAME_HEIGHT = 500
CONSOLE_WIDTH = 200
CONSOLE_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PixelDuty")

# Font
font = pygame.font.Font(None, 36)

# Game loop
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        screen.fill(WHITE)
        title_text = font.render("PixelDuty", True, BLACK)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        start_text = font.render("Press any button to start", True, BLACK)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()

def game():
    console_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Command entered:", console_text)
                    console_text = "processing..."
                    time.sleep(1)
                    console_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    console_text = console_text[:-1]
                else:
                    console_text += event.unicode

        screen.fill(WHITE)
        console_surface = font.render(console_text, True, BLACK)
        screen.blit(console_surface, (GAME_WIDTH + 10, GAME_HEIGHT + 10))

        pygame.display.flip()

def main():
    main_menu()
    game()

if __name__ == "__main__":
    main()
