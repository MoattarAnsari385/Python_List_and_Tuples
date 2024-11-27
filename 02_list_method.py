# LIST METHODS

names = ["Hassan", "Ayesha", "Fatima", "Umer", "Moattar", "Khan"]

# Add a new name "Aroob" at the end of the list
names.append("Aroob")
print(f"After append: {names}")

# Sort the list in ascending order (alphabetical order)
names.sort()
print(f"After sort (ascending): {names}")  

# Sort the list in descending order (reverse alphabetical order)
names.sort(reverse=True)
print(f"After sort (descending): {names}") 

# Reverse the order of the list
names.reverse()
print(f"After reverse: {names}")

# Insert "Ahmed" at index 2
names.insert(2, "Ahmed")
print(f"After insert: {names}")

# Remove the first occurrence of "Ayesha" from the list
names.remove("Ayesha")
print(f"After remove: {names}") 

# Pop the item at index 4 and return it
remove_item = names.pop(4)
print(f"Removed item: {remove_item}")

# Count the number of occurrences of "Aroob" in the list\
count = names.count("Aroob")
print(f"Count of 'Aroob': {count}")

# Check if "Umer" is in the list
is_in_list = "Umer" in names
print(f"Is 'Umer' in the list: {is_in_list}")

# Find the index of "Fatima" in the list    
index = names.index("Fatima")
print(f"Index of 'Fatima': {index}")

# Join all the names in the list into a single string, separated by a comma
names_string = ", ".join(names)
print(f"Names string: {names_string}")
