class students:

    # Creates Object Template
    def __init__(self, name, year, major, gpa, is_married):

        self.name = name
        self.year = year
        self.major = major
        self.gpa = gpa
        self.marriedstatus = is_married

    # Creates Object Functions
    def should_honor(self):
        '''
        This method determines if the person's GPA is >= 3.90.
        '''

        return self.gpa >= 3.90

    def years_to_graduate(self):
        '''
        This method determines the number of years left for the person to graduate.
        '''

        if(self.year >= 4):
            return "Should graduate."
        elif(self.year == 3):
            return "1 more year to go."
        elif(self.year in range(0, 3)):
            return "%d more years to go." % (4 - self.year)
        else:
            return "The year is invalid."