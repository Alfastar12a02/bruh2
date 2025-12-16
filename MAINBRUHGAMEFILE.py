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
FPS = 20
CLOCK = pygame.time.Clock()
CLOCK.tick(FPS)
run = True
RADAR_CX = 262.5
RADAR_CY = 437.5
RADAR_RADIUS = 212.5
planes_on_radar_rn = []
min_arrival_frequency = 300
max_arrival_frequency = 1800
next_arrival_time = random.randint(min_arrival_frequency, max_arrival_frequency)+gametime
avg_spd = 400.0
pixel_speed_base = 0.5
land_or_no_chance = 0.2
visibility_on_screen = 'Visibility: 20km'
visibility_display = 20
next_weather_changetime = gametime
possible_cmds = ['Hello', 'Divert', "You may land", 'You may take off', 'Abort', 'Traffic, go lower', 'Traffic, go higher', 'Go to flight level FLXXX']
#draws the main lines of the screen and decides its color
def DRAW_DA_SCREEN():
    screen.fill(GRAY)
    pygame.draw.line(screen, BLACK, (0, 175), (550, 175))
    pygame.draw.line(screen, BLACK, (550, 0), (550, 700))
    pygame.draw.line(screen, BLACK, (550, 445), (1500, 445))
    pygame.draw.line(screen, BLACK, (550, 640), (1500, 640))
    pygame.draw.line(screen, BLACK, (175, 0), (175, 175))
    pygame.draw.line(screen, BLACK, (1025, 445), (1025, 640))
    pygame.draw.line(screen, BLACK, (550, 40), (1500, 40))
#draws the radar circles
def draw_a_radar_challenge():
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
#draws the numbers on the ends of the radar lines
def numbers_of_the_radar():
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

#displays the time, located above the radar
def UPPERPART_BRUHBRUH():
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

#contains the weather and visibility code
def WEATHERPART_BRUHBRUHBRUH():
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

#contains code for what is under the text pad
def UNDER_TEXTPAD_BRUHBRUHBRUHRBRUH():
    weather_on_the_screen = weatherfont.render(f'current weather:{current_weather}', True, GREEN)
    screen.blit(weather_on_the_screen, (1060, 470))
    visibility_on_screen = weatherfont.render(f'Visibility: {visibility_display}km', True, GREEN)
    screen.blit(visibility_on_screen, (1060, 510))
#contains plane spawning code and new arrival time
def SPAWN():
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
#displays the plane on the screen and gives it starting instructions
def DRAW_DA_PLANE_ON_DA_SCREEN():
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
#main game cycle
while run:
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

    SPAWN()

    DRAW_DA_PLANE_ON_DA_SCREEN()

    if gametime >= next_weather_changetime:
        WEATHERPART_BRUHBRUHBRUH()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()