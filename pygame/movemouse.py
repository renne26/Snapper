#THIS IS JUST FOR TESTING
from PIL import ImageGrab
for i in range(0,3):
    screenshot = ImageGrab.grab()
    screenshot.save('e{}.png'.format(i))
    screenshot.show()