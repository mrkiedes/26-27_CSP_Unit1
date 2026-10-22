import turtle

car1 = turtle.Turtle()
car1.penup()
car1.goto(-100, 0)

car2 = turtle.Turtle()
car2.penup()
car2.goto(0, 100)

'''
Task 1  Where is car1?
Write an if statement that prints "car1 is west of the intersection" when car1's x position is less than 0.
'''
# Complete Task 1 Here

if car1.xcor() < 0:
    print("car1 is west of the intersection")

'''
Task 2  Has car2 arrived?
Write an if / else that prints "car2 has not reached the intersection" when car2's y position is greater than 0, and "car2 is at or past the intersection" otherwise.
'''

# Complete Task 2 Here
if car2.ycor() > 0:
    print("car2 has not reached the intersection")
else:
    print("car2 is at or past the intersection")

'''
Task 3  Challenge: Danger Zone
Write one condition using and that prints "DANGER!" when both cars are within 50 units of the intersection. 
Hint: abs() gives distance from zero, so abs(-40) is 40.
'''
#Complete Task 3 Here
if abs(car1.xcor()) < 50 and abs(car2.ycor()) < 50:
    print("DANGER!")


'''
Does "DANGER!" print now? ______   After moving to (-40, 0) and (0, 40)? ______
'''