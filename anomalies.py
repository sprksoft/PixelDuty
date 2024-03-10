import pygame
door_bathroom = pygame.image.load("assets/door_bathroom.png")
def renderAnomaly(type, room, width_height):
    WIDTH = width_height[0]
    HEIGHT = width_height[1]
    if room == "bathroom": # bathroom
        if type == "door":
            return [door_bathroom, (WIDTH//2,HEIGHT//2)]
        elif type == "toilet":
            return [door_bathroom, (WIDTH//3,HEIGHT//3)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "bedroom": # bedroom
        return 
    elif room == "kitchen": # kitchen
        return 
    print("This room doesn't exist: ", room)

def dontRenderAnomaly(type, room, width_height):
    WIDTH = width_height[0]
    HEIGHT = width_height[1]
    if room == "bathroom": # bathroom
        if type == "door":
            return [door_bathroom, (WIDTH//1.4,HEIGHT//1.4)]
        elif type == "toilet":
            return [door_bathroom, (WIDTH//1.6,HEIGHT//1.6)]
        else:
            print("This anomaly doesn't exist: ", type) 
    elif room == "bedroom": # bedroom
        return 
    elif room == "kitchen": # kitchen
        return 
    print("This room doesn't exist: ", room)