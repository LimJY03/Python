# If-Else

def determine_max(num1, num2, num3):
    '''
    This function will determine the largest number and return it to the user.

    >>> determine_max(3, 7, 5)
    7
    '''
    
    if((num1 >= num2) and (num1 >= num3)):      # In Python, we use 'and' instead of & or &&
        return num1
    elif((num2 >= num1) and (num2 >= num3)):
        return num2
    else:
        return num3

def get_numbers():
    '''
    This function will get user inputs and return them in an array.
    '''

    userinput = []

    userinput.append(int(input("Enter a number: ")))
    userinput.append(int(input("Enter a number: ")))
    userinput.append(int(input("Enter a number: ")))

    return userinput

def run_main():
    '''
    This function will execute all statements in it.
    '''

    number_set = get_numbers()
    max = determine_max(number_set[0], number_set[1], number_set[2])

    print("The greater number is " + str(max) + ".")

run_main()