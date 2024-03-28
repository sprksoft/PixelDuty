import pygame
IMAGE_WIDTH = 160
IMAGE_HEIGHT = 90
CELL_WIDTH = 8
SCREEN_WIDTH = IMAGE_WIDTH * CELL_WIDTH
SCREEN_HEIGHT = IMAGE_HEIGHT * CELL_WIDTH
bathroom_plant_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_plant_inactive.png"), CELL_WIDTH)
bathroom_plant_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_plant_active.png"), CELL_WIDTH)
bathroom_rug_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_rug_inactive.png"), CELL_WIDTH)
bathroom_rug_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_rug_active.png"), CELL_WIDTH)
bathroom_mirror_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_mirror_inactive.png"), CELL_WIDTH)
bathroom_mirror_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_mirror_active.png"), CELL_WIDTH)
bathroom_toiletpaper_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_toiletpaper_active.png"), CELL_WIDTH)
bathroom_boxes_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_boxes_inactive.png"), CELL_WIDTH)
bathroom_boxes_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_boxes_active.png"), CELL_WIDTH)
def multiplyCordsByFactor(x,y):
    return (x * CELL_WIDTH,y * CELL_WIDTH)
def renderAnomaly(type, room):
    if room == "bathroom": # bathroom
        if type == "plant":
            return [bathroom_plant_active, multiplyCordsByFactor(87,13)]
        if type == "rug":
            return [bathroom_rug_active, multiplyCordsByFactor(82,59)]
        if type == "mirror":
            return [bathroom_mirror_active, multiplyCordsByFactor(103,25)]
        if type == "toiletpaper":
            return [bathroom_toiletpaper_active, multiplyCordsByFactor(88,30)]
        if type == "boxes":
            return [bathroom_boxes_active, multiplyCordsByFactor(65,21)]
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
        if type == "rug":
            return [bathroom_rug_inactive, multiplyCordsByFactor(82,59)]
        if type == "mirror":
            return [bathroom_mirror_inactive, multiplyCordsByFactor(103,25)]
        if type == "toiletpaper":
            return
        if type == "boxes":
            return [bathroom_boxes_inactive, multiplyCordsByFactor(65,21)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "bedroom": # bedroom
        return 
    elif room == "kitchen": # kitchen
        return 
    print("This room doesn't exist: ", room)