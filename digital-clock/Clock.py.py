# Importing tkinter for creating the window (GUI)
import tkinter as tk

# Importing time module to get current time and date
import time


# This function will run again and again to update time every second
def update_time():
    global color_index  # allows us to use and change this variable inside function

    # get current time (like 03:45:10 PM)
    current_time = time.strftime("%I:%M:%S %p")

    # get current date (like Sunday, 16 April 2026)
    current_date = time.strftime("%A, %d %B %Y")

    # update the main time text AND change its color every second
    time_label.config(
        text=current_time,
        fg=colors[color_index]  # picks next color from list
    )

    # update the glow layer (same text, darker color behind)
    glow_label.config(text=current_time)

    # update date text
    date_label.config(text=current_date)

    # move to next color in list
    color_index = (color_index + 1) % len(colors)

    # run this function again after 1 second (1000 milliseconds)
    window.after(1000, update_time)


# Create the main window of the application
window = tk.Tk()

# Set title of the window
window.title("Digital Clock")

# Set size of window (width x height)
window.geometry("400x200")

# Set background color of window
window.configure(bg="black")


# Glow layer (behind main time)
glow_label = tk.Label(
    window,
    font=("Consolas", 65, "bold"),
    fg="#003333",  # darker glow color
    bg="black"
)
glow_label.place(relx=0.5, rely=0.3, anchor="center")


# Create label to display TIME (big text)
time_label = tk.Label(
    window,
    font=("Consolas", 60, "bold"),
    fg="#362BAE",
    bg="black"
)
time_label.place(relx=0.5, rely=0.3, anchor="center")


# Create label to display DATE (smaller text)
date_label = tk.Label(
    window,
    font=("Consolas", 35),
    fg="#FFFFFF",
    bg="black"
)
date_label.place(relx=0.5, rely=0.6, anchor="center")


colors = ["#FF9D00", "#00F7FF", "#1900FF", "#FF006A"]
color_index = 0

# Start the updating process
update_time()

# Keep the window running
window.mainloop()