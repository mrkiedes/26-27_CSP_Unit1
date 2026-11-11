# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.speed(0)

painter.fillcolor("yellow")
painter.begin_fill()
painter.circle(100)
painter.end_fill()

painter.penup()
painter.goto(0, 50)
painter.pendown()

painter.fillcolor("white")
painter.begin_fill()
painter.circle(50)
painter.end_fill()



# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()