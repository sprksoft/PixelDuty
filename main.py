import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up screen dimensions
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Custom Main Menu')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

# Function to display text on screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Function to display credits screen
def show_credits():
    screen.fill(WHITE)
    draw_text('Credits', font, BLACK, screen, width // 2, height // 4)
    draw_text('This game was created by [Your Name]', font, BLACK, screen, width // 2, height // 2)
    draw_text('Press any key to return to main menu', font, BLACK, screen, width // 2, 3 * height // 4)
    pygame.display.update()

    # Wait for key press to return to main menu
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False

# Main menu loop
def main_menu():
    button_width = 200
    button_height = 50
    button_spacing = 10
    num_buttons = 3

    total_button_height = num_buttons * button_height + (num_buttons - 1) * button_spacing
    start_y = (height - total_button_height) // 2

    start_button = pygame.Rect((width - button_width) // 2, start_y, button_width, button_height)
    credits_button = pygame.Rect((width - button_width) // 2, start_y + button_height + button_spacing, button_width, button_height)
    quit_button = pygame.Rect((width - button_width) // 2, start_y + 2 * (button_height + button_spacing), button_width, button_height)

    while True:
        screen.fill(WHITE)
        draw_text('Main Menu', font, BLACK, screen, width // 2, height // 4)

        # Draw buttons
        pygame.draw.rect(screen, BLACK, start_button, 2)
        pygame.draw.rect(screen, BLACK, credits_button, 2)
        pygame.draw.rect(screen, BLACK, quit_button, 2)

        # Add your menu options here
        draw_text('Start Game', font, BLACK, screen, width // 2, start_button.centery)
        draw_text('Credits', font, BLACK, screen, width // 2, credits_button.centery)
        draw_text('Quit', font, BLACK, screen, width // 2, quit_button.centery)

        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    # Start game function
                    start_game()
                elif credits_button.collidepoint(mouse_pos):
                    # Credits function
                    show_credits()
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
# Load background images for different cameras
background_images = [
    pygame.image.load('cam1.png'),  # Replace 'camera1.jpg' with actual image file paths
    pygame.image.load('cam2.png'),  # Replace 'camera2.jpg' with actual image file paths
    pygame.image.load('cam3.png')   # Replace 'camera3.jpg' with actual image file paths
]
current_camera = 0  # Index of the current camera view

def observation_screen():
    screen.fill(WHITE)
    screen.blit(background_images[current_camera], (0, 0))  # Display current camera view
    # Adjusted position of the report button to be in the bottom right corner
    report_button_rect = pygame.Rect(width - 250, height - 100, 200, 50)
    pygame.draw.rect(screen, BLACK, report_button_rect, 2)
    
    # Calculate text position to center it within the button
    text_surface = font.render('Report', True, BLACK)
    text_rect = text_surface.get_rect(center=report_button_rect.center)

    screen.blit(text_surface, text_rect)
    pygame.display.update()


# Function to handle camera cycling
def cycle_camera(direction):
    global current_camera
    if direction == 'left':
        current_camera = (current_camera - 1) % len(background_images)  # Cycle left
    elif direction == 'right':
        current_camera = (current_camera + 1) % len(background_images)  # Cycle right
def report_window():
    # Create a transparent surface to darken the background
    darken_surface = pygame.Surface((width, height))
    darken_surface.set_alpha(128)  # Set transparency level
    darken_surface.fill(BLACK)
    screen.blit(darken_surface, (0, 0))
    
    # Report window dimensions and position
    report_window_width = 400
    report_window_height = 300
    report_window_x = (width - report_window_width) // 2
    report_window_y = (height - report_window_height) // 2
    
    # Draw report window
    pygame.draw.rect(screen, WHITE, (report_window_x, report_window_y, report_window_width, report_window_height))
    pygame.draw.rect(screen, BLACK, (report_window_x, report_window_y, report_window_width, report_window_height), 2)
    
    # Draw text on report window
    draw_text('Select Camera:', font, BLACK, screen, report_window_x + 20, report_window_y + 20)
    draw_text('Select Anomaly Type:', font, BLACK, screen, report_window_x + 20, report_window_y + 100)
    
    # Add code to draw camera and anomaly selection UI elements (e.g., dropdown menus, buttons, etc.)
    # For simplicity, let's assume we have a list of cameras and anomaly types
    cameras = ['Camera 1', 'Camera 2', 'Camera 3']
    anomaly_types = ['Type 1', 'Type 2', 'Type 3']
    
    # Draw dropdown menus for camera and anomaly type selection
    camera_dropdown = pygame.Rect(report_window_x + 170, report_window_y + 15, 200, 30)
    anomaly_dropdown = pygame.Rect(report_window_x + 170, report_window_y + 95, 200, 30)
    pygame.draw.rect(screen, BLACK, camera_dropdown, 2)
    pygame.draw.rect(screen, BLACK, anomaly_dropdown, 2)
    draw_text('Select', font, BLACK, screen, report_window_x + 175, report_window_y + 20)
    draw_text('Select', font, BLACK, screen, report_window_x + 175, report_window_y + 100)
    
    # Display camera options
    for i, camera in enumerate(cameras):
        draw_text(camera, font, BLACK, screen, report_window_x + 170, report_window_y + 55 + i * 30)
    
    # Display anomaly type options
    for i, anomaly_type in enumerate(anomaly_types):
        draw_text(anomaly_type, font, BLACK, screen, report_window_x + 170, report_window_y + 135 + i * 30)
    
    # Draw report button
    report_button = pygame.Rect(report_window_x + 150, report_window_y + 230, 100, 40)
    pygame.draw.rect(screen, BLACK, report_button, 2)
    draw_text('Report', font, BLACK, screen, report_button.centerx - 35, report_button.centery - 10)
    
    pygame.display.update()
    
    # Report window event loop
    reporting = True
    while reporting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if report_button.collidepoint(mouse_pos):
                    # Handle report button click
                    selected_camera = None
                    selected_anomaly = None
                    # Check if camera or anomaly type is selected
                    if camera_dropdown.collidepoint(mouse_pos):
                        # Handle camera selection
                        print("Camera selected")
                    elif anomaly_dropdown.collidepoint(mouse_pos):
                        # Handle anomaly type selection
                        print("Anomaly type selected")
                    else:
                        # Close report window if clicked outside dropdowns or button
                        reporting = False
    
    pygame.display.flip()  # Update display after closing window



# Function to start the game
def start_game():
    observation_screen()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cycle_camera('left')  # Cycle camera left on left arrow key press
                    observation_screen()
                elif event.key == pygame.K_RIGHT:
                    cycle_camera('right')  # Cycle camera right on right arrow key press
                    observation_screen()
                elif event.key == pygame.K_SPACE:
                    report_window()  # Open report window when spacebar is pressed

# Start the main menu
main_menu()
