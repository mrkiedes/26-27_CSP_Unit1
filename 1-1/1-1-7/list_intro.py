# Defining two lists (numbers and words)
list1 = [3,4,5,6,7]
list2 = ["hello", "world"]

## Display Examples:
# Output World
print(list2[1])

# Ouptup 5
print(list1[2])

## Change values in a list
# Access the list via the ID
list2[0] = "Goodbye"
print(list2[0])


# Using a Loop with a List
for num in list1:
    # Printing elements - list is unchanged
    # print(num)

    #Popping an element removes it, but lets you access it
    print(list1.pop())
    print(list1)








