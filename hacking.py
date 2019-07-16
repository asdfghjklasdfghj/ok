from uagame import Window 
import random
from time import sleep

window = Window('hacking', 600, 500)
window.set_font_color("white")
window.set_font_name("couriernew")
window.set_bg_color("black")
window.set_font_size(18)
answer = random.randint(1, 7)

if answer == 1:
    real = "DOG"
elif answer == 2:
    real = "CAT"
elif answer == 3:
    real = "FROG"
elif answer == 4:
    real = "FOX"
elif answer == 5:
    real = "RAT"
elif answer == 6:
    real = "BEAR"    
else:
    real = "WOLF"
length = len(real)

tries = 3
#line_y = 0
string_height = window.get_font_height()
while tries > 0:
    line_y = 0
    window.set_font_color("white")
    window.draw_string(str(tries)+ " ATTEMPT(S) LEFT", 0, line_y)
    window.update()
    line_y = line_y + string_height
    
    window.draw_string("DOG", 0, line_y)
    window.update()
    line_y = line_y + string_height
    window.draw_string("CAT", 0, line_y)
    window.update()
    line_y = line_y + string_height
    window.draw_string("FROG", 0, line_y)
    window.update()
    line_y = line_y + string_height
    window.draw_string("FOX", 0, line_y)
    window.update()
    line_y = line_y + string_height
    window.draw_string("RAT", 0, line_y)
    window.update()
    line_y = line_y + string_height
    window.draw_string("BEAR", 0, line_y)
    window.update()
    line_y = line_y + string_height
    window.draw_string("WOLF", 0, line_y)
    window.update()
    line_y = line_y + string_height    
    place = line_y + string_height
    

    guess = window.input_string("ENTER PASSWORD > ", 0, line_y)

    window.clear()

    if guess == real:
        window.set_font_color("green")
        window.draw_string("SUCCESS!!!", 0, 0)
        window.update()
        tries = -1
    else:
        window.set_font_color("red")
        window.draw_string("WRONG TRY AGAIN", 0, place)
        place = place + string_height
        window.set_font_color("blue")
        window.draw_string(" out of " + str(length) + " letters correct", 0, place)
        window.update()
        tries = tries - 1
window.clear()        
if tries == 0:
    window.clear()
    window.set_font_color("red")
    window.draw_string("FAILURE", 0, 0)
sleep(1)

window.set_font_color("white")
window.input_string("PRESS ENTER TO QUIT", 0, line_y)
window.close() 
