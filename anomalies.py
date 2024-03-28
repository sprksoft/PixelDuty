import pygame
IMAGE_WIDTH = 160
IMAGE_HEIGHT = 90
CELL_WIDTH = 8
SCREEN_WIDTH = IMAGE_WIDTH * CELL_WIDTH
SCREEN_HEIGHT = IMAGE_HEIGHT * CELL_WIDTH
bathroom_plant_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_plant_inactive.png"), CELL_WIDTH)
bathroom_plant_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_plant_active.png"), CELL_WIDTH)
def multiplyCordsByFactor(x,y):
    return (x * CELL_WIDTH,y * CELL_WIDTH)
def renderAnomaly(type, room):
    if room == "bathroom": # bathroom
        if type == "plant":
            return [bathroom_plant_active, multiplyCordsByFactor(87,13)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "bedroom": # bedroom
        return 
    elif room == "kitchen": # kitchen
        return 
    print("This room doesn't exist: ", room)

def dontRenderAnomaly(type, room):
    if room == "bathroom": # bathroom
        if type == "plant":
            return [bathroom_plant_inactive, multiplyCordsByFactor(87,13)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "bedroom": # bedroom
        return 
    elif room == "kitchen": # kitchen
        return 
    print("This room doesn't exist: ", room)