import pygame
import win32api
import win32con
import win32gui
import time
import mouse
from PIL import ImageGrab
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # import after disabling environ prompt
import tkinter as tk
from keras_Model import ten
from Genshincheck import move

if __name__=='__main__': 
    root = tk.Tk()  # create only one instance for Tk()
    root.withdraw()  # keep the root window from appearing

    screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
    x = round((screen_w) / 2)
    y = round((screen_h) / 2 * 0.8)  # 80 % of the actual height

    screen = pygame.display.set_mode((screen_w, screen_h))
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 1)
    # pygame.init()
    # screen = pygame.display.set_mode((0,0),pygame.NOFRAME) # For borderless, use pygame.NOFRAME

    done = False
    fuchsia = (255, 0, 128)  # Transparency color
    dark_red = (5, 0, 128)

    # Create layered window
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                        win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    # Set window transparency color
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

    #INITIAL VARIABLES
    animatino = [pygame.image.load('pygame\TT.png'), pygame.image.load('pygame\TO.png')]
    clock = pygame.time.Clock()
    #t_end is for how long the code will run
    t_end = time.time() + 60 * 2
    #x,y for turtle
    x = 0 
    y = 0
    vel = 300
    is_cool =  True
    is_hunt = False
    on_screen = False
    is_bite = 1
    once = 1
    def scan_for_turtle():
        global is_hunt
        screenshot = ImageGrab.grab()
        screenshot.save('e.png')
        result = int(ten())
        #print("AFTER REVIEWING YOUR IMAGE RESULT:{}".format(result))
        if result and once:
            is_hunt = True
            move()
        os.remove("e.png") 
        return is_hunt

    def ishunt(is_hunt):
        global x,y,on_screen,is_bite
        if is_hunt:
            is_bite = False
            #will pass in variables for now we assummme he hunting (690,690)
            legs = 5
            x_hunt,y_hunt = mouse.get_position()
            if abs(x_hunt-x)<200 and abs(y_hunt-y)<200:
                legs = 2
            y_hunt = y_hunt -75
            #print("y:{} target:{}".format(y,y_hunt))
            x_hunt_mov = int(abs(x_hunt-x)/legs)
            y_hunt_mov = int(abs(y_hunt-y)/legs)

            if x > x_hunt:
                x_hunt_mov = -1*x_hunt_mov
            if y > y_hunt:
                y_hunt_mov = -1*y_hunt_mov
            #print("move y:{}".format(y_hunt_mov))
            # if (x <= (x_hunt+10) and x >= (x_hunt-10) and y <= (y_hunt+10) and y <= (y_hunt+10)):
            #     is_hunt = False
            #     is_bite = True
            #     print("HUNT IS OVER")
            #     time.sleep(1)
            on_screen = True
            x += x_hunt_mov
            y += y_hunt_mov
            #time.sleep(1/legs)


    def draw_turtle():
        screen.fill(fuchsia)
        if (on_screen):
            #shows the turtle on screen
            imagez = pygame.transform.scale(animatino[is_bite], (150, 100))
            screen.blit(imagez, (x,y))

        pygame.display.update()

    #where all the magic happens
    while (not done and time.time() < t_end):
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        is_hunt = scan_for_turtle()
        ishunt(is_hunt)
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