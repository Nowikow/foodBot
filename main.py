import spidev as SPI
import logging
import libs.ST7789
import time

import drawer

from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

# Display inizialisation
disp = libs.ST7789.ST7789() # 240x240 display with hardware SPI:
disp.Init() # Initialize library
disp.bl_DutyCycle(50)#Set the backlight to 100
########################

# Main variables declaration
screen = "" # screen mode name declaration
image = Image.new("RGB", (disp.width, disp.height), "WHITE") # image declaration

mainFont = ImageFont.truetype("/home/anowd/FoodBot/fonts/main_font.ttf", 25) # Main font declaration
#mainFont = ImageFont.truetype("fonts/main_font.ttf", 25) # Main font declaration
titelFont = ImageFont.truetype("/home/anowd/FoodBot/fonts/main_font.ttf", 20) # Titel font declaration 4pi
# titelFont = ImageFont.truetype("fonts/main_font.ttf", 20) # Titel font declaration

keys = list("abcdefghijklmnopqrstuvwxyz") # Keys list declaration
current_index = 0 # Choice keyboard index declaration
############################

# Main programm cycle
try:
    screen = drawer.change_screen("Keyboard", disp, image, current_index, keys, mainFont) # Draw a keyboard first time

    while True:
        match screen:
            case "Keyboard":
                if disp.digital_read(disp.GPIO_KEY_LEFT_PIN):  #move cursor left
                    current_index = drawer.move(current_index, -1, disp, image, keys, mainFont)
                elif disp.digital_read(disp.GPIO_KEY_RIGHT_PIN):  #move cursor right
                    current_index = drawer.move(current_index, 1, disp, image, keys, mainFont)
                
                elif disp.digital_read(disp.GPIO_KEY_PRESS_PIN):  #choose ok cursor
                    letterChar = keys[current_index]
                    logging.info(f"Selected key: {letterChar}")
                    screen = drawer.change_screen("FoodTitel", disp, image, current_index, letterChar, titelFont)
            
            case "FoodTitel":
                if disp.digital_read(disp.GPIO_KEY1_PIN):  #back to keyboard
                    screen = drawer.change_screen("Keyboard", disp, image, current_index, keys, mainFont)
        
        time.sleep(0.1)  # process pause

except KeyboardInterrupt:
    print(" Programm was interupted!")
########################