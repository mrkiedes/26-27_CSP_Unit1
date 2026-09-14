# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()


painter.circle(150)
painter.penup()
painter.goto(100,120)
painter.pendown()
painter.circle(150)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()