def divide(num1, num2):
    '''
    This function determines the quotient of two numbers.

    >>> quotient(9, 3)
    3.0
    '''

    if(num2 != 0):
        return num1 / num2
    else:
        print("Cannot divide by 0")
        return num1

def run_main():
    '''
    This function executes all statements in it.
    '''

    total = float(input("Enter a number: "))
    
    while(True):

        operator = input("Enter an operator: ")
        
        # Choose Operation Based On Operator
        match operator:

            case '+': total += float(input("Enter a number: "))
            case '-': total -= float(input("Enter a number: "))
            case '*': total *= float(input("Enter a number: "))
            case '/': total /= float(input("Enter a number: "))
            case '^': total **= float(input("Enter a number: "))
            case '=': break

            case _:  # Default Case
                print("Enter a valid operator! (+ or - or * or / or ^)")

    # Check if the result is an integer
    if((total % 1) == 0.0): 
        total = int(total)

    print(total)

# Execute code
run_main()