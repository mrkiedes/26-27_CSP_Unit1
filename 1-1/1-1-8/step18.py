################################################################################
#   a118_TR2_turtles_in_traffic.py
#   Example solution:
#      Extra features were added to speed up and slow down turtles,
#      change color and shape during a collision, and recover their original
#      shape and color when the keep on moving.
################################################################################
import turtle as trtl

# create two empty lists of turtles
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "classic", "square", "triangle"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "pink", "indigo", "brown"]

tloc = 50  # place turtles on screen in diff. locations
for s in turtle_shapes:
    # create a list of turtles that will move horizontally
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    # create a list of turtles that will move vertically with the
    # same shapes but different colors than the horizontal turtles
    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)

    # next turtle location
    tloc += 50

# move turtles on screen, stopping if a collision occurs
steps = 0
pixel_size = 20
distance = 3
while steps < 25:
    steps = steps + 1

    # speed up and then slow down
    distance = 3
    distance = distance + 2
    if (distance > 10):
        distance = 3

    for ht in horiz_turtles:

        for vt in vert_turtles:

            # move
            ht.forward(distance)
            vt.forward(distance)

            # collision occurs if too close
            if (abs(ht.xcor() - vt.xcor()) < pixel_size):
                if (abs(ht.ycor() - vt.ycor()) < pixel_size):
                    # remember color and shape of turtles
                    orig_ht_color = ht.fillcolor()
                    orig_ht_shape = ht.shape()
                    orig_vt_color = vt.fillcolor()
                    orig_vt_shape = vt.shape()

                    # change color and shape to indicate collision
                    # then back up a bit and recover
                    vt.fillcolor("gray")
                    vt.shape("circle")
                    vt.back(distance + 3)
                    ht.fillcolor("gray")
                    ht.shape("circle")
                    ht.back(distance + 3)

                    # restore orig shape and color
                    ht.shape(orig_ht_shape)
                    ht.fillcolor(orig_ht_color)
                    vt.shape(orig_vt_shape)
                    vt.fillcolor(orig_vt_color)

for ht in horiz_turtles:
    ht.fillcolor("gray")
for vt in vert_turtles:
    vt.fillcolor("gray")

wn = trtl.Screen()
wn.mainloop()