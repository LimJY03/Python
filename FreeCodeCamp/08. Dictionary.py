# Dictionary

month_conversion = {
    
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

number_to_words = {

    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

month_abbreviation = input("Enter a month: ")
num = int(input("Enter a number: "))

print(month_conversion.get(month_abbreviation, "Enter a valid month's abbreviation."))
print(number_to_words.get(num, "Enter an integer from 0 to 9."))