import pygame
import sys
import time
import random
import threading
import anomalies

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800
CONSOLE_WIDTH = 200
CONSOLE_HEIGHT = 100

cams = [pygame.image.load('cam0.png'), pygame.image.load('cam1.png'), pygame.image.load('cam2.png')]
cams_rooms = {
    cams[0]: "bathroom",
    cams[1]: "bedroom",
    cams[2]: "kitchen"
}
maxcamindex = len(cams) - 1
activeanomalies = []

available_anomalies = [["bathroom", "toilet"], ["bathroom", "door"]]

print(activeanomalies)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PixelDuty")

font = pygame.font.Font(None, 20)

# Thread event to signal anomaly thread to stop
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
            print("active anomalies: ", activeanomalies)
            print("available anomalies: ", available_anomalies)
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


def renderbase(camnumber):
    # Scale the camera image to cover the entire screen
    scaled_cam = pygame.transform.scale(cams[camnumber], (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_cam, (0, 0))
    
    # Render active anomalies
    for anomaly in activeanomalies:
        room = anomaly[0]
        anomaly_type = anomaly[1]
        anomaly_surface = renderAnomalies(camnumber, room, anomaly_type)
        if anomaly_surface is not None:
            screen.blit(anomaly_surface[0], anomaly_surface[1])
    
    # Render available anomalies (if needed)
    for anomaly in available_anomalies:
        room = anomaly[0]
        anomaly_type = anomaly[1]
        anomaly_surface = dontRenderAnomalies(camnumber, room, anomaly_type)
        if anomaly_surface is not None:
            screen.blit(anomaly_surface[0], anomaly_surface[1])

def createAnomaly(multiplier):
    global available_anomalies
    time.sleep(1)
    while not stop_event.is_set():
        if random.random() < (0.1 * multiplier):
            if available_anomalies:  # Check if available_anomalies is still not empty
                chosen_anomaly_index = random.randint(0, len(available_anomalies) - 1)
                print(chosen_anomaly_index)
                chosen_anomaly = available_anomalies[chosen_anomaly_index]
                activeanomalies.append(chosen_anomaly)
                available_anomalies.remove(chosen_anomaly)  # Remove chosen anomaly from available anomalies
                print("active anomalies: ", activeanomalies)
                print("available anomalies: ", available_anomalies)
                multiplier = 1  # Reset the multiplier after rendering an anomaly
        multiplier += 0.1  # Increase the multiplier over time
        time.sleep(1)

def game():
    currentcam = 0
    console_text = ""
    anomaly_thread = threading.Thread(target=createAnomaly, args=(1,))
    anomaly_thread.start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                stop_event.set()  # Set the event to stop anomaly thread
                anomaly_thread.join()  # Wait for anomaly thread to finish
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
        
        # Render the camera image and anomalies
        renderbase(currentcam)

        # Render console as a white box at the bottom right corner
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - CONSOLE_WIDTH, SCREEN_HEIGHT - CONSOLE_HEIGHT, CONSOLE_WIDTH, CONSOLE_HEIGHT))
        
        # Render console text
        console_surface = font.render(console_text, True, BLACK)
        screen.blit(console_surface, (SCREEN_WIDTH - CONSOLE_WIDTH + 10, SCREEN_HEIGHT - CONSOLE_HEIGHT + 10))

        pygame.display.flip()


def main():
    main_menu()
    game()


if __name__ == "__main__":
    main()