from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # import after disabling environ prompt
from win32gui import SetWindowPos
import tkinter as tk


root = tk.Tk()  # create only one instance for Tk()
root.withdraw()  # keep the root window from appearing

screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
win_w = 250
win_h = 300

x = round((screen_w - win_w) / 2)
y = round((screen_h - win_h) / 2 * 0.8)  # 80 % of the actual height

# pygame screen parameter for further use in code
screen = pygame.display.set_mode((win_w, win_h))

# Set window position center-screen and on top of other windows
# Here 2nd parameter (-1) is essential for putting window on top
SetWindowPos(pygame.display.get_wm_info()['window'], -1, x, y, 0, 0, 1)

# regular pygame loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True