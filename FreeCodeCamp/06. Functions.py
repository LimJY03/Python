# Functions

def say_hi(username, age):      # We cannot set datatype for parameter.

    username = str(username)    # Converts into str
    age = int(age)              # Converts into int
    
    print("Hello " + username + ", you are now " + str(age) + " years old.")

def get_userinfo():             # Gets user info and returns as an array.

    info = []
    info.append(input("Enter a name: "))
    info.append(int(input("Enter an age: ")))

    return info                 # Breaks the function

def run_main():

    userinfo = get_userinfo()

    say_hi("LimJY03", 19)       # Hello LimJY03, you are now 19 years old.
    say_hi(userinfo[0], userinfo[1])

run_main()