import pygame, sys, random

#initialise pygame
pygame.init()

#setting width and height
width  = 800
height = 600

#allows for fps
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
dodgeball_size = 50
dodgeballs = []
dodgeball_img = pygame.image.load('dodgeball.png')
dodge_col_x = 1
dodge_col_y = 2

#colours  R   G   B
black = (000,000,000)
white = (255,255,255)
red = (255,000,000)
green = (000,200,000)
light_green = (000,255,000)
dark_red = (200,000,000)
blue = (000,000,200)
light_blue = (000,000,255)

#fonts
smallfont = pygame.font.Font("luckiestGuy.ttf",25)
medfont = pygame.font.Font("luckiestGuy.ttf",50)
largefont = pygame.font.Font("luckiestGuy.ttf",100)

#display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('dodge Ball')


def text_object(text,color, size):  #gives the text to the message_to_screen function for centering
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace = 0, size = "small"):   #easy way of putting text onto the screen
    textSurf, textRect = text_object(msg, color, size)
    textRect.center = (width/2), (height/2)+y_displace
    screen.blit(textSurf, textRect)
    
def health_bar():   #draws healthbar
    global health
    
    pygame.draw.rect(screen,black,[11,11,health*4+1, 31])
    pygame.draw.rect(screen, red, [10, 10, health*4, 30])
    text_health = smallfont.render(str(health)+'/100',True,black)
    screen.blit(text_health, [health*4+20,5])



def draw_dodgeballs():  #draws dodgeballs onto screen
    for dodgeball in dodgeballs:
        screen.blit(dodgeball[0], (dodgeball[1], dodgeball[2]))

def move_dodgeballs():  #makes the dodgeballs move, also contains dodgeball collisions
    global dodgeball_speed, dodgeball,dodge_split, health
    for dodgeball in dodgeballs:
        dodgeball[2] += random.randint(dodge_min_speed,dodge_max_speed)
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
                health -= 10
               


        
        

#these 3 functions are for movement
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


                    
def game_intro():   #front end of the game
    intro = True
    while intro:
        screen.fill(white)
        message_to_screen('welcome to dodgeball dash',black,-100,'medium')
        message_to_screen('dodge the balls and survive as long as possible',red,0,'small')

        mouse = pygame.mouse.get_pos()

        text_start = medfont.render('Start!',True,white)
        text_quit = medfont.render('Quit',True,white)


        pygame.draw.rect(screen,green,[100,400,230,70])
        pygame.draw.rect(screen,dark_red,[470,400,230,70])
#play
        if 100+230 > mouse[0] > 100 and 400+70 > mouse[1] > 400:
            pygame.draw.rect(screen,light_green,[105,405,220,60])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    intro = False
                    difficulty_choice()
#quit
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


        screen.blit(text_start, [140,415,230,70])
        screen.blit(text_quit, [530,415,230,70])
        pygame.display.update()
        clock.tick(15)
    
def game_over():    #game over screen for death
    global gameover
    while gameover == True:
        mouse = pygame.mouse.get_pos()

        text_replay = medfont.render('replay',True,white)
        text_quit = medfont.render('Quit',True,white)


        pygame.draw.rect(screen,green,[100,400,230,70])
        pygame.draw.rect(screen,dark_red,[470,400,230,70])
#restart
        if 100+230 > mouse[0] > 100 and 400+70 > mouse[1] > 400:
            pygame.draw.rect(screen,light_green,[105,405,220,60])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = False
                    difficulty_choice()
#quit
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
        screen.blit(text_replay, [135,415])
        screen.blit(text_quit, [530,415])
        pygame.display.update()


def scoring():  #a scoring system based on time
    global time, time_displayed
    if time > 70000000000: #there are 70000000000 in a second
        time = clock.get_time()
        time_displayed += 1
    time += time
    text_time = smallfont.render('time:' + str(time_displayed),True,black)
    screen.blit(text_time,[10,570])

def difficulty_choice():    #allows the user to choose a suitable difficulty
    global num_of_dodgeballs,dodge_min_speed,dodge_max_speed
    screen.fill(white)
    difficulty_choice = True
    while difficulty_choice == True:
        mouse = pygame.mouse.get_pos()

        message_to_screen('choose your difficulty',black,-250,'medium')

        pygame.draw.rect(screen,green,[290,120,220,90])
        pygame.draw.rect(screen,blue,[290,285,220,90])
        pygame.draw.rect(screen,dark_red,[290,450,220,90])
#easy
        if 290 + 220 > mouse[0] > 290 and 120 + 90 > mouse[1] > 120:
            pygame.draw.rect(screen,light_green,[295,125,210,80])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    num_of_dodgeballs = 4
                    dodge_min_speed = 10
                    dodge_max_speed = 15
                    difficulty_choice = False
                    gameloop()
#medium
        if 290 + 220 > mouse[0] > 290 and 285 + 90 > mouse[1] > 285:
            pygame.draw.rect(screen,light_blue,[295,290,210,80])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    num_of_dodgeballs = 6
                    dodge_min_speed = 15
                    dodge_max_speed = 25
                    difficulty_choice = False
                    gameloop()
#hard
        if 290 + 220 > mouse[0] > 290 and 450 + 90 > mouse[1] > 450:
            pygame.draw.rect(screen,red,[295,455,210,80])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    num_of_dodgeballs = 8
                    dodge_min_speed = 25
                    dodge_max_speed = 35
                    difficulty_choice = False
                    gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        text_easy = medfont.render('easy',True,white)
        text_medium = medfont.render('medium',True,white)
        text_hard = medfont.render('hard',True,white)
        screen.blit(text_easy,[340,149])
        screen.blit(text_medium,[305,313])
        screen.blit(text_hard,[340,477])
        
        pygame.display.update()
        clock.tick(15)
    
def gameloop():   #the main function, cointains all of the game
    global cx, cy, speed, left, right, dx, character_size, dy, dodge_col_x, dodge_col_y,gameover,health,dodgeballs,time,time_displayed
#time variables
    time = clock.get_time()
    time_displayed = 0

#used to detect if death has occured
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
    dodgeballs = []
    dodgeball_img = pygame.image.load('dodgeball.png')
    dodge_col_x = 1
    dodge_col_y = 2


#making list of dx and dy for each dodgeball
    for i in range (num_of_dodgeballs):
        dx = random.randint(0,width - dodgeball_size)
        dodgeballs.append([dodgeball_img, dx, dy,4])

#main game loop starts
    while True:
        screen.fill(white)
        
#handles death
        if gameover == True:
            screen.fill(white)
            message_to_screen('you died',red,-25,'large')
            game_over()
            pygame.display.update()

#movement
        check_all_events()             
        if cx < width - character_size:
            if right:
                move_right()

        if cx > 0:
            if left:
                move_left()

#drawing stuff and main game functions
        pygame.draw.rect(screen, black, [cx, cy, character_size, character_size])
        draw_dodgeballs()
        move_dodgeballs()
        health_bar()
        scoring()
#decides if death has happened
        if health <= 0:
            gameover = True
#screen updates
        pygame.display.update()
        clock.tick(30)

#start of game
game_intro()  

