# Functions

## Defining Functions ##

def say_hi(username, age):      # We cannot set datatype for parameter.
    '''
    This function will display a hello message to user based on their name and age.

    >>> say_hi('Bob', 19)
    Hello Bob, you are now 19 years old.
    '''

    username = str(username)    # Converts into str
    age = int(age)              # Converts into int
    
    print("Hello " + username + ", you are now " + str(age) + " years old.")

def get_userinfo():
    '''
    This function gets user info and returns it as an array.
    '''

    info = []
    info.append(input("Enter a name: "))
    info.append(int(input("Enter an age: ")))

    return info                 # Breaks the function

def run_main():
    '''
    This function will execute the statements in it.
    '''

    userinfo = get_userinfo()

    say_hi("LimJY03", 19)       # Hello LimJY03, you are now 19 years old.
    say_hi(userinfo[0], userinfo[1])

run_main()

## Docstring ##

# Docstring is a triple-quoted string (which may span multiple lines) that comes immediately after the header of a function.
# It will be displayed when the help() function is called on that function.

help(say_hi)

# Output:
# say_hi(username, age)
#     This function will display a hello message to user based on their name and age.      
#    
#     >>> say_hi('Bob', 19)
#     Hello Bob, you are now 19 years old.