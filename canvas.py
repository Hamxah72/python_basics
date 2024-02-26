from tkinter import *

# Create the main window
root = Tk()
root.title("Tkinter Canvas Example")

# Create a canvas widget
canvas = Canvas(root, width=400, height=300, bg="lightblue")
canvas.pack()

# Draw a rectangle
rectangle = canvas.create_rectangle(50, 50, 150, 100, fill="red", outline="black")

# Draw an oval
oval = canvas.create_oval(200, 50, 300, 100, fill="green")

# Draw a line
line = canvas.create_line(100, 150, 300, 250, fill="blue", width=3)

# Draw an arc
arc = canvas.create_arc(50, 200, 150, 300, start=0, extent=150, fill="yellow")

# Draw text
text = canvas.create_text(200, 250, text="Tkinter Canvas", font=("Arial", 20), fill="purple")

# Add an image (replace "image.png" with your image path)
# image = PhotoImage(file="image.png")
#image_id = canvas.create_image(300, 200, image=image)

# Start the main event loop
root.mainloop()
