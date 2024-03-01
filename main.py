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

cams = [pygame.image.load('cam0.png'),pygame.image.load('cam1.png'),pygame.image.load('cam2.png')]
maxcamindex = len(cams)-1
activeanomalies = [["bathroom", "fire"], ["bedroom", "fire"], ["kitchen", "fire"]]

new_array = ["bedroom", "water"]
activeanomalies.append(new_array)

print(activeanomalies)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PixelDuty")

font = pygame.font.Font(None, 20)

def remove_anomaly(anomaly):
    activeanomalies.remove(anomaly)
    return

def handle_console(user_input): 
    if len(user_input.split(" ")) != 2:
        print("Invalid command")
        return
    location = user_input.split(" ")[0]
    anomaly = user_input.split(" ")[1].strip()
    if location in ["bathroom", "bedroom", "kitchen"]:
        anomaly_found = False
        for active_anomaly in activeanomalies:
            if [location, anomaly] == active_anomaly:
                anomaly_found = True
                break
        if anomaly_found:
            remove_anomaly([location, anomaly])
        else:
            print("Anomaly not active")
    else:
        return

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





def renderbase(camnumber):
    image_rect = cams[camnumber].get_rect()
    cams[camnumber].convert
    image_rect.center = (SCREEN_WIDTH // 2,SCREEN_HEIGHT // 2)
    screen.blit(cams[camnumber],image_rect)

def game():
    currentcam = 0
    console_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Command entered:", console_text)
                    handle_console(console_text)
                    console_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    console_text = console_text[:-1]
                elif event.key == pygame.K_LEFT:
                    currentcam -= 1
                    if currentcam < 0:
                        currentcam = maxcamindex
                elif event.key == pygame.K_RIGHT:
                    currentcam += 1
                    if currentcam > maxcamindex:
                        currentcam = 0
                else:
                    console_text += event.unicode
        renderbase(currentcam)    
        console_surface = font.render(console_text, True, BLACK)
        screen.blit(console_surface, (GAME_WIDTH + 10, GAME_HEIGHT + 10))

        pygame.display.flip()

def main():
    main_menu()
    game()

if __name__ == "__main__":
    main()
