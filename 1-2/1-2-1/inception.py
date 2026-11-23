def my_function():
    print("Does Stuff")

def your_function():
    print("Does other stuff")

def other_function():
    my_function()
    your_function()

other_function()