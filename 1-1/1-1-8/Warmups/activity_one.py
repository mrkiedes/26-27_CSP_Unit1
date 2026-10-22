light = "red"
speed = 35

'''
Task 1  Stop or Go
Write an if / else statement that prints "Stop" when light is "red", and prints "Go" otherwise.
'''

# Complete Task 1 Here
if light == "red":
    print("Stop")
else:
    print("Go")

'''
Task 2  Speed Check
The speed limit is 30. Write an if / elif / else that prints "Slow down" if speed is over 30, "Speed up" if speed is under 20, and "Just right" otherwise.
'''

# Complete Task 2 Here
if speed > 30:
    print("Slow down")
elif speed < 20:
    print("Speed up")
else:
    print("Just right")

'''
Challenge (if you finish early)
Write a single condition using and that prints "Go ahead" only when the light is green and the speed is less than 30.
'''
# Complete Challenge Here
if light == "green" and speed < 30:
    print("Go ahead")