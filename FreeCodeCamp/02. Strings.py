# Strings

# Concatenation of strings by using '+'

string1 = "This is "
string2 = "concatenation "
string3 = "of strings."

phrase = string1 + string2 + string3

print(phrase)               # This is concatenation of strings.

# String formatting

string_normal = "This is a normal sentence written in Visual Studio Code."
string_upperCase = string_normal.upper()
string_lowerCase = string_normal.lower()

print(string_upperCase)     # THIS IS A NORMAL SENTENCE WRITTEN IN VISUAL STUDIO CODE.
print(string_lowerCase)     # this is a normal sentence written in visual studio code.

# String formatting checker

upper_check = string_upperCase.isupper() # equivalent to string_normal.upper().isupper()
lower_check = string_lowerCase.islower() # equivalent to string_normal.lower().islower()

print(upper_check)          # True
print(lower_check)          # True

# Escape Character '\'

string_newline = "This is line 1 and\nThis is line 2"
string_tab = "Add a tab here [\t]"
string_quotation = "This '' is printed without the need of \ because it is inside a \"\"" # \ is added to print "" in this case

print(string_newline)       # 
print(string_tab)           # Add a tab here [        ]
print(string_quotation)     # This ' is printed without the need of \ because it is inside a ""

# Length of string

string4 = "Spaces are counted as one character, same goes to symbols."
string4_length = len(string4)

print(string4_length)       # 58

# Character in string

string5 = "We can determine a specific character from a string based on the index."
character_selected = string5[19]
character_index = string5.index("c")    # returns the index of the first 'c'
word_index = string5.index("determi")   # returns the index of the first alphabet of 'determi'

print(character_selected)   # s
print(character_index)      # 3
print(word_index)           # 7

# Replacing word in string

string6 = "I want to replace the word Mike to Michael"
string6_replaced = string6.replace("Mike", "Michael")

print(string6_replaced)     # I want to replace the word Michael to Michael

string7 = "Mike1 and Mike2 are going to Mike's House"
string7_replaced = string7.replace("Mike", "John")  # Replaces the 4 characters 'Mike' to 'John' even though the 4 characters are not an independent word
print(string7_replaced)     # John1 and John2 are going to John's House