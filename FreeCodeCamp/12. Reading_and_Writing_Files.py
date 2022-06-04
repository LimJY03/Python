# Reading and Writing Files

## Read Files ##

'''
The function open() have 3 parameters: 'directory', 'mode', encoding

'directory' refers to the relative / absolute directory to the file.
'mode' refers to the filw open mode, by default is 'r'

- 'r': flie will be read-only
- 'w': file will be write-only (overwrites the content in the file)
- 'a': file will be appended (text is added to the end of the file)
- 'r+': file can be read and written

encoding refers to the rendering of the file, by default is 'utf-8'
'''

# Reading all contents in a file

with open('./Text Files/Sample_1.txt', 'r', encoding = 'utf-8') as f:

    file_content = f.read()

    print(file_content)                             # Prints all contents in the file

print("Is the file closed? " + str(f.closed))       # Is the file closed? True

# Reading lines manually in a file

with open('./Text Files/Sample_1.txt') as f:

    print(f.readline(), end = '')                   # This is Line 1.
    print(f.readline(), end = '')                   # This is Line 2.
    print(f.readline(), end = '')                   # This is Line 3.

# Reading lines using for loop

with open('./Text Files/Sample_1.txt') as f:
    
    for line in f:

        print(line, end = '')                       # Prints all contents in the file

# Importing lines into lists

with open('./Text Files/Sample_1.txt') as f:

    content_list_way1 = f.readlines()
    content_list_way2 = list(f)

    print(content_list_way1)                        # ['This is Line 1.\n', 'This is Line 2.\n', 'This is Line 3.\n', '\n', 'Lorem ipsum ...']
    print(content_list_way2)                        # ['This is Line 1.\n', 'This is Line 2.\n', 'This is Line 3.\n', '\n', 'Lorem ipsum ...']

## Write Files ##

# Writing files

with open('./Text Files/Sample_2.txt', 'w') as f:   # Since there is no Sample_2.txt in the directory, this file is created

    content = []

    content.append("This is a new file.")
    content.append("This is the second line in the new file.")
    content.append("This is the third line.")

    f.write('\n'.join(content))                     # Joins each strings in the content list separated by \n, which creates a new line.

# Appending to files

with open('./Text Files/Sample_2.txt', 'a') as f:

    f.write('\nThis is the fourth line.')           # Appends "This is the fourth line" to the file Sample_2.txt