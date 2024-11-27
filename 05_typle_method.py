food = ("burger", "pizza", "sandwich", "burger")

count_food = food.count("burger")  # Count occurrences of "burger" in the tuple
print(count_food)

index = food.index("pizza")  # Find the index of "pizza" in the tuple
print(index)

slice = food[0:3]  # Get the first 3 elements of the tuple
print(slice)

num1 = (1, 2, 3, 4, 5)
num2 = (6, 7, 8, 9, 10)
concat = num1 + num2  # Concatenate two tuples
print(concat)

t = (1, 2, 3)
print(2 in t)  # Check if 2 is in the tuple
print(4 in t)  # Check if 4 is in the tuple

number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
return_number = number * 3  # Repeat the tuple 3 times
print(return_number)

my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)  # Get the length of the tuple
print(length)

my_tuple = (1, 2, 3, 4, 5)
print(min(my_tuple))  # Get the minimum value in the tuple
print(max(my_tuple))  # Get the maximum value in the tuple

my_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = my_tuple  # Unpack the tuple into individual variables
print(a, b, c, d, e)
