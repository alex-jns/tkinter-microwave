# Todo: Microwave door, buttons, and timer
import tkinter as tk
import winsound

minutes = 0
seconds = 0
after_id = None
isOpen = False
hasFood = False

# Opens and closes upon click
# When open and closed, changes image with PhotoImage()
# Use door_closed.png and door_open.png
def microwave_door():
    global isOpen, hasFood

    if not isOpen:
        if not hasFood:
            timer_label.place_forget()
            new_img = tk.PhotoImage(file="microwave_open.png")
            microwave_image.configure(image=new_img)
            microwave_image.image = new_img
            isOpen = True
        if hasFood:
            timer_label.place_forget()
            new_img = tk.PhotoImage(file="microwave_open_food.png")
            microwave_image.configure(image=new_img)
            microwave_image.image = new_img
            isOpen = True
    else:
        timer_label.place(x=420, y=40)
        new_img = tk.PhotoImage(file="microwave_closed.png")
        microwave_image.configure(image=new_img)
        microwave_image.image = new_img
        isOpen = False

def microwave_food():
    global isOpen, hasFood

    if isOpen:
        if not hasFood:
            new_img = tk.PhotoImage(file="microwave_open_food.png")
            microwave_image.configure(image=new_img)
            microwave_image.image = new_img
            hasFood = True
        else:
            new_img = tk.PhotoImage(file="microwave_open.png")
            microwave_image.configure(image=new_img)
            microwave_image.image = new_img
            hasFood = False

# Start button
# Use win sound for pygame beep sound
def start_button():
    countdown()
    beep()

def add_time(number):
    global minutes, seconds

    # Converts the numbers into a 4 char string
    combined = f"{minutes:02d}{seconds:02d}"

    # Add the new number to the end
    combined += str(number)

    # Take only the last 4 characters (shifts left)
    combined = combined[-4:]

    # Splice the string into two sections: first two indices and last two
    minutes = int(combined[:2])
    seconds = int(combined[2:])

    update_display()
    beep()

# Stop button
# Use win sound for pygame beep sound
def stop_button():
    global after_id

    if after_id != None:
        timer_label.after_cancel(after_id)

    beep()

# Reset button
def reset_button():
    global minutes, seconds
    minutes = 0
    seconds = 0
    update_display()
    beep()

def countdown():
    global minutes, seconds, after_id

    seconds -= 1

    if seconds < 0:
        minutes -= 1
        if minutes < 0:
            minutes = 0
            return
        else:
            seconds = 59

    update_display()

    after_id = timer_label.after(1000, countdown)

# Update the timer label
def update_display():
    global minutes, seconds
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

# Beep when a button is pressed
def beep():
    freq = 2000
    dur = 300
    winsound.Beep(freq, dur)

# Food can be taken in/out without stopping timer
def move_food():
    return ""

# Create a Tkinter instance
app = tk.Tk()
app.title("Microwave")

frame = tk.Frame()
frame.grid()

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

img = tk.PhotoImage(file="microwave_closed.png")
microwave_image = tk.Label(app, image=img)
microwave_image.grid(row=0, rowspan=6, column=0)

# Creates a Label Widget with text on it
timer_label = tk.Label(app, text="", bg="#3D586B", fg="light blue", width=9, height=0, pady=0)
timer_label.place(x=420, y=40)

# Refresh timer to show 00:00
update_display()

app.resizable(False, False)

# Start the main loop
app.mainloop()