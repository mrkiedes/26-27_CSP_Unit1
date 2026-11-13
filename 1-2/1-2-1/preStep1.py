# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.speed(0)

def draw_ring(startX, startY):
    painter.goto(startX, startY)
    painter.fillcolor("yellow")
    painter.begin_fill()
    painter.circle(100)
    painter.end_fill()

    painter.penup()
    painter.goto(startX, startY + 50)
    painter.pendown()

    painter.fillcolor("white")
    painter.begin_fill()
    painter.circle(50)
    painter.end_fill()

draw_ring(0,0)
draw_ring(200,200)
draw_ring(100,100)
draw_ring(-200,0)
draw_ring(0,-200)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()