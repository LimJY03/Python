# Classes and Objects

# Importing Students Class

from Custom_Class import students  

# Creating Objects

s1 = students('Jim', 3, 'Computer Science', 3.86, False)
s2 = students('Ben', 2, 'Photography', 4.00, False)
s3 = students('Amy', 5, 'Software Engineer', 3.72, True)

print(s1.name)                  # Jim
print(s2.year)                  # 2
print(s3.major)                 # Software Engineer

print(s1.should_honor())        # False
print(s2.should_honor())        # True
print(s3.should_honor())        # False

print(s1.years_to_graduate())   # 1 more year to go.
print(s2.years_to_graduate())   # 2 more years to go.
print(s3.years_to_graduate())   # Should graduate.