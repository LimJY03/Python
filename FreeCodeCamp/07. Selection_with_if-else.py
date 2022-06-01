# If-Else

def determine_max(num1, num2, num3):
    
    if((num1 >= num2) & (num1 >= num3)):
        return num1
    elif((num2 >= num1) & (num2 >= num3)):
        return num2
    else:
        return num3

def get_numbers():

    userinput = []

    userinput.append(int(input("Enter a number: ")))
    userinput.append(int(input("Enter a number: ")))
    userinput.append(int(input("Enter a number: ")))

    return userinput

def run_main():

    number_set = get_numbers()
    max = determine_max(number_set[0], number_set[1], number_set[2])

    print("The greater number is " + str(max) + ".")

run_main()