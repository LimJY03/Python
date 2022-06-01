def divide(num1, num2):

    if(num2 != 0):
        return num1 / num2
    else:
        print("Cannot divide by 0")
        return num1

def run_main():

    total = float(input("Enter a number: "))
    
    while(True):

        operator = input("Enter an operator: ")
        
        # User Entered =
        if(operator == '='):
            break
        
        # Invalid Operator Entered
        while((operator != '+') & (operator != '-') & (operator != '*') & (operator != '/') & (operator != '^')):

            print("Enter a valid operator! (+ or - or * or / or ^)")
            operator = input("Enter an operator: ")

        # User Entered Next Number After Operator
        num = float(input("Enter a number: "))

        # Perform Calculation Based On Operator
        if(operator == '+'):
            total += num
        elif(operator == '-'):
            total -= num
        elif(operator == '*'):
            total *= num
        elif(operator == '/'):
            total = divide(total, num)
        elif(operator == '^'):
            total **= num

    # Displays Result
    print(total)

# Execute code
run_main()