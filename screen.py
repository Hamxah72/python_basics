import tkinter as tk
import time

# Define functions
def display_splash_screen():
  splash_root = tk.Tk()
  splash_root.title("Splash Screen")

  # Customize the splash screen appearance here
  splash_width = 400
  splash_height = 200
  splash_root.geometry(f"{splash_width}x{splash_height}+{int(screen_width/2 - splash_width/2)}+{int(screen_height/2 - splash_height/2)}")

  # Add a label with your app logo or message
  splash_label = tk.Label(splash_root, text="Your App Name", font=("Arial", 20), justify="center")
  splash_label.pack(fill="both", expand=True)

  # Display the splash screen for a few seconds
  splash_root.after(2000, splash_root.destroy)  # Destroy the splash screen after 2 seconds
  splash_root.mainloop()

def main_window():
  # Create your main window and application logic here
  # ...

# Get screen width and height for splash screen positioning
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

# Display the splash screen
display_splash_screen()

# Main program logic after splash screen
main_window()
