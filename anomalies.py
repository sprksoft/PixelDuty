#initializing the anomalies file
import pygame 
IMAGE_WIDTH = 160
IMAGE_HEIGHT = 90
CELL_WIDTH = 8
SCREEN_WIDTH = IMAGE_WIDTH * CELL_WIDTH
SCREEN_HEIGHT = IMAGE_HEIGHT * CELL_WIDTH

#bathroom anomalies
bathroom_plant_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_plant_inactive.png"), CELL_WIDTH)
bathroom_plant_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_plant_active.png"), CELL_WIDTH)

bathroom_rug_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_rug_inactive.png"), CELL_WIDTH)
bathroom_rug_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_rug_active.png"), CELL_WIDTH)

bathroom_mirror_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_mirror_inactive.png"), CELL_WIDTH)
bathroom_mirror_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_mirror_active.png"), CELL_WIDTH)

bathroom_toiletpaper_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_toiletpaper_active.png"), CELL_WIDTH)

bathroom_boxes_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_boxes_inactive.png"), CELL_WIDTH)
bathroom_boxes_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_boxes_active.png"), CELL_WIDTH)

bathroom_sink_inactive = pygame.transform.scale_by(pygame.image.load("assets/bathroom_sink_inactive.png"), CELL_WIDTH)
bathroom_sink_active = pygame.transform.scale_by(pygame.image.load("assets/bathroom_sink_active.png"), CELL_WIDTH)

#bedroom anomalies

bedroom_bed_inactive = pygame.transform.scale_by(pygame.image.load("assets/bedroom_bed_inactive.png"), CELL_WIDTH)
bedroom_bed_active = pygame.transform.scale_by(pygame.image.load("assets/bedroom_bed_active.png"), CELL_WIDTH)

bedroom_bookshelf_inactive = pygame.transform.scale_by(pygame.image.load("assets/bedroom_bookshelf_inactive.png"), CELL_WIDTH)
bedroom_bookshelf_active = pygame.transform.scale_by(pygame.image.load("assets/bedroom_bookshelf_active.png"), CELL_WIDTH)

bedroom_lamp_inactive = pygame.transform.scale_by(pygame.image.load("assets/bedroom_lamp_inactive.png"), CELL_WIDTH)
bedroom_lamp_active = pygame.transform.scale_by(pygame.image.load("assets/bedroom_lamp_active.png"), CELL_WIDTH)

bedroom_window_inactive = pygame.transform.scale_by(pygame.image.load("assets/bedroom_window_inactive.png"), CELL_WIDTH)
bedroom_window_active = pygame.transform.scale_by(pygame.image.load("assets/bedroom_window_active.png"), CELL_WIDTH)

bedroom_rug_inactive = pygame.transform.scale_by(pygame.image.load("assets/bedroom_rug_inactive.png"), CELL_WIDTH)

bedroom_plant_inactive = pygame.transform.scale_by(pygame.image.load("assets/bedroom_plant_inactive.png"), CELL_WIDTH)
bedroom_plant_active = pygame.transform.scale_by(pygame.image.load("assets/bedroom_plant_active.png"), CELL_WIDTH)

bedroom_bomb_active = pygame.transform.scale_by(pygame.image.load("assets/bedroom_bomb_active.png"), CELL_WIDTH)


#kitchen anomalies
kitchen_sink_inactive = pygame.transform.scale_by(pygame.image.load("assets/kitchen_sink_inactive.png"), CELL_WIDTH)
kitchen_sink_active = pygame.transform.scale_by(pygame.image.load("assets/kitchen_sink_active.png"), CELL_WIDTH)

kitchen_microwave_inactive = pygame.transform.scale_by(pygame.image.load("assets/kitchen_microwave_inactive.png"), CELL_WIDTH)
kitchen_microwave_active = pygame.transform.scale_by(pygame.image.load("assets/kitchen_microwave_active.png"), CELL_WIDTH)

kitchen_fridge_inactive = pygame.transform.scale_by(pygame.image.load("assets/kitchen_fridge_inactive.png"), CELL_WIDTH)
kitchen_fridge_active = pygame.transform.scale_by(pygame.image.load("assets/kitchen_fridge_active.png"), CELL_WIDTH)

kitchen_items_inactive = pygame.transform.scale_by(pygame.image.load("assets/kitchen_items_inactive.png"), CELL_WIDTH)
kitchen_items_active = pygame.transform.scale_by(pygame.image.load("assets/kitchen_items_active.png"), CELL_WIDTH)

kitchen_towel_inactive = pygame.transform.scale_by(pygame.image.load("assets/kitchen_towel_inactive.png"), CELL_WIDTH)
kitchen_towel_active = pygame.transform.scale_by(pygame.image.load("assets/kitchen_towel_active.png"), CELL_WIDTH)

kitchen_utensils_inactive = pygame.transform.scale_by(pygame.image.load("assets/kitchen_utensils_inactive.png"), CELL_WIDTH)
kitchen_utensils_active = pygame.transform.scale_by(pygame.image.load("assets/kitchen_utensils_active.png"), CELL_WIDTH)

def multiplyCordsByFactor(x,y): # some math to convert coordinates
    return (x * CELL_WIDTH,y * CELL_WIDTH)

def renderAnomaly(type, room): # rendering all active anomalies
    if room == "bathroom": # bathroom
        if type == "plant":
            return [bathroom_plant_active, multiplyCordsByFactor(87,13)]
        if type == "rug":
            return [bathroom_rug_active, multiplyCordsByFactor(82,59)]
        if type == "mirror":
            return [bathroom_mirror_active, multiplyCordsByFactor(103,25)]
        if type == "toiletpaper":
            return [bathroom_toiletpaper_active, multiplyCordsByFactor(88,30)]
        if type == "sink":
            return [bathroom_sink_active, multiplyCordsByFactor(104,48)]
        if type == "boxes":
            return [bathroom_boxes_active, multiplyCordsByFactor(65,21)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "bedroom": # bedroom
        if type == "bed":
            return [bedroom_bed_active, multiplyCordsByFactor(67,36)]
        if type == "bookshelf":
            return [bedroom_bookshelf_active, multiplyCordsByFactor(104,29)]
        if type == "lamp":
            return [bedroom_lamp_active, multiplyCordsByFactor(58,41)]
        if type == "window":
            return [bedroom_window_active, multiplyCordsByFactor(40,25)]
        if type == "rug":
            return
        if type == "plant":
            return [bedroom_plant_active, multiplyCordsByFactor(85,20)]
        if type == "bomb":
            return [bedroom_bomb_active, multiplyCordsByFactor(67,7)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "kitchen": # kitchen
        if type == "sink":
            return [kitchen_sink_active, multiplyCordsByFactor(87,42)]
        if type == "utensils":
            return [kitchen_utensils_active, multiplyCordsByFactor(82,14)]
        if type == "fridge":
            return [kitchen_fridge_active, multiplyCordsByFactor(87,23)]
        if type == "microwave":
            return [kitchen_microwave_active, multiplyCordsByFactor(64,26)]
        if type == "items":
            return [kitchen_items_active, multiplyCordsByFactor(47,39)]
        if type == "towel":
            return [kitchen_towel_active, multiplyCordsByFactor(49,55)]
        else:
            print("This anomaly doesn't exist: ", type) 
        return 
    print("This room doesn't exist: ", room)

def dontRenderAnomaly(type, room): #rendering all inactive anomalies
    if room == "bathroom": # bathroom
        if type == "plant":
            return [bathroom_plant_inactive, multiplyCordsByFactor(87,13)]
        if type == "rug":
            return [bathroom_rug_inactive, multiplyCordsByFactor(82,59)]
        if type == "mirror":
            return [bathroom_mirror_inactive, multiplyCordsByFactor(103,25)]
        if type == "toiletpaper":
            return
        if type == "sink":
            return [bathroom_sink_inactive, multiplyCordsByFactor(104,48)]
        if type == "boxes":
            return [bathroom_boxes_inactive, multiplyCordsByFactor(65,21)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "bedroom": # bedroom
        if type == "bed":
            return [bedroom_bed_inactive, multiplyCordsByFactor(67,36)]
        if type == "bookshelf":
            return [bedroom_bookshelf_inactive, multiplyCordsByFactor(104,29)]
        if type == "lamp":
            return [bedroom_lamp_inactive, multiplyCordsByFactor(58,41)]
        if type == "window":
            return [bedroom_window_inactive, multiplyCordsByFactor(42,25)]
        if type == "rug":
            return [bedroom_rug_inactive, multiplyCordsByFactor(61,60)]
        if type == "plant":
            return [bedroom_plant_inactive, multiplyCordsByFactor(85,20)]
        if type == "bomb":
            return
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "kitchen": # kitchen
        if type == "sink":
            return [kitchen_sink_inactive, multiplyCordsByFactor(87,42)]
        if type == "fridge":
            return [kitchen_fridge_inactive, multiplyCordsByFactor(96,30)]
        if type == "microwave":
            return [kitchen_microwave_inactive, multiplyCordsByFactor(64,32)]
        if type == "items":
            return [kitchen_items_inactive, multiplyCordsByFactor(46,41)]
        if type == "towel":
            return [kitchen_towel_inactive, multiplyCordsByFactor(49,55)]
        if type == "utensils":
            return [kitchen_utensils_inactive, multiplyCordsByFactor(82,14)]
        else:
            print("This anomaly doesn't exist: ", type) 
    print("This room doesn't exist: ", room)