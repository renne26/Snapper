import pygame
import win32api
import win32con
import win32gui
import time
import mouse
from PIL import ImageGrab
import os

pygame.init()
screen = pygame.display.set_mode((800, 600),pygame.NOFRAME) # For borderless, use pygame.NOFRAME

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

#INITIAL VARIABLES
done = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (5, 0, 128)
animatino = [pygame.image.load('T.png'), pygame.image.load('T_eat.png')]
clock = pygame.time.Clock()
#t_end is for how long the code will run
t_end = time.time() + 60 * 0.5
#x,y for turtle
x = 50 
y = 400
vel = 50
walkCount = 0

def scan_for_turtle():
    screenshot = ImageGrab.grab()
    screenshot.save('e.png')
    print("scr")
    #do search
    os.remove("e.png") 

def add():
    global x
    time.sleep(1)
    x += vel
    scan_for_turtle() # idk where to put this function D:

def draw_turtle():
    global walkCount
    screen.fill(fuchsia)
    #shows the turtle on screen
    screen.blit(animatino[walkCount], (x,y))
    if walkCount == 0:
        walkCount +=1
    else:
        walkCount = 0
    pygame.display.update()

#where all the magic happens
while (not done and time.time() < t_end):
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    add()
    draw_turtle()

    #to control tuertle
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     x -= vel
    # elif keys[pygame.K_RIGHT]:
    #     x += vel

       
    #check = int((t_end-time.time()))/2
    #if (check == int(check)):
       # print(mouse.get_position())
        #print("x is in {} and y is in {}".format(mouse.get_position()))

    #pygame.draw.rect(screen, dark_red, pygame.Rect(-200, -200, 600, 600))