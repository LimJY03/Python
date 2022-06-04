# Modules

# We can import external 3rd-party modules using: pip install module_name

# Using built-in modules

import math

num1 = float(input("Enter a number: "))
roundedup = math.ceil(num1)

print("%f is rounded up to %d" % (num1, roundedup))

# Using self-made modules

import Custom_Module as cm

upperlim = round(float(input("Enter the upper limit: ")))

outcome = cm.roll(upperlim)

print(outcome)