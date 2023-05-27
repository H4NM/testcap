from pynput.keyboard import Key, Listener
import mouseinfo, os
from PIL import ImageGrab
from datetime import datetime


__author__ = "H4NM"

"""

This tool may screenshot a predefined area and saving the screenshot as a .png file in a catalog on your users desktop.
This facilitates the process of taking an online test where you might to simultaneously want to record the questions 
in order to review your provided answers or questions at a later stage where the test may not be available.

To use this tool, first start install the necessary libraries (pynput, mouseinfo, os, PIL (ImageGrab) and datetime)
This tool uses pynput to get the key strokes of the usage of the 'printscreen', 'space' and 'esc' buttons. 
These keys are recorded to enable the calls to the related functions.  
mouseinfo is used to retrieve the X and Y positions of the area that will be printscreened. 
os is used to get current user to get the path to the desktop and to create a catalog. 
ImageGrab from PIL is used to screenshot the area.
Lastly, datetime is used to get the current time which is used in catalog creation.


Detta verktyg kan ta en skärmavbild på ett fördefinierat område med ett knapptryck. 
Anvädning:

För att kunna köra detta verktyg, installera följande delar:
            pynput, pyautogui


1. Hitta området som du vill ta skärmavbild av
            Starta programmet och flytta muspekaren till ett hörn högst upp till vänster i det området där skärmavbilden ska tas
            tryck sedan på f2 då den printar ut positionen (x och y). Flytta sedan muspekaren till den andra positionen (längst ner till höger)
            och tryck på f2 igen. Då har du 2 x och y positioner, den första lägger du in som värde i variabeln mouse_pos_1 och det andra värdet
            i mouse_pos_2. Starta sedan om programmet och nu kan du starta provet och trycka på f1 så kommer programmet printscreena området
            och lägga bilderna i en katalog som skapats när du starta programmet.

            För att visa hur positionerna funkar:

                    (100,150)
                     X - - - - - - - - - - - - -
                    |                           |
                    |                           |
                    |                           |
                    |                           |
                    |                           |
                    |                           |
                     - - - - - - - - - - - - - X (200,350)

"""

          
# ~~~~~~~~~ VARIABLES ~~~~~~~~~ 
mouse_pos_1 = (566,124)
mouse_pos_2 = (1322,160)

img_catalog_created = False
root_storage_dir = r'C:\Users\{}\Desktop\testhelper-'.format(os.getlogin())
storage_dir =  root_storage_dir + datetime.now().strftime("%Y%m%d-%H%M%S") + '\\'
screenshot_counter = 0


# ~~~~~~~~~ FUNCTIONS ~~~~~~~~~ 
def create_catalog():
    global img_catalog_created
    img_catalog_created = True
    
    try:
        os.mkdir(storage_dir)
        print(f"Created catalog {storage_dir}")
    except Exception as e:
        print(f"Unable to create catalog {storage_dir}. Error: {e}")
        exit(1)

def screenshot():
    global screenshot_counter
    global img_catalog_created

    if not img_catalog_created:
        create_catalog()
    
    try:
        im = ImageGrab.grab(bbox=(*mouse_pos_1, *mouse_pos_2))
        screenshot_counter += 1
        img_full_path = storage_dir + f"Screenshot {screenshot_counter}.png"
        im.save(img_full_path)
        print(f"Screenshot saved to {img_full_path}")
    except Exception as e:
        print(f"Unable to screenshot. Error: {e}")

def get_mouse_pos():
    pos_x, pos_y = mouseinfo.position()
    print(f"Mouse position: ({pos_x},{pos_y})")  
           
def on_press(key):
    if key == Key.print_screen:
        screenshot()
    elif key == Key.space:
        get_mouse_pos()
    elif key == Key.esc:
        print("Closing screenshot application")
        exit(0)


if __name__ == '__main__':
    print("Listening for keystrokes.")
    with Listener(on_press=on_press) as listener:
        listener.join()
