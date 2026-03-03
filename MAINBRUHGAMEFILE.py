import pygame
import random
import PlaneCreateFile
import math
import time


#default statements(time, starting weather etc.)
gametime = 28800
current_weather = 'clear'
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WIDTH = 1500
HEIGHT = 700
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BRAHGAME')
screen.fill(GRAY)
pygame.display.flip()
#FPS settings
FPS = 20
CLOCK = pygame.time.Clock()
CLOCK.tick(FPS)
#runs the whole game cycle
run = True
#X level of the radar center
RADAR_CX = 262.5
#Y level of the radar center
RADAR_CY = 437.5
#radius of the radar in pixels
RADAR_RADIUS = 212.5
#planes on radar right now
planes_on_radar_rn = []
#minimum and maximum numbers of plane arrival frequency
min_arrival_frequency = 300
max_arrival_frequency = 1800
#time before next plane will arrive
next_arrival_time = random.randint(min_arrival_frequency, max_arrival_frequency)+gametime
#the average speed of a plane in knots
avg_spd = 400.0
#das ist change
#base count of pixels per second that a plane will pass(i think)
pixel_speed_base = 0.5
#chance for a plane to fly by and not land
land_or_no_chance = 0.2
#what exactly is getting displayed
visibility_on_screen = 'Visibility: 20km'
#holds the number of visibility in kilometers to go on display
visibility_display = 20
#time before next weather change will occur
next_weather_changetime = gametime
chat_activity = False
chat_input = ''
chat_history = ['brehbrehbrehberehbedbuewabnhdiewfhwuialnwqeuiowefhsulifnersoiruufhsojfioernfirlnjeo;sfjoi;wsoa/fo;rnfwiosfnoa;nfh', 'nhujadbnwjkdewddyhaweubhdeaukbhckubnhuawekbhukbswkehfuiafhuwabhufybasybheyuabhfayufbsyuabfyuhsbfsyuabhsfhbakugwkebf', 'nhfrwyubgdfhaeyuikxdebuaybgauidhueiwadnheuiergbfhuerihfruihrrhruhfjufhfhfhfhfhfhhfhfhwikdjoaeudeuiweuijdjdjdjdjdjjdjdjdjdjdjdjjdjdjdjdjdjjdjdjdjdj']
def DRAW_DA_SCREEN():
    '''
    draws the main lines of the screen and decides its color
    '''
    screen.fill(GRAY)
    pygame.draw.line(screen, BLACK, (0, 175), (550, 175))
    pygame.draw.line(screen, BLACK, (550, 0), (550, 700))
    pygame.draw.line(screen, BLACK, (550, 445), (1500, 445))
    pygame.draw.line(screen, BLACK, (175, 0), (175, 175))
    pygame.draw.line(screen, BLACK, (1025, 445), (1025, 700))
    pygame.draw.line(screen, BLACK, (550, 40), (1500, 40))
    pygame.draw.line(screen, BLACK, (1350, 445), (1350, 40))
#draws the radar circles
def draw_a_radar_challenge():
    '''
    draws the radar using green and black circles and green lines
    '''
    pygame.draw.circle(screen, GREEN, (262.5, 437.5), 214.5)
    pygame.draw.circle(screen, BLACK, (262.5, 437.5), 212.5)
    pygame.draw.line(screen, GREEN, (48, 223), (475, 652), width=2)
    pygame.draw.line(screen, GREEN, (48, 652), (475, 223), width=2)
    pygame.draw.line(screen, GREEN, (262.5, 215), (262.5, 660), width=2)
    pygame.draw.line(screen, GREEN, (40, 437.5), (483, 437.5), width=2)
    pygame.draw.circle(screen, GREEN, (262.5, 437.5), 187.5)
    pygame.draw.circle(screen, BLACK, (262.5, 437.5), 185.5)
    pygame.draw.circle(screen, GREEN, (262.5, 437.5), 150.5)
    pygame.draw.circle(screen, BLACK, (262.5, 437.5), 148.5)
    pygame.draw.circle(screen, GREEN, (262.5, 437.5), 113.5)
    pygame.draw.circle(screen, BLACK, (262.5, 437.5), 111.5)
    pygame.draw.circle(screen, GREEN, (262.5, 437.5), 76.5)
    pygame.draw.circle(screen, BLACK, (262.5, 437.5), 74.5)
    pygame.draw.circle(screen, GREEN, (262.5, 437.5), 39.5)
    pygame.draw.circle(screen, BLACK, (262.5, 437.5), 37.5)
    pygame.draw.line(screen, GREEN, (162.5, 454.5), (362.5, 419.5))
    pygame.draw.line(screen, GREEN, (164.5, 464.5), (364.5, 429.5))
#fonts
font = pygame.font.SysFont('Calibri', 20)
timefont = pygame.font.SysFont('Bahschrift SemiBold Condensed', 50)
weatherfont = pygame.font.SysFont('Calibri', 30)
flight_font = pygame.font.SysFont('Consolas', 16, bold=True)
small_font = pygame.font.SysFont('Calibri', 30)
text_tips_VERY_small = pygame.font.SysFont('Calibri', 20)
#draws the numbers on the ends of the radar lines
def numbers_of_the_radar():
    '''draws the radar's azimuth numbers'''
    az_360 = font.render('360', True, GREEN)
    screen.blit(az_360, (262.5, 195))
    az_180 = font.render('180', True, GREEN)
    screen.blit(az_180, (262.5, 665))
    az_90 = font.render('90', True, GREEN)
    screen.blit(az_90, (488, 437.5))
    az_270 = font.render('270', True, GREEN)
    screen.blit(az_270, (5, 437.5))
    az_45 = font.render('45', True, GREEN)
    screen.blit(az_45, (478, 205))
    az_315 = font.render('315', True, GREEN)
    screen.blit(az_315, (15, 205))
    az_225 = font.render('225', True, GREEN)
    screen.blit(az_225, (20, 655))
    az_135 = font.render('135', True, GREEN)
    screen.blit(az_135, (478, 655))

def UPPERPART_BRUHBRUH():
    '''
    displays the time, located above the radar
    '''
    gametime_hrs = gametime//60//60
    gametime_min = gametime//60 % 60
    fullmin_secreset = gametime//60
    gametime_sec = gametime - fullmin_secreset*60
    str(gametime_min).zfill(3)
    gametime_hrs_scr = timefont.render(f'HRS:{gametime_hrs}', True, CYAN)
    screen.blit(gametime_hrs_scr, (30, 25))
    gametime_min_scr = timefont.render(f'MIN:{gametime_min}', True, CYAN)
    screen.blit(gametime_min_scr, (30, 70))
    gametime_sec_scr = timefont.render(f'SEC:{gametime_sec}', True, CYAN)
    screen.blit(gametime_sec_scr, (30, 115))

def WEATHERPART_BRUHBRUHBRUH():
    '''
    contains the weather and visibility code
    '''
    global visibility_display, next_weather_changetime, current_weather, crosswind, thunder, rain, weather_is_clear, wind_course_randomizer, wind_speed_randomizer
    wind_course_randomizer = random.randint(0, 23) * 15
    wind_speed_randomizer = random.randint(0, 50)
    next_weather_changetime = gametime + random.randint(3600, 10800)
    weather_roll = random.random()
    if weather_roll < 0.02:
        current_weather = 'rain and thunder'
        visibility_display = random.uniform(0.2, 0.6)
        visibility_display = round(visibility_display, 1)
        visibility_on_screen = f'Visibility: {visibility_display}km'
    elif weather_roll < 0.18:
        current_weather = 'thunder'
        visibility_display = random.randint(1, 3)
        visibility_on_screen = f'Visibility: {visibility_display}km'
    elif weather_roll < 0.30:
        current_weather = 'rain'
        visibility_display = random.uniform(0.2, 1)
        visibility_display = round(visibility_display, 1)
        visibility_on_screen = f'Visibility: {visibility_display}km'
    elif  weather_roll < 0.80:
        current_weather = 'clear'
        visibility_display = random.randint(20, 50)
        visibility_on_screen = f'Visibility: {visibility_display}km'


def UNDER_TEXTPAD_BRUHBRUHBRUHRBRUH():
    '''
    contains code for what is under the text pad
    '''
    weather_on_the_screen = weatherfont.render(f'current weather:{current_weather}', True, GREEN)
    screen.blit(weather_on_the_screen, (1060, 470))
    visibility_on_screen = weatherfont.render(f'Visibility: {visibility_display}km', True, GREEN)
    screen.blit(visibility_on_screen, (1060, 510))
def SPAWN():
    '''
    contains plane spawning code and new arrival time
    '''
    global next_arrival_time
    if gametime >= next_arrival_time:
        newplane = PlaneCreateFile.Plane.OBJECT_CREATOR(PlaneCreateFile.Plane)
        newplane.pixel_speed = pixel_speed_base*(newplane.speed/avg_spd)
        if random.random()<land_or_no_chance:
            newplane.behavior = 'flyby'
            newplane.direction = random.uniform(0, 360)
            start_angle = (newplane.direction + 180)%360
            rad_start = math.radians(start_angle)
            newplane.x = RADAR_CX+RADAR_RADIUS*math.sin(rad_start)
            newplane.y = RADAR_CY-RADAR_RADIUS*math.cos(rad_start)
            newplane.course = int(newplane.direction)
        else:
            newplane.behavior = 'circle'
            radPS = newplane.pixel_speed/RADAR_RADIUS
            newplane.angular_speed = math.degrees(radPS)
            newplane.angle = random.uniform(0, 360)
            rad_angle = math.radians(newplane.angle)
            newplane.x = RADAR_CX+RADAR_RADIUS*math.sin(rad_angle)
            newplane.y = RADAR_CY-RADAR_RADIUS*math.cos(rad_angle)
            newplane.course = int(newplane.angle)
        planes_on_radar_rn.append(newplane)
        next_arrival_time = random.randint(min_arrival_frequency, max_arrival_frequency)+gametime

def DRAW_DA_PLANE_ON_DA_SCREEN():
    '''
    displays the plane on the screen and gives it starting instructions
    '''
    for plane in planes_on_radar_rn[:]:
        if plane.behavior == 'circle':
            plane.angle -= plane.angular_speed
            if plane.angle < 0:
                plane.angle += 360
            rad_angle = math.radians(plane.angle)
            plane.x = RADAR_CX+RADAR_RADIUS*math.sin(rad_angle)
            plane.y = RADAR_CY-RADAR_RADIUS*math.cos(rad_angle)
        elif plane.behavior == 'flyby':
            rad_dir = math.radians(plane.direction)
            dx = plane.pixel_speed*math.sin(rad_dir)
            dy = plane.pixel_speed*math.cos(rad_dir)
            plane.x += dx
            plane.y += dy
            dist = math.hypot(plane.x - RADAR_CX, plane.y - RADAR_CY)
            if dist > RADAR_RADIUS + 10:
                planes_on_radar_rn.remove(plane)
                continue
        pygame.draw.rect(screen, YELLOW, (int(plane.x) - 4, int(plane.y) - 4, 8, 8))
        pygame.draw.rect(screen, BLACK, (int(plane.x) - 4, int(plane.y) - 4, 8, 8), 1)

        alt_kft = plane.altitude // 100
        label_text = f"{plane.flight_stats} {alt_kft}"

        label = flight_font.render(label_text, True, WHITE)
        label_rect = label.get_rect()

        label_rect.topleft = (int(plane.x) + 10, int(plane.y) - 20)

        pygame.draw.line(screen, WHITE, (int(plane.x) + 4, int(plane.y)), label_rect.midleft, width=1)

        screen.blit(label, label_rect)

def InTerFACE():
    possible_cmds = ['Hello', 'Divert', 'Cleared for landing', 'Cleared for takeoff', 'Abort', 'Traffic, go lower',
                     'Traffic, go higher', 'Go to flight level FLXXX']
    for i in possible_cmds:
        current_cmd = small_font.render(i, True, GREEN)
        screen.blit(current_cmd, (565, 780))
    if chat_activity == False:
        label = small_font.render('Press T to activate chat', True, GREEN)
        screen.blit(label, (810, 220))
    else:
        pygame.draw.rect(screen, GRAY, (550, 344, 800, 101))
        pygame.draw.rect(screen, GREEN, (550, 344, 800, 101), 2)


def GO_WRITE_DA_COMMANDS_OR_NO_GAME():
    POSSIBLE_CMDS_FOR_SCREEN = ['1-Hello', '2-Divert', '3-Cleared for landing', '4-Cleared for takeoff', '5-Abort', '6-Traffic, go lower', '7-Traffic, go higher', '8-Go to flight level FL[input flight level]']
    for i, x in enumerate(POSSIBLE_CMDS_FOR_SCREEN):
        render_cmd = text_tips_VERY_small.render(x, True, GREEN)
        screen.blit(render_cmd, (570, 455 + i * 30))
def chat_history_before_gta6():
    if not chat_history:
        label = small_font.render('No communication yet.', True, GREEN)
        screen.blit(label, (810, 250))
    else:
        chat_history_meant_for_display = []
        if len(chat_history) > 12:
            chat_history_meant_for_display = chat_history[-12:]
        else:
            chat_history_meant_for_display = chat_history
        for count, i in enumerate(chat_history_meant_for_display):
            if len(i) > 70:
                i = i[0:46] + '...'
            lababel = small_font.render(i, True, GREEN)
            screen.blit(lababel, (560, 60 + count * 30))


def AMD_Ryzen_9800X3D_COMMAND_PROCESSOR_CHIP(last_command_for_display, Plane):
    break_last_cmd_to_pieces = last_command_for_display.lower().split()
    if not break_last_cmd_to_pieces:
        return 'Invalid command. Enter one of the commands listed below.'
    first_part_of_the_broken_last_cmd = break_last_cmd_to_pieces[0]
    status = ''
    if first_part_of_the_broken_last_cmd == 'hello':
        if Plane.on_ground == True:
            if Plane.fuel >= 100:
                status = f'Hello, this is {Plane.flight_stats}, fuel:{Plane.fuel}/{Plane.max_fuel}, ready to go.'
            else:
                status = f'Hello, this is {Plane.flight_stats}, fuel:{Plane.fuel}/{Plane.max_fuel}, still refueling.'
        elif Plane.on_ground == False:
            if Plane.emergency == True:
                status = f'Hello, this is {Plane.flight_stats}, we have an emergency, requesting immediate landing.'
            else:
                status = f'Hello, this is {Plane.flight_stats} reporting.'
    elif first_part_of_the_broken_last_cmd == 'divert' and Plane.on_ground == False:
        status = f'Hello, this is {Plane.flight_stats}, diverting to nearest available airport. Goodbye!'
        time.sleep(10)
    elif first_part_of_the_broken_last_cmd == 'cleared for landing':
        status = f'Hello, this is {Plane.flight_stats}, beginning landing procedure.'
    elif first_part_of_the_broken_last_cmd == 'cleared for takeoff':

    elif first_part_of_the_broken_last_cmd == 'abort':

    elif first_part_of_the_broken_last_cmd == 'traffic, go lower':

    elif first_part_of_the_broken_last_cmd == 'traffic, go higher':

    elif first_part_of_the_broken_last_cmd == 'go to flight level fl[input flight level]':


while run:
    '''
    main game cycle
    '''
    CLOCK.tick(FPS)

    if gametime <= 72000:
        gametime += 1
    else:
        gametime = 28800
    DRAW_DA_SCREEN()
    draw_a_radar_challenge()
    numbers_of_the_radar()
    UPPERPART_BRUHBRUH()
    UNDER_TEXTPAD_BRUHBRUHBRUHRBRUH()
    InTerFACE()
    SPAWN()
    GO_WRITE_DA_COMMANDS_OR_NO_GAME()
    DRAW_DA_PLANE_ON_DA_SCREEN()
    chat_history_before_gta6()
    if gametime >= next_weather_changetime:
        WEATHERPART_BRUHBRUHBRUH()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()