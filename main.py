import pygame
print(pygame.version.ver)
import sys
import time
import random
import threading
import anomalies
import math
# Initialize Pygame
pygame.init()

# Screen dimensions
IMAGE_WIDTH = 160
IMAGE_HEIGHT = 90
CELL_WIDTH = 10
SCREEN_WIDTH = IMAGE_WIDTH * CELL_WIDTH
SCREEN_HEIGHT = IMAGE_HEIGHT * CELL_WIDTH
CONSOLE_WIDTH = 50 * CELL_WIDTH
CONSOLE_HEIGHT = 10 * CELL_WIDTH

cams = [pygame.image.load('cam0.png'), pygame.image.load('cam1.png'), pygame.image.load('cam2.png')]
cams_rooms = {
    cams[0]: "bathroom",
    cams[1]: "bedroom",
    cams[2]: "kitchen"
}
maxcamindex = len(cams) - 1
activeanomalies = []
high_anomaly_time = None
available_anomalies = [["bathroom", "plant"],["bathroom", "rug"],["bathroom", "mirror"],["bathroom", "toiletpaper"],["bathroom", "boxes"],["bathroom", "sink"],["kitchen", "sink"],["kitchen", "fridge"],["kitchen", "microwave"],["kitchen", "items"],["kitchen", "towel"],["kitchen", "utensils"],["bedroom", "bed"],["bedroom", "bookshelf"],["bedroom", "lamp"],["bedroom", "window"],["bedroom", "rug"],["bedroom", "plant"],["bedroom", "bomb"]]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PixelDuty")

font = pygame.font.Font(None, 40)

stop_event = threading.Event()

def remove_anomaly(anomaly):
    activeanomalies.remove(anomaly)
    available_anomalies.append(anomaly)


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


def renderAnomalies(camnumber, room, anomaly_type):
    cam = cams[camnumber]
    if cams_rooms.get(cam) == room:
        return anomalies.renderAnomaly(anomaly_type, room)
def dontRenderAnomalies(camnumber, room, anomaly_type):
    cam = cams[camnumber]
    if cams_rooms.get(cam) == room:
        return anomalies.dontRenderAnomaly(anomaly_type, room)


def renderbase(camnumber, console_text):

    cam_image = cams[camnumber]

    width_scale_factor = SCREEN_WIDTH / cam_image.get_width()
    height_scale_factor = SCREEN_HEIGHT / cam_image.get_height()

    scale_factor = min(width_scale_factor, height_scale_factor)

    scaled_cam_width = int(cam_image.get_width() * scale_factor)
    scaled_cam_height = int(cam_image.get_height() * scale_factor)
    scaled_cam = pygame.transform.scale(cam_image, (scaled_cam_width, scaled_cam_height))

    screen.blit(scaled_cam, ((SCREEN_WIDTH - scaled_cam_width) // 2, (SCREEN_HEIGHT - scaled_cam_height) // 2))
    activeanomalies.sort()
    activeanomalies.reverse()
    for anomaly in activeanomalies:
        room = anomaly[0]
        anomaly_type = anomaly[1]
        anomaly_surface = renderAnomalies(camnumber, room, anomaly_type)
        if anomaly_surface is not None:
            screen.blit(anomaly_surface[0], anomaly_surface[1])

    for anomaly in available_anomalies:
        room = anomaly[0]
        anomaly_type = anomaly[1]
        anomaly_surface = dontRenderAnomalies(camnumber, room, anomaly_type)
        if anomaly_surface is not None:
            screen.blit(anomaly_surface[0], anomaly_surface[1])

    console_rect = pygame.Rect(SCREEN_WIDTH - CONSOLE_WIDTH, SCREEN_HEIGHT - CONSOLE_HEIGHT, CONSOLE_WIDTH, CONSOLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, console_rect)

    console_surface = font.render(console_text, True, BLACK)
    screen.blit(console_surface, (console_rect.x + 10, console_rect.y + 10))


def createAnomaly(multiplier):
    global available_anomalies
    time.sleep(1)
    while not stop_event.is_set():
        if random.random() < (0.1 * multiplier):
            if available_anomalies:
                chosen_anomaly_index = random.randint(0, len(available_anomalies) - 1)
                chosen_anomaly = available_anomalies[chosen_anomaly_index]
                activeanomalies.append(chosen_anomaly)
                available_anomalies.remove(chosen_anomaly)
                print(chosen_anomaly)
                multiplier = 1 
        multiplier += 0.1  
        print(round(multiplier*10))
        time.sleep(1)

def reset_game():
    global activeanomalies, available_anomalies
    stop_event.set() 
    activeanomalies = [] 
    available_anomalies = [] 
    main_menu()
    game()

def game():
    currentcam = 0
    console_text = ""
    global anomaly_thread
    stop_event.clear() 
    anomaly_thread = threading.Thread(target=createAnomaly, args=(1,))
    anomaly_thread.start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                reset_game()
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

        renderbase(currentcam, console_text)

        pygame.display.flip()


def main():
    main_menu()
    game()


if __name__ == "__main__":
    main()