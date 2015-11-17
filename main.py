import pygame, sys, random

pygame.init()

#setting width and height
width  = 800
height = 600

clock = pygame.time.Clock()
gameover = False

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
red = (255,000,000)
green = (000,200,000)
light_green = (000,255,000)
dark_red = (200,000,000)

smallfont = pygame.font.Font("comic.ttf",25)
medfont = pygame.font.Font("comic.ttf",50)
largefont = pygame.font.Font("comic.ttf",80)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('dodge Ball')


def text_object(text,color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_object(msg, color, size)
    textRect.center = (width/2), (height/2)+y_displace
    screen.blit(textSurf, textRect)
    
##for i in range (num_of_dodgeballs):
##    dx = random.randint(0,width - dodgeball_size)
##    dodgeballs.append([dodgeball_img, dx, dy,4])
    
def health_bar():
    global health
    
    pygame.draw.rect(screen,black,[11,11,health*4+1, 31])
    pygame.draw.rect(screen, red, [10, 10, health*4, 30])
    text_health = smallfont.render(str(health)+'/100',True,black)
    screen.blit(text_health, [health*4+20,5])



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
                health -= 5
               


        
        


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

##def game_over():
##    global gameover, gameExit
##    while gameover == True:
##        screen.fill(white)
##        message_to_screen('you died',red,-25,'large')
##        message_to_screen('press q to quit',black,40,'small')
##        pygame.display.update()
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
##            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_c:
##                    health = 100
##                    gameover = False
##                    gameloop()
##                    break
##                if event.key == pygame.K_q:
##                    pygame.quit()
##                    quit()

                    
def game_intro():
    intro = True
    while intro:
        screen.fill(white)
        message_to_screen('welcome to dodgeball dash',black,-100,'medium')
        message_to_screen('dodge the balls and survive as long as possible',red,0,'small')

        mouse = pygame.mouse.get_pos()

        text_start = medfont.render('Start!',True,black)
        text_quit = medfont.render('Quit',True,black)


        pygame.draw.rect(screen,green,[100,400,230,70])
        pygame.draw.rect(screen,dark_red,[470,400,230,70])

        if 100+230 > mouse[0] > 100 and 400+70 > mouse[1] > 400:
            pygame.draw.rect(screen,light_green,[105,405,220,60])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    intro = False
                    gameloop()
        if 470+230 > mouse[0] > 470 and 400+70 > mouse[1] > 400:
            pygame.draw.rect(screen,red,[475,405,220,60])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        screen.blit(text_start, [140,395,230,70])
        screen.blit(text_quit, [530,395,230,70])
        pygame.display.update()
        clock.tick(15)
    

    
def gameloop():
    global cx, cy, speed, left, right, dx, character_size, dy, dodge_col_x, dodge_col_y,dodge_split,gameover,health,dodgeballs
    gameExit =  False

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

    for i in range (num_of_dodgeballs):
        dx = random.randint(0,width - dodgeball_size)
        dodgeballs.append([dodgeball_img, dx, dy,4])

    while not gameExit:
        if gameover == True:
            screen.fill(white)
            message_to_screen('you died',red,-25,'large')
            message_to_screen('press q to quit or c to play again',black,40,'small')
            pygame.display.update()
            while gameover == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            health = 100
                            gameover = False
                            gameloop()
                            break
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
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
        health_bar()
        if health <= 0:
            gameover = True
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
game_intro()    

