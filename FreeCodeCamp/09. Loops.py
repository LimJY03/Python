# Loops

## While Loops ##

# Counter-Controlled

i = 0

while(i < 10):                  
    print("%d" % i, end = ' ')  # %d indicates that the datatype after the '%' outside of string is an integer, the integer will substitute the term %d. 
    i += 1

print("Completed.")

# Sentinel-Controlled

code = 0

while(code >= 0):               
    print(code)
    code = int(input("Enter code: "))

## For Loops ##

text = "Learning Python"

for character in text:
    print(character, end = '')  # end = '' means to end the print with '' without breaking the line.

print("")                       # Breaks the line

programming_lang = ['Java', 'Python', 'JavaScript', 'HTML', 'CSS']

for language in programming_lang:
    print(language, end = ', ')

print("")                       # Breaks the line

# Counter-Controlled

for index in range(len(programming_lang)):
    print(programming_lang[index], end = ', ')

print("")                       # Breaks the line

for num in range(10, 30, 2):    # Loops from 10 to 30 excluded or [10, 30) with increment of 2 per loop.
    print(num, end = ' ')