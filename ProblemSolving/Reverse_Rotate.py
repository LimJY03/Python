'''
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of 
size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; 
otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If:

> sz is <= 0 or if str is empty return ""
> sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

Examples:

> revrot("123456987654", 6) --> "234561876549"
> revrot("123456987653", 6) --> "234561356789"
> revrot("66443875", 4) --> "44668753"
> revrot("66443875", 8) --> "64438756"
> revrot("664438769", 8) --> "67834466"
> revrot("123456779", 8) --> "23456771"
> revrot("", 8) --> ""
> revrot("123456779", 0) --> "" 
> revrot("563000655734469485", 4) --> "0365065073456944"

Example of a string rotated to the left by one position:
> s = "123456" gives "234561".

src: "https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991"
'''

def revrot(number_string, chunk):

    # Return empty string if the conditions above are met
    if (chunk == 0) or (len(number_string) < chunk): return ''
    
    # Perform reverse or rotate function
    chunk_list = [number_string[i:i+chunk] for i in range(0, len(number_string), chunk)]

    # Remove the extra chunk
    if (len(chunk_list[-1]) != chunk): chunk_list.pop()

    # Generate new chunks into array
    final_string = []
    
    for each_chunk in chunk_list:

        sum = 0

        for digit in each_chunk: sum += int(digit) ** 3

        final_string.append(each_chunk[::-1] if (sum % 2 == 0) else each_chunk[1:] + each_chunk[0] if chunk != 1 else each_chunk)

    return ''.join(final_string)

print(
    revrot("123456987654", 6),
    revrot("123456987653", 6),
    revrot("66443875", 4),
    revrot("66443875", 8),
    revrot("664438769", 8),
    revrot("123456779", 8),
    revrot("", 8),
    revrot("123456779", 0),
    revrot("563000655734469485", 4),
    sep = '\n'
)