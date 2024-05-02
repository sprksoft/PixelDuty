import pygame
pygame_version = pygame.version.ver
if pygame_version >= ("2.1.3"):
    print("Pygame version is compatible.")
else:
    print(f"Pygame version {pygame_version} is lower than the required version 2.1.3.")
    exit(1)

import sys
import time
import random
import threading
import anomalies
import math
# initialize Pygame
pygame.init()

# screen dimensions and other variables
IMAGE_WIDTH = 160
IMAGE_HEIGHT = 90
CELL_WIDTH = anomalies.CELL_WIDTH
SCREEN_WIDTH = IMAGE_WIDTH * CELL_WIDTH
SCREEN_HEIGHT = IMAGE_HEIGHT * CELL_WIDTH
CONSOLE_WIDTH = 50 * CELL_WIDTH
CONSOLE_HEIGHT = 10 * CELL_WIDTH
clock_state = 0
show_anomaly_found_screen = False
show_no_anomaly_found_message = False
is_counting_down =  False

# all needed images or sprites
cams = [pygame.image.load('cam0.png'), pygame.image.load('cam1.png'), pygame.image.load('cam2.png')]
clocks = [pygame.transform.scale_by(pygame.image.load("clock/clock_0.png"), CELL_WIDTH),pygame.transform.scale_by(pygame.image.load("clock/clock_1.png"), CELL_WIDTH), pygame.transform.scale_by(pygame.image.load("clock/clock_2.png"), CELL_WIDTH), pygame.transform.scale_by(pygame.image.load("clock/clock_3.png"), CELL_WIDTH),pygame.transform.scale_by(pygame.image.load("clock/clock_4.png"), CELL_WIDTH)]
anomaly_found_screen = pygame.image.load('anomaly_found_screen.png')
death_screen = pygame.image.load('death_screen.png')
anomaly_not_found_message = pygame.transform.scale_by(pygame.image.load("anomaly_not_found_message.png"), CELL_WIDTH)
many_active_anomalies_warning = pygame.transform.scale_by(pygame.image.load("many_active_anomalies_warning.png"), CELL_WIDTH)
console_box = pygame.transform.scale_by(pygame.image.load("console_box.png"), CELL_WIDTH)
journal_image = pygame.image.load('journal_screen.png')
cams_rooms = {
    cams[0]: "bathroom",
    cams[1]: "bedroom",
    cams[2]: "kitchen"
}
maxcamindex = len(cams) - 1
activeanomalies = []
high_anomaly_time = None
available_anomalies = [["bathroom", "plant"],["bathroom", "rug"],["bathroom", "mirror"],["bathroom", "toiletpaper"],["bathroom", "boxes"],["bathroom", "sink"],["kitchen", "sink"],["kitchen", "fridge"],["kitchen", "microwave"],["kitchen", "items"],["kitchen", "towel"],["kitchen", "utensils"],["bedroom", "bed"],["bedroom", "bookshelf"],["bedroom", "lamp"],["bedroom", "window"],["bedroom", "rug"],["bedroom", "plant"],["bedroom", "bomb"]]

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PixelDuty")

font = pygame.font.Font(None, CELL_WIDTH * 5)

stop_event = threading.Event()

show_journal = False

def remove_anomaly(anomaly): # removes anomaly form active anomalies list and adds it back to available anomalies
    activeanomalies.remove(anomaly)
    available_anomalies.append(anomaly)

def render_clock(state): # rendering the clock based on the state 
    return [clocks[state],anomalies.multiplyCordsByFactor(1,1)]

def handle_console(user_input):
    global clock_state
    global show_anomaly_found_screen
    global show_no_anomaly_found_message
    global is_counting_down
    anomaly = user_input.split(" ")[0].strip()
    anomaly_found = False
    locations={ # dictionary for switch case because it looks fancy
    0: "bathroom",
    1: "bedroom",
    2: "kitchen"
    }
    location=locations.get(currentcam)
    for active_anomaly in activeanomalies:
        if [location, anomaly] == active_anomaly:
            anomaly_found = True
            break
    # clock sequence
    is_counting_down = True
    clock_state = 4
    time.sleep(1)
    clock_state = 3
    time.sleep(1)
    clock_state = 2
    time.sleep(1)
    clock_state = 1
    time.sleep(1)
    clock_state = 0
    if anomaly_found: # show anomaly found screen if anomaly found
        remove_anomaly([location, anomaly])
        show_anomaly_found_screen = True
        time.sleep(2)
        show_anomaly_found_screen = False
        is_counting_down = False
    else: # show anomaly not found screen if anomaly not found
        show_no_anomaly_found_message = True
        is_counting_down = False
        time.sleep(2)
        show_no_anomaly_found_message = False


# rendering the main menu
def main_menu():
    global CELL_WIDTH
    global SCREEN_HEIGHT
    global SCREEN_WIDTH
    global CONSOLE_HEIGHT
    global CONSOLE_WIDTH
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    CELL_WIDTH = int(event.unicode)
                else:
                    return

        screen.fill(WHITE)
        title_text = font.render("PixelDuty", True, BLACK)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        start_text = font.render("Press any button to start", True, BLACK)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()

def renderAnomalies(camnumber, room, anomaly_type):# function  to render all active anomalies
    cam = cams[camnumber]
    if cams_rooms.get(cam) == room:
        return anomalies.renderAnomaly(anomaly_type, room)
def dontRenderAnomalies(camnumber, room, anomaly_type): # function  to render all inactive anomalies
    cam = cams[camnumber]
    if cams_rooms.get(cam) == room:
        return anomalies.dontRenderAnomaly(anomaly_type, room)

def renderbackground(image): # bad code to scale and render a background image
    width_scale_factor = SCREEN_WIDTH / image.get_width()
    height_scale_factor = SCREEN_HEIGHT / image.get_height()
    scale_factor = min(width_scale_factor, height_scale_factor)
    scaled_image_width = int(image.get_width() * scale_factor)
    scaled_image_height = int(image.get_height() * scale_factor)
    scaled_image = pygame.transform.scale(image, (scaled_image_width, scaled_image_height))
    screen.blit(scaled_image, ((SCREEN_WIDTH - scaled_image_width) // 2, (SCREEN_HEIGHT - scaled_image_height) // 2))

def renderbase(camnumber, console_text, clock_state): # rendering the main parts of the game

    renderbackground(cams[camnumber])

    activeanomalies.sort()
    activeanomalies.reverse()
    clock_surface = render_clock(clock_state)
    if clock_surface is not None:
        screen.blit(clock_surface[0], clock_surface[1])
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
    screen.blit(console_box,anomalies.multiplyCordsByFactor(112,79))
    console_surface = font.render(console_text, True, WHITE)
    screen.blit(console_surface, anomalies.multiplyCordsByFactor(114,81))


def createAnomaly(multiplier): # creating anomalies
    global available_anomalies
    time.sleep(5) #initial wait 
    while not stop_event.is_set():
        if random.random() < (0.1 * multiplier):
            if available_anomalies: # create anomaly based on random chance 
                chosen_anomaly_index = random.randint(0, len(available_anomalies) - 1)
                chosen_anomaly = available_anomalies[chosen_anomaly_index]
                activeanomalies.append(chosen_anomaly)
                available_anomalies.remove(chosen_anomaly)
                print(chosen_anomaly)
                multiplier = 1 
        multiplier += 0.1 # increase multiplier for larger chances as time goes on
        print(round(multiplier*10))
        time.sleep(3) # time between anomaly creation

def reset_game(): # reset the game
    global activeanomalies, available_anomalies
    stop_event.set() # quit all threads
    activeanomalies = [] 
    available_anomalies = available_anomalies = [["bathroom", "plant"],["bathroom", "rug"],["bathroom", "mirror"],["bathroom", "toiletpaper"],["bathroom", "boxes"],["bathroom", "sink"],["kitchen", "sink"],["kitchen", "fridge"],["kitchen", "microwave"],["kitchen", "items"],["kitchen", "towel"],["kitchen", "utensils"],["bedroom", "bed"],["bedroom", "bookshelf"],["bedroom", "lamp"],["bedroom", "window"],["bedroom", "rug"],["bedroom", "plant"],["bedroom", "bomb"]]
    main_menu()
    game() # call game function when main menu is done

def game():
    # initalize the game
    global currentcam
    currentcam = 0
    console_text = ""
    global anomaly_thread
    global clock_thread
    global is_counting_down
    global show_journal
    stop_event.clear() 
    anomaly_thread = threading.Thread(target=createAnomaly, args=(1,))
    anomaly_thread.start()
    
    
    while True:
        for event in pygame.event.get(): # check keyboard inputs
            if event.type == pygame.QUIT: # reset game on quit event
                reset_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not is_counting_down:
                    print("Command entered:", console_text)
                    clock_thread = threading.Thread(target=handle_console,args=(console_text,)) # start the console checking thread
                    clock_thread.start()
                    console_text = ""
                elif event.key == pygame.K_BACKSPACE: # remove from console
                    console_text = console_text[:-1]
                elif event.key == pygame.K_LEFT: # switch cams
                    currentcam -= 1
                    if currentcam < 0:
                        currentcam = maxcamindex
                elif event.key == pygame.K_RIGHT: # switch cams
                    currentcam += 1
                    if currentcam > maxcamindex:
                        currentcam = 0
                elif event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE: # switch cams
                    show_journal = not show_journal
                else:
                    if not is_counting_down:
                        console_text += event.unicode # add all other charaters to the console

        renderbase(currentcam, console_text, clock_state) #render the game
        if show_anomaly_found_screen: # render found anomaly screen
            renderbackground(anomaly_found_screen)
        if show_no_anomaly_found_message: # render no anomalies found message
            screen.blit(anomaly_not_found_message,anomalies.multiplyCordsByFactor(96,1))
        if len(activeanomalies) > 4: # render many active anomalies warning
            screen.blit(many_active_anomalies_warning,anomalies.multiplyCordsByFactor(1,83))
        if len(activeanomalies) >= 6: # render death screen
            renderbackground(death_screen)
            pygame.display.flip()
            time.sleep(4)
            reset_game()
        if show_journal:
            renderbackground(journal_image)
        pygame.display.flip()


def main():
    main_menu()
    game()


if __name__ == "__main__":
    main()