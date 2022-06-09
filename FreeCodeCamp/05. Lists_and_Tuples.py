# Lists and Tuples

## Lists ##

# List Operations

string_list = ["pencil", "eraser", "ruler", "sharpener"]
random_list = [1.33453, "python", True, 2, 'cat']           

item_num2 = string_list[1]
item_from_num2 = string_list[1:]
item_from_num2_to_num3 = string_list[1:3]   # The item at index 3 is not included.
item_last = string_list[-1]                 # Index from front starts from 0, from behind starts from -1.

print(string_list)                          # ['pencil', 'eraser', 'ruler', 'sharpener']
print(random_list)                          # [1.33453, 'python', True, 2, 'cat']
print(item_num2)                            # eraser
print(item_from_num2)                       # ['eraser', 'ruler', 'sharpener'] 
print(item_from_num2_to_num3)               # ['eraser', 'ruler']
print(item_last)                            # sharpener

string_list[1] = 7                          # Replaces "eraser" in index 1 of string_list to 7.

print(string_list)                          # ['pencil', 7, 'ruler', 'sharpener']

# List Functions

basic_stationery = ["pencil", "highlighter", "eraser", "ruler", "scissors"]
pencil_box = ["pen", "correction tape", "glue"]

pencil_box.extend(basic_stationery)         # Combines the basic_stationery list to the behind of the pencil_box list
print(pencil_box)                           # ['pen', 'correction tape', 'glue', 'pencil', 'highlighter', 'eraser', 'ruler', 'scissors']

pencil_box.append("highlighter")            # Adds a new string "highlighter" to the behind of the pencil_box list
print(pencil_box)                           # ['pen', 'correction tape', 'glue', 'pencil', 'highlighter', 'eraser', 'ruler', 'scissors', 'highlighter']

pencil_box.insert(3, "paper clip")          # Adds a new string "paper clip" to the index 3 of the pencil_box list
print(pencil_box)                           # ['pen', 'correction tape', 'glue', 'paper clip', 'pencil', 'highlighter', 'eraser', 'ruler', 'scissors', 'highlighter']

print(pencil_box.count("highlighter"))      # 2
print(pencil_box.index("pen"))              # 0

pencil_box.sort()                           # Sorts the pencil_box lists alphabetically in ascending order. The sort() function can only sort lists containing same datatype
print(pencil_box)                           # ['correction tape', 'eraser', 'glue', 'highlighter', 'highlighter', 'paper clip', 'pen', 'pencil', 'ruler', 'scissors']

# Alternatively:

pencil_box_sorted = sorted(pencil_box)      # sorted() returns a value unlike .sort() that changes the list directly.
print(pencil_box_sorted)                    # ['correction tape', 'eraser', 'glue', 'highlighter', 'highlighter', 'paper clip', 'pen', 'pencil', 'ruler', 'scissors']

new_pencil_box = pencil_box.copy()          # Creates a copy of the pencil_box list and assign it to the new_pencil_box list

new_pencil_box.reverse()                    # Reverses the order of strings in the new_pencil_box list
print(new_pencil_box)                       # ['scissors', 'ruler', 'pencil', 'pen', 'paper clip', 'highlighter', 'highlighter', 'glue', 'eraser', 'correction tape']

pencil_box.remove("highlighter")            # Removes the first string "highlighter" found in the pencil_box list
print(pencil_box)                           # ['correction tape', 'eraser', 'glue', 'highlighter', 'paper clip', 'pen', 'pencil', 'ruler', 'scissors']

pencil_box.pop()                            # Removes the last string in the pencil_box list
print(pencil_box)                           # ['correction tape', 'eraser', 'glue', 'highlighter', 'paper clip', 'pen', 'pencil', 'ruler']

pencil_box.clear()                          # Clears the pencil_box list
print(pencil_box)                           # []

## Tuples ##

coordinates = (1, 4.3)                      # Tuples are mostly used for coordinates or CONSTANT arrays
print(coordinates)                          # (1, 4.3)

important_coordinates = [
    ("Village with Mending Villagers", (649, 66, -967)),
    ("Spider Spawner", (923, 40, -486)),
    ("Large Copper Vein", (804, 24, 52)),
    ("Zombie Spawner", (806, 28, -86))
]

print(important_coordinates[2])             # ('Large Copper Vein', (804, 24, 52))