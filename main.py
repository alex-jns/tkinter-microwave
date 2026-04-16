import tkinter as tk
import winsound

# Global variables available for each function; initializes as these values
minutes = 0
seconds = 0
after_id = None
isOpen = False
hasFood = False

# Occurs when the "Door" button is clicked
def microwave_door():
    # Use global variables
    global isOpen, hasFood

    # Open the door if it is not open
    if not isOpen:

        # Display food if there is food inside
        if not hasFood:
            timer_label.place_forget()
            new_img = tk.PhotoImage(file="microwave_open.png")
            microwave_image.configure(image=new_img)
            microwave_image.image = new_img
            isOpen = True
        
        # Do not display food because there is no food inside
        if hasFood:
            timer_label.place_forget()
            new_img = tk.PhotoImage(file="microwave_open_food.png")
            microwave_image.configure(image=new_img)
            microwave_image.image = new_img
            isOpen = True
    
    # If the door is open, close it
    else:
        timer_label.place(x=420, y=40)
        new_img = tk.PhotoImage(file="microwave_closed.png")
        microwave_image.configure(image=new_img)
        microwave_image.image = new_img
        isOpen = False

# Occurs when the "Food" button is pressed
def microwave_food():
    # Use the global variables
    global isOpen, hasFood

    # Door must be open to put in food
    if isOpen:

        # If there is no food, put food into the microwave
        if not hasFood:
            new_img = tk.PhotoImage(file="microwave_open_food.png")
            microwave_image.configure(image=new_img)
            microwave_image.image = new_img
            hasFood = True
        
        # If there is food in the microwave, take it out
        else:
            new_img = tk.PhotoImage(file="microwave_open.png")
            microwave_image.configure(image=new_img)
            microwave_image.image = new_img
            hasFood = False

# Occurs when the "Start" button is clicked; starts countdown
def start_button():
    countdown()
    beep()

# Occurs when the "Start" button is clicked
def countdown():
    # Use global variables
    global minutes, seconds, after_id

    # Decrement time by 1
    seconds -= 1

    # If time goes below 0, decrement minutes by 1 and add 59 seconds
    # If minutes goes below 0, set minutes to 0 and end the countdown
    if seconds < 0:
        minutes -= 1
        if minutes < 0:
            minutes = 0
            long_beep()
            long_beep()
            return
        else:
            seconds = 59

    # Update the timer label
    update_display()

    # Recursion after 1 second
    after_id = timer_label.after(1000, countdown)

# Update the timer label
def update_display():
    # Use global variables
    global minutes, seconds

    # Display 2 digits of minutes and seconds (add leading zeroes if single digit)
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

# Occurs when a number button is pressed; passes that number to this function
def add_time(number):
    # Use global variables
    global minutes, seconds

    # Converts the numbers into a 4 char string
    combined = f"{minutes:02d}{seconds:02d}"

    # Add the new number to the end (cast to string)
    combined += str(number)

    # Take only the last 4 characters (shifts left)
    combined = combined[-4:]

    # Splice the string into two sections: first two indices and last two
    minutes = int(combined[:2])
    seconds = int(combined[2:])

    # Update the time label
    update_display()
    beep()

# Occurs when the "Stop" button is clicked; need the after_id from the after() func
def stop_button():
    global after_id

    if after_id != None:
        timer_label.after_cancel(after_id)

    beep()

# Occurs when the "Reset" button is clicked; sets global variables back to 0 and updates label
def reset_button():
    global minutes, seconds
    minutes = 0
    seconds = 0
    update_display()
    beep()

# Beep when a button is pressed
def beep():
    freq = 2000
    dur = 300
    winsound.Beep(freq, dur)

def long_beep():
    freq = 1500
    dur = 500
    winsound.Beep(freq, dur)

# Create a Tkinter instance
app = tk.Tk()
app.title("Microwave")

# Create a frame
frame = tk.Frame()
frame.grid()

# Buttons 0-9 are used to add numbers to the timer; positioned in a grid
button_1 = tk.Button(app, text="1", command=lambda: add_time(1))
button_1.grid(row=1, column=1, ipadx=10, ipady=10, padx=10, pady=10)

button_2 = tk.Button(app, text="2", command=lambda: add_time(2))
button_2.grid(row=1, column=2, ipadx=10, ipady=10, padx=10, pady=10)

button_3 = tk.Button(app, text="3", command=lambda: add_time(3))
button_3.grid(row=1, column=3, ipadx=10, ipady=10, padx=10, pady=10)

button_4 = tk.Button(app, text="4", command=lambda: add_time(4))
button_4.grid(row=2, column=1, ipadx=10, ipady=10, padx=10, pady=10)

button_5 = tk.Button(app, text="5", command=lambda: add_time(5))
button_5.grid(row=2, column=2, ipadx=10, ipady=10, padx=10, pady=10)

button_6 = tk.Button(app, text="6", command=lambda: add_time(6))
button_6.grid(row=2, column=3, ipadx=10, ipady=10, padx=10, pady=10)

button_7 = tk.Button(app, text="7", command=lambda: add_time(7))
button_7.grid(row=3, column=1, ipadx=10, ipady=10, padx=10, pady=10)

button_8 = tk.Button(app, text="8", command=lambda: add_time(8))
button_8.grid(row=3, column=2, ipadx=10, ipady=10, padx=10, pady=10)

button_9 = tk.Button(app, text="9", command=lambda: add_time(9))
button_9.grid(row=3, column=3, ipadx=10, ipady=10, padx=10, pady=10)

button_0 = tk.Button(app, text="0", command=lambda: add_time(0))
button_0.grid(row=4, column=1, ipadx=10, ipady=10, padx=10, pady=10)

open_close_button = tk.Button(app, text="Door", command=lambda: microwave_door())
open_close_button.grid(row=4, column=2, ipadx=10, ipady=10, padx=10, pady=10)

food_button = tk.Button(app, text="Food", command=lambda: microwave_food())
food_button.grid(row=4, column=3, ipadx=10, ipady=10, padx=10, pady=10)

start_button = tk.Button(app, text="Start Timer", command=start_button)
start_button.grid(row=5, column=1)

stop_button = tk.Button(app, text="Stop Timer", command=stop_button)
stop_button.grid(row=5, column=2)

reset_button = tk.Button(app, text="Reset Timer", command=reset_button)
reset_button.grid(row=5, column=3)

# Creates the background image of the application (microwave)
img = tk.PhotoImage(file="microwave_closed.png")
microwave_image = tk.Label(app, image=img)
microwave_image.grid(row=0, rowspan=6, column=0)

# Creates the timer label; positioned purposefully (not on the grid)
timer_label = tk.Label(app, text="", bg="#3D586B", fg="light blue", width=9, height=0, pady=0)
timer_label.place(x=420, y=40)

# Refresh timer to show 00:00
update_display()

# Application window is not resizeable
app.resizable(False, False)

# Start the main loop
app.mainloop()