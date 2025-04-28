import tkinter as tk
import time
import math

def update_clock():
    """Update the clock hands with numbers along their length."""
    # Get the current time
    now = time.localtime()
    seconds = now.tm_sec
    minutes = now.tm_min
    hours = now.tm_hour % 12  # Convert 24-hour to 12-hour format

    # Calculate the angles for the clock hands
    second_angle = math.radians(seconds * 6 - 90)
    minute_angle = math.radians(minutes * 6 - 90)
    hour_angle = math.radians((hours * 30 + minutes * 0.5) - 90)

    # Draw numbers for the second hand
    draw_number_line(second_hand, seconds, second_angle, second_hand_length, "red")

    # Draw numbers for the minute hand
    draw_number_line(minute_hand, minutes, minute_angle, minute_hand_length, "blue")

    # Draw numbers for the hour hand
    draw_number_line(hour_hand, hours, hour_angle, hour_hand_length, "black")

    # Schedule the function to run again after 100 milliseconds
    root.after(100, update_clock)

def draw_number_line(hand_id, value, angle, length, color):
    """Draw a line of repeating numbers for a clock hand without collision."""
    canvas.delete(hand_id)  # Clear previous numbers
    spacing = 15  # Distance between each number
    for i in range(1, int(length / spacing)):  # Calculate how many numbers to draw
        x = center_x + (spacing * i) * math.cos(angle)
        y = center_y + (spacing * i) * math.sin(angle)
        canvas.create_text(x, y, text=str(value), font=("Helvetica", 10), fill=color, tags=hand_id)

root = tk.Tk()
root.title("Analog Clock with Number Hands")

# Set the dimensions of the clock
clock_diameter = 400
center_x, center_y = clock_diameter // 2, clock_diameter // 2
second_hand_length = clock_diameter // 2 - 20
minute_hand_length = clock_diameter // 2 - 40
hour_hand_length = clock_diameter // 2 - 80

# Create the canvas for the clock
canvas = tk.Canvas(root, width=clock_diameter, height=clock_diameter, bg="white")
canvas.pack()

# Draw the clock face
canvas.create_oval(10, 10, clock_diameter - 10, clock_diameter - 10, outline="black", width=2)

# Draw the hour markers
for i in range(12):
    angle = math.radians(i * 30)
    x1 = center_x + (clock_diameter // 2 - 20) * math.cos(angle)
    y1 = center_y + (clock_diameter // 2 - 20) * math.sin(angle)
    x2 = center_x + (clock_diameter // 2 - 10) * math.cos(angle)
    y2 = center_y + (clock_diameter // 2 - 10) * math.sin(angle)
    canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

# Create tags for the hands
second_hand = "second_hand"
minute_hand = "minute_hand"
hour_hand = "hour_hand"

# Start the clock
update_clock()

# Run the tkinter main loop
root.mainloop()
