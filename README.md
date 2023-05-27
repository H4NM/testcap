# testcap.py


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

When the libraries are installed, run the script, move your mouse in the top-left corner of the area you want to screenshot later, then press 'space'.
The (X,Y) positions of your mouse will be printed to the terminal that spawned when the script ran (copy these positions, you'll use them later).
Now, repeat the same thing but in the bottom-right corner of the area you want to screenshot later. See the illustration below.

                    (100,150)
                     X - - - - - - - - - - - - -
                    |                           |
                    |                           |
                    |                           |
                    |                           |
                    |                           |
                    |                           |
                     - - - - - - - - - - - - - X (200,350)

When you have the two x and y positions, enter them respectively into the variables 'top_left_mouse_pos' and 'bottom_right_mouse_pos'.
Exit the script, either by pressing 'esc' or by closing the terminal in which it ran.
Run it again, and now you can test your automated image capture by pressing the 'screenshot' key.

