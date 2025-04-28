import tkinter as tk
from tkinter import Entry, Label, Button
from PIL import Image, ImageTk, ImageFilter

# Function to handle login button click
def login_action():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}")
    print(f"Password: {password}")

# Initialize the main application window
root = tk.Tk()
root.geometry("1280x720")
root.title("Login Page")

# Load and set the background image
try:
    # Open the image and resize to fit the window
    img_original = Image.open("./img/bg_img.jpg")
    img_resized = img_original.resize((1280, 720), Image.LANCZOS)
    img_blur = img_resized.filter(ImageFilter.GaussianBlur(3))  # Add slight blur
    bg_image = ImageTk.PhotoImage(img_blur)
except Exception as e:
    print("Error loading image:", e)
    bg_image = None

# Set the background image
if bg_image:
    bg_label = Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    root.configure(bg="gray")  # Fallback to gray background if image fails

# Create a transparent overlay for the login form
form_frame = tk.Frame(root, bg="#ffffff", bd=2, highlightthickness=2)
form_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

# Add a title label
title_label = Label(
    form_frame,
    text="Login",
    font=("Arial", 24, "bold"),
    # bg="",
    fg="#333333",
)
title_label.pack(pady=20)

# Username field
username_label = Label(
    form_frame, text="Username", font=("Arial", 14), bg="#ffffff", fg="#333333"
)
username_label.pack(pady=5)
username_entry = Entry(form_frame, font=("Arial", 14), width=30, bd=2, relief="groove")
username_entry.pack(pady=5)

# Password field
password_label = Label(
    form_frame, text="Password", font=("Arial", 14), bg="#ffffff", fg="#333333"
)
password_label.pack(pady=5)
password_entry = Entry(
    form_frame, font=("Arial", 14), show="*", width=30, bd=2, relief="groove"
)
password_entry.pack(pady=5)

# Login button
login_button = Button(
    form_frame,
    text="Login",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    relief="raised",
    bd=2,
    command=login_action,  # Attach the login_action function
)
login_button.pack(pady=16)
# Run the application
root.mainloop()