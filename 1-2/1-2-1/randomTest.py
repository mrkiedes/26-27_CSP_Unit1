import random as rand

letters = ["A", "B", "C", "D", "E", "F", "G"]
for x in range(100):
    print(rand.choice(letters))

'''
newX = rand.randint(-200, 200)
newY = rand.randint(-200, 200)
spot.goto(newX, newY)
for x in range(100):
    print(rand.randint(1, 20))
'''