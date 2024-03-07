import pygame
door_bathroom = pygame.image.load("assets/door_bathroom.png")
def renderAnomaly(type, room):
    if room == "bathroom": # bathroom
        if type == "door":
            return [door_bathroom, (50,50)]
        elif type == "toilet":
            return [door_bathroom, (150,150)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "bedroom": # bedroom
        return 
    elif room == "kitchen": # kitchen
        return 
    print("This room doesn't exist: ", room)

def dontRenderAnomaly(type, room):
    if room == "bathroom": # bathroom
        if type == "door":
            return [door_bathroom, (400,400)]
        elif type == "toilet":
            return [door_bathroom, (500,500)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "bedroom": # bedroom
        return 
    elif room == "kitchen": # kitchen
        return 
    print("This room doesn't exist: ", room)