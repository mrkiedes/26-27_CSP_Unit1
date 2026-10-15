'''
Intro Problem:
In a new file, create a list called my_nums that stores values 1 - 10

Write a loop that multiplies all the values by 2 and stores the results in the list.
	ie: 1 -> 2, 2 -> 4, 3 -> 6

Output the entire list with a print statement
'''

# Define a list
my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the values
for num in range(len(my_nums)):
    # Double the values
    my_nums[num] *= 2

# Print the list
print(my_nums)