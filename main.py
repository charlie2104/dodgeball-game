import pygame, sys, random

pygame.init()

#setting width and height
width  = 800
height = 600

clock = pygame.time.Clock()


#info for characters
cx = width/2
cy = height - 50
speed = 20
character_size = 32
left = False
right = False
health = 100
#info for dodgeballs
dx = -60
dy = 20
dodgeball_speed = 0.5
dodgeball_size = 50
dodgeballs = []
dodgeball_img = pygame.image.load('dodgeball.png')
dodge_col_x = 1
dodge_col_y = 2
num_of_dodgeballs = 5

#colours  R   G   B
black = (000,000,000)
white = (255,255,255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('dodge Ball')

for i in range (num_of_dodgeballs):
    dx = random.randint(0,width - dodgeball_size)
    dodgeballs.append([dodgeball_img, dx, dy,4])
    

def draw_dodgeballs():
    for dodgeball in dodgeballs:
        screen.blit(dodgeball[0], (dodgeball[1], dodgeball[2]))

def move_dodgeballs():
    global dodgeball_speed, dodgeball,dodge_split, health
    for dodgeball in dodgeballs:
        dodgeball[2] += random.randint(10,30)
        if dodgeball[2] >= 600:
            dx = random.randint(0,width - dodgeball_size)
            dodgeball[1] = dx
            dodgeball[2] = -60
        #collisions
        if cx > dodgeball[1] and cx < dodgeball[1] + dodgeball_size or cx + character_size > dodgeball[1] and cx + character_size < dodgeball[1] + dodgeball_size:
            if cy > dodgeball[2] and cy < dodgeball[2] + dodgeball_size or cy + character_size > dodgeball[2] and cy + character_size < dodgeball[2] + dodgeball_size:
                dx = random.randint(0,width - dodgeball_size)
                dodgeball[1] = dx
                dodgeball[2] = -60
                health-=1
                print (health)


        
        


def move_left():
    global cx
    cx -= speed
def move_right():
    global cx
    cx += speed

def check_all_events():
    global left, right, cx
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True


def gameloop():

    global cx, cy, speed, left, right, dx, character_size, dy, dodge_col_x, dodge_col_y,dodge_split
    gameExit =  False
    
    while not gameExit:
        screen.fill(white)
        check_all_events()
    
        if cx < width - character_size:
            if right:
                move_right()

        if cx > 0:
            if left:
                move_left()


            
        dodge_split = str(dodgeballs).split(",")
        pygame.draw.rect(screen, black, [cx, cy, character_size, character_size])
        draw_dodgeballs()
        move_dodgeballs()


        #dodge_split = str(dodgeballs).split(",")


##        the old hard coded split colissions  
##        if cx > int(dodge_split[1]) and cx < int(dodge_split[1]) + dodgeball_size or cx + character_size > int(dodge_split[1]) and cx + character_size < int(dodge_split[1]) + dodgeball_size:
##            if cy > int(dodge_split[2]) and cy < int(dodge_split[2]) + dodgeball_size or cy + character_size > int(dodge_split[2]) and cy + character_size < int(dodge_split[2]) + dodgeball_size:
##                dx = random.randint(0,width - dodgeball_size)
##                dodgeball[1] = dx
##
##                dodgeball[2] = -60
##        if cx > int(dodge_split[5]) and cx < int(dodge_split[5]) + dodgeball_size or cx + character_size > int(dodge_split[5]) and cx + character_size < int(dodge_split[5]) + dodgeball_size:
##            if cy > int(dodge_split[6]) and cy < int(dodge_split[6]) + dodgeball_size or cy + character_size > int(dodge_split[6]) and cy + character_size < int(dodge_split[6]) + dodgeball_size:
##                dx = random.randint(0,width - dodgeball_size)
##                dodgeball[1] = dx
##
##                dodgeball[2] = -60


 
        pygame.display.update()
        clock.tick(30)




    pygame.quit
    quit()
    
gameloop()
