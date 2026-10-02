import turtle as trtl

painter = trtl.Turtle()
painter.pensize(20)
for number in range(8):
   painter.forward(75)
   painter.left(45)


painter.pensize(10)

for number in range(8):
   painter.forward(100)
   painter.right(45)
painter.forward(100)
painter.right(120)
painter.forward(100)
painter.right(120)

painter.forward(100)
painter.right(120)
painter. right(100)
painter.forward(100)
painter.right(120)
painter.forward(100)
painter.right(120)
painter.forward(100)
painter.left(50)
painter.forward(100)
painter.left(120)
painter.forward(100)
painter.left(120)
painter.forward(100)
painter.penup()
painter.circle(10)

wn = trtl.Screen()
wn.mainloop()