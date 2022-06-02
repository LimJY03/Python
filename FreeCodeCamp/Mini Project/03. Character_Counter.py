def character_counter(text, char):

    lower_char_count = 0
    upper_char_count = 0

    for letter in text:

        if(letter == char.lower()): 
            lower_char_count += 1
        elif(letter == char.upper()):
            upper_char_count += 1
        else:
            continue
    
    return [lower_char_count, upper_char_count]

def get_input():

    user_input = [input("Enter a long text: ")]
    char = input("Enter a character:")

    user_input.append(char[0])

    return user_input

def run_main():

    user_input = get_input()
    character_count = character_counter(user_input[0], user_input[1])

    print("There are %d '%s' and %d '%s' in the text." % (character_count[0], user_input[1].lower(), character_count[1], user_input[1].upper()))

run_main()
