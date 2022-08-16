'''
We will represent complex numbers in either cartesian or polar form as an array/list, using the first element as a type 
tag; the normal tags are "cart" (for cartesian) and "polar". The forms of the tags depend on the language.

> ['cart', 3, 4] represents the complex number 3+4i
> ['polar', 2, 3] represents the complex number with modulus (or magnitude) 2 and angle 3

In the same way:

> ['cart', 1, 2, 3, 4, 5, 6] includes the three complex numbers 1+2i, 3+4i, 5+6i
> ['polar', 2, 1, 2, 2, 2, 3] represents the complex numbers (2, 1), (2, 2), (2, 3) in polar form where the magnitudes are 
  2, 2, 2 and the angles 1, 2, 3

Note:

> The polar form of a complex number z = a+bi is z = (r, θ) = r(cosθ+isinθ), where r = |z| = the (non-negative) square-root 
  of a^2+b^2 is the modulus.
> In the arrays/lists beginning by a tag all terms after the tag must be integers (no floats, no strings).

Task

Given a sequence of complex numbers z in one of the previous forms we first calculate the sum s of the squared modulus of all complex elements of z if z is in correct form.

Our function sqr-modulus returns an array/list of three elements; the form of the list will depend on the language:

> The first element is a boolean:
    > True if z is in correct form as defined previously (correct type of numbers, correct tag)
    > False if z is not in correct form.
> The second element is the sum s of the squared modulus of all complex numbers in z if the returned boolean is true, -1 if it is false.
> The third element is the greatest number got by rearranging the digits of s. We will admit that the greatest number got from -1 is 1.

Examples (in general form):

> sqr_modulus(['cart', 3, 4]) -> (True, 25, 52)
> sqr_modulus(['cart', 3, 4, 3, 4]) -> (True, 50, 50)
> sqr_modulus(['polar', 2531, 3261]) -> (True, 6405961, 9665410)
> sqr_modulus(['polar', 2, 3, 2, 4]) -> (True, 8, 8)
> sqr_modulus(['polar', "2", 3]) -> (False, -1, 1)
> sqr_modulus(['polara', 2, 3]) -> (False, -1, 1)
> sqr_modulus(['cart', 3, 4.1]) -> (False, -1, 1)

src: "https://www.codewars.com/kata/5cc70653658d6f002ab170b5"
'''

def sqr_modulus(input_array):

    if (input_array[0] not in ['cart', 'polar']) or not(all(isinstance(item, int) for item in input_array[1:])) or (len(input_array) % 2 == 0): 
        return [False, -1, 1]

    if input_array[0] == 'polar': 
        del input_array[2::2]

    sum = 0

    for i in input_array[1:]:
        sum += i ** 2
    
    return [True, sum, int(''.join(sorted([digit for digit in str(sum)], reverse=True)))]

print(
    sqr_modulus(['cart', 3, 4]), 
    sqr_modulus(['cart', 3, 4, 3, 4]), 
    sqr_modulus(['polar', 2531, 3261]), 
    sqr_modulus(['polar', 2, 3, 2, 4]), 
    sqr_modulus(['polar', "2", 3]), 
    sqr_modulus(['polara', 2, 3]), 
    sqr_modulus(['cart', 3, 4.1]), 
    sep='\n'
)