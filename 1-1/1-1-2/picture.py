# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

painter.fillcolor("Pink")
painter.begin_fill()
painter.circle(150)
painter.end_fill()


painter.penup()
painter.goto(100,120)
painter.pendown()

painter.fillcolor("Green")
painter.begin_fill()
painter.circle(150)
painter.end_fill()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()