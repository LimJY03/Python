# Handling Exceptions with Try

def quotient(n1, n2):
    
    result = 0

    try:
        result = n1 / n2
        return result
    except ZeroDivisionError as e:
        print(e)

def get_input():

    input_values = []

    # Loop input if user entered invalid values
    while(True):
        try:
            input_values.append(float(input("Enter a number: ")))
            break
        except ValueError:
            print("Please enter a number!")

    # Loop input if user entered invalid values
    while(True):
        try:
            input_values.append(float(input("Enter the divisor: ")))
            break
        except ValueError:
            print("Please enter a number!")
    
    return input_values

def run_main():

    user_input = get_input()
    divide_result = quotient(user_input[0], user_input[1])

    while(divide_result == None):
        user_input = get_input()
        divide_result = quotient(user_input[0], user_input[1])
    
    print(divide_result)

run_main()