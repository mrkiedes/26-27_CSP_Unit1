# variable to hold solution
product = 1

# Get user input for the base and the exponent
base = int(input("What is the base of your problem?"))
exponent = int(input("What is the exponent of your problem?"))

# Write a loop to run exponent times and multiply by the base
for l in range(exponent):
    product *= base

# Print out the solution
print(product)