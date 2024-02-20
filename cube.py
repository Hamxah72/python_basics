import turtle

# Define colors for each face
cube_colors = ["red", "green", "blue", "yellow", "orange", "purple"]

# Define cube edge length
edge_length = 100

# Define function to draw a single square face
def draw_square(color):
  turtle.begin_fill()
  for _ in range(4):
    turtle.forward(edge_length)
    turtle.right(90)
  turtle.end_fill()
  turtle.color(color)

# Set starting position and angle
turtle.penup()
turtle.goto(-edge_length // 2, edge_length // 2)
turtle.pendown()
turtle.setheading(0)

# Draw each face of the cube
for i in range(6):
  draw_square(cube_colors[i])
  turtle.right(90)
  turtle.forward(edge_length)

# Hide the turtle and keep the window open
turtle.hideturtle()
turtle.done()
