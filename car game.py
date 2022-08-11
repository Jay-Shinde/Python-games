import pygame
from pygame.locals import *
import random
import time


    
    

#-----------------------function for main window of game----------------------- 
def gameloop():
    size = wt , ht = (800 , 800)
    road_w = int(wt/1.6)
    road_mk = int(wt/80)
    right_lane = wt/2 + road_w/4
    left_lane = wt/2 - road_w/4

    pygame.init()
    running = True
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("jay's car game")
    screen.fill((60, 220, 0))


    pygame.display.update()

    car = pygame.image.load("car.png")
    car_loc = car.get_rect()
    car_loc.center = right_lane , ht*0.8

    car_1= pygame.image.load("otherCar.png")
    car_loc_1 = car_1.get_rect()
    car_loc_1.center = left_lane , ht*0.2


    count = 0
    level = 0
    speed = 2
    while running:
        level += 1
        if level == 1000:
            speed += 0.25
            level = 0
            print("level up")
        
        car_loc_1[1]+= speed
        
        
        if car_loc_1[1] > ht:
            
            if random.randint(0,1) == 0:
                car_loc_1.center = left_lane , -200
            else:
                car_loc_1.center = right_lane , -200
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT] and count == 0:
                    car_loc = car_loc.move([-int(road_w/2),0])
                    count = count+1
                if event.key in [K_d, K_RIGHT] and count == 1:
                    car_loc = car_loc.move([int(road_w/2),0])
                    count = count-1
        if car_loc_1[0]==car_loc[0] and car_loc_1[1]>=car_loc[1]-240:
            time.sleep(1)
            print("Game Over ! You Lost !")
            break
        pygame.draw.rect(
            screen,
            (50,50,50),
            (wt/2-road_w/2 , 0 , road_w , ht))

        pygame.draw.rect(
            screen,
            (255,240,60),
            (wt/2-road_mk/2 , 0 , road_mk , ht))

        pygame.draw.rect(
            screen,
            (255,255,255),
            (wt/2-road_w/2+road_mk , 0 , road_mk , ht))

        pygame.draw.rect(
            screen,
            
            (255,255,255),
            (wt/2+road_w/2-road_mk*2 , 0 , road_mk , ht))
        screen.blit(car,car_loc)
        screen.blit(car_1,car_loc_1)
        
                

        pygame.display.update()



    pygame.quit()
    


gameloop()

