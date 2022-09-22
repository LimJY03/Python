'''
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar 
for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

1. The year can be evenly divided by 4, is a leap year, unless:
2. The year can be evenly divided by 100, it is NOT a leap year, unless:
3. The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are 
NOT leap years. Source [http://www.timeanddate.com/date/leapyear.html]

Task

> Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
> Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the 
  is_leap function.

Input Format

> Read year, the year to test.

Constraints

> 1900 <= year <= 10^5

Output Format

> The function must return a Boolean value (True/False). Output is handled by the provided code stub.

Sample Input 0

> 1990

Sample Output 0

> False

Explanation 0

> 1990 is not a multiple of 4 hence it's not a leap year.

src: "https://www.hackerrank.com/challenges/write-a-function/problem"
'''

def is_leap(year: int) -> bool:
        
    return year % 400 == 0 if (year % 100 == 0) else year % 4 == 0

if __name__ == '__main__':

    print(is_leap(1900))
    print(is_leap(1930))
    print(is_leap(2000))