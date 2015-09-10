'''
Created on April 20, 2015
@author:   Kelvin Rodriguez
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date:
    ''' A user-defined data structure that stores and manipulates dates.
    '''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        ''' The constructor for objects of type Date.
        '''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        ''' This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        '''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        ''' Returns True if the calling object is in a leap year; False
            otherwise.
        '''
        if self.year % 400 == 0 : return True
        if self.year % 100 == 0 : return False
        if self.year % 4 == 0 : return True
        return False

    def copy(self):
        ''' Returns a new object with the same month, day, year
            as the calling object (self).
        '''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        ''' Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        '''
        return self.year == d2.year and self.month == d2.month and \
           self.day == d2.day

    def tomorrow_helper(self):
        ''' Helper method for the tomorrow() and yesterday() methods.
            Used to verify whether or not calling object falls on leap
            year.
        '''
        if self.isLeapYear() and self.month == 2 : return 29
        else : return DAYS_IN_MONTH[(self.month)]

    def tomorrow(self):
        ''' Changes the calling object so that it represents one calendar
            day after the date it originally represented.
        '''
        if self.day == self.tomorrow_helper():
            if self.month == 12:
                self.year += 1
                self.month = 1
                self.day = 1
            else:
                self.month += 1
                self.day = 1
        else : self.day += 1
    
    def yesterday(self):
        ''' Changes the calling object so that it represents one calendar
            day before the date it originally represented.
        '''
        if self.day == 1:
            if self.month == 1:
                self.year += -1
                self.month = 12
                self.day = 31
            else:
                self.month += -1
                self.day = self.tomorrow_helper()
        else : self.day += -1

    # NOTE: examples in hw file demonstrate original object being printed
    # but the unit testing does not look for this output
    def addNDays(self, N):
        ''' Changes the calling object so that it represents N calendar
            days after the date it originally represented.

            Precondition: it is assumed that N is a nonnegative integer.
        '''
        for i in range(N):
            self.tomorrow()
            print self

    # NOTE: examples in hw file demonstrate original object being printed
    # but the unit testing does not look for this output
    def subNDays(self, N):
        ''' Changes the calling object so that it represents N calendar
            days before the date it originally represented.

            Precondition: it is assumed that N is a nonnegative integer.
        '''
        for i in range(N):
            self.yesterday()
            print self

    def isBefore(self, d2):
        ''' Returns True if the calling object is a calendar date before
            the input named d2.

            Precondition: d2 is always an object of type Date and if self
            and d2 represent the same day, the method returns False.
        '''
        if self.year < d2.year : return True
        elif self.year == d2.year:
            if self.month < d2.month : return True
            elif self.month == d2.month:
                if self.day < d2.day : return True
                else : return False
            else : return False
        else : return False

    def isAfter(self, d2):
        ''' Returns True if the calling object is a calendar date after
            the input named d2.

            Precondition: d2 is always an object of type Date and if self
            and d2 represent the same day, the method returns False.
        '''
        if self.year > d2.year : return True
        elif self.year == d2.year:
            if self.month > d2.month : return True
            elif self.month == d2.month:
                if self.day > d2.day : return True
                else : return False
            else : return False
        else : return False

    def diff(self, d2):
        ''' Returns an integer representing the number of days between
            self and d2.
        '''
        if self.equals(d2) : return 0
        elif self.isBefore(d2):
            a = self.copy()
            b = d2.copy()
            days = 0
            while not a.equals(b):
                a.tomorrow()
                days += -1
            return days
        elif self.isAfter(d2):
            a = self.copy()
            b = d2.copy()
            days = 0
            while not a.equals(b):
                b.tomorrow()
                days += 1
            return days

    def dow(self):
        ''' Returns a string that indicates the day of the week of the
            object that calls it.

            Uses the given known date of November 9, 2011 as reference.
        '''
        knownDate = Date(11, 9, 2011)
        diff = self.diff(knownDate)
        if diff % 7 == 0 : return 'Wednesday'
        elif diff % 7 == 1 : return 'Thursday'
        elif diff % 7 == 2 : return 'Friday'
        elif diff % 7 == 3 : return 'Saturday'
        elif diff % 7 == 4 : return 'Sunday'
        elif diff % 7 == 5 : return 'Monday'
        elif diff % 7 == 6 : return 'Tuesday'

# END        