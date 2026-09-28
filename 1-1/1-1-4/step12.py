
import turtle as trtl

# define the color variables
color1 = "yellow"
color2 = "green"

# Define the screen
wn = trtl.Screen()
width = 400
height = 300

# Define the turtle
painter = trtl.Turtle()

# Make the turtle fast!
painter.speed(0)

# Set color 1
painter.color(color1)

# Start assuming we will draw
answer = "y"
# Loop until the user is bored
while (answer == "y"):
    # erase what is on the current window
    wn.clearscreen()
    # Start in the middle
    painter.goto(0, 0)

    # Set up the space counter
    space = 1

    # Get angle form the user
    angle = int(input("angle:"))
    seg = int(360 / angle)

    while painter.ycor() < height:
       if space % 100 == 0:
        painter.fillcolor(color2)
        painter.color(color2)

       if space % 200 == 0:
        painter.fillcolor(color1)
        painter.color(color1)

       painter.right(angle)
       painter.forward(2 * space + 10)  # experiment
       painter.begin_fill()
       painter.circle(3)
       painter.end_fill()
       space = space + 1

    answer = input("again?")

wn.bye()