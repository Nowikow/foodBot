from PIL import Image,ImageDraw,ImageFont
from get_food import get_recipe_titel

#draw mode logic
def change_screen(screenName, display, image, index, txt, font):
    display.clear()

    match screenName:
        case "Keyboard":
            draw_keyboard_img(display, image, index, txt, font)
        
        case "FoodTitel":
            draw_food_titel(display, image, txt, font)

    return screenName
################

#Keyboard logic
def draw_keyboard_img(display, image, index, keys, font):

    draw = ImageDraw.Draw(image) # Create blank image for drawing
    draw.rectangle((0, 0, display.width, display.height), fill="WHITE") # Clear display

    for i, key in enumerate(keys): # Make a keyboard buttons
        x = 10 + (i % 6) * 40  
        y = 20 + (i // 6) * 40
        color = "BLACK" if i != index else "RED"
        draw.text((x, y), key, fill=color, font=font)
    
    display.ShowImage(image) # Show result imgs

def move(index, step, display, image, keys, font): # Move cursor logic
    new_index = (index + step) % len(keys)
    draw_keyboard_img(display, image, new_index, keys, font)
    return new_index
##################

#Food titel draw logic
def draw_food_titel(display, image, txt, font):

    draw = ImageDraw.Draw(image) # Create blank image for drawing.
    draw.rectangle((0, 0, display.width, display.height), fill="WHITE") # Clear display
    titel = get_recipe_titel(txt) # Get a random food titel by letter

    
    max_line_length = 240 // font.getsize('A')[0] # Max line length
    words = titel.split() # Split the titel

    lines = [] # Line array declaration
    line = "" # Line for array declaration

    for word in words: # Count the line and lines
        if len(line + " " + word) <= max_line_length:
            line += " " + word if line else word  
        else:
            lines.append(line)
            line = word
    
    if line: # Add the last line
        lines.append(line)
    
    line_height = sum([font.getsize(line)[1] for line in lines]) # Lines height
    y = (240 - line_height) // 2 # Start vertical postiton

    for line in lines: # Draw the lines
        text_width, text_height = draw.textsize(line, font=font)
        x = (240 - text_width) // 2  # Start horizontal postiton
        draw.text((x, y), line, font=font, fill="BLACK")
        y += text_height  # To next line
    
    display.ShowImage(image) # Show result imgs
    
    # text_width, text_height = draw.textsize(titel, font=font) # Get a text size 

    # x = (240 - text_width) // 2
    # y = (240 - text_height) // 2  # Get x and y params for text

    # draw.text((x, y), titel, font=font, fill="BLACK") # Draw a text
######################