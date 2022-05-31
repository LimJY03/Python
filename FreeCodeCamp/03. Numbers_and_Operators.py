# Numbers

from math import * # For floor and ceil functions

## Arithmetic Operations ##

# 01. Parentheses

num1 = (5)          # = 6

# 02. Exponents

num2 = 5 ** 3       # = 125                 (Returns 5 ^ 3)
num2_1 = 25 ** 0.5  # = 5.0                 (Similar to sqrt(25))

# 03. Multiplication / Division / Modulus

num3 = 5 * 7        # = 35
num3_1 = 5 / 7      # = 0.7142857142857143  (True Division)
num3_2 = 5 // 7     # = 0                   (Returns Quotient)
num3_3 = 5 % 7      # = 5                   (Returns Remainder)

# 04. Addition / Subtraction

num4 = 5 + 7        # = 12
num4_1 = 5 - 7      # = -2

# Order of Operation (01 -> 04)

arithmetic_operation = 7 * 4 ** 5 % 6 - 3 / 2 + 1 // 8 + 9  # Grouping looks like: (((((7 * (4 ** 5)) % 6) - (3 / 2)) + (1 // 8)) + 9)

print(arithmetic_operation) # = 11.5

## Number Functions ##

# Force Convert into Datatype

num5 = -3.0
int_number = int(num5)      # = -3      (Ensures that num5 fits to be an int, can convert from str as well)
float_number = float(num5)  # = -3.0    (Ensures that num5 becomes a float, can convert from str as well)
positive_number = abs(num5) # = 3.0     (Ensures that num5 becomes positive value)

# Comparison

num6 = 5
num7 = 19

larger_number = max(num1, num2, num3, num4, num5, num6, num7)
smaller_number = min(num1, num2, num3, num4, num5, num6, num7)

print(larger_number)        # 125
print(smaller_number)       # -3.0

# Rounding Numbers

num8 = 5.3
num9 = 5.8

normal_round_down = round(num8) # 5
normal_round_up = round(num9)   # 6

force_round_down1 = floor(num8) # 5
force_round_down2 = floor(num9) # 5 (5.8 still round down to 5)

force_round_up1 = ceil(num8)    # 6 (5.3 still round up to 6)
force_round_up2 = ceil(num9)    # 6

# Printing Numbers with Texts

message = "The lucky number is " + str(num6) + "."    # String cannot concatenate with non-strings.
print(message)              # The lucky number is 5.