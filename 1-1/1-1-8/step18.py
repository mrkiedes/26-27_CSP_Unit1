# CODE TO COPY
#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)

    tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
''' Distance example
distance between ht and vt in the x direction:
abs(ht.xcor() - vt.xcor())
'''



for step in range(50):
    # Loop through all horizontal turtles in the list
	for ht in horiz_turtles:
         # Loop through all turtles in the vertical list
         for vt in vert_turtles:
            # Move each turtle forward
            ht.forward(10)
            vt.forward(10)

            # Check for collision in x
            if (abs(ht.xcor() - vt.xcor()) < 40):
                # Check for collision in y
                if (abs(ht.ycor() - vt.ycor()) < 40):

                    # Remove the turtles from the list
                    horiz_turtles.remove(ht)
                    vert_turtles.remove(vt)
                    ht.fillcolor("gray")
                    vt.fillcolor("gray")

wn = trtl.Screen()
wn.mainloop()