daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def isMonthValid(month):
    if (month <1 or month >12 ):
        return False
    return True

def daysInMonth(year, month):
    if not isMonthValid(month):
        return  -1
    if month == 2 and isLeapYear(year):
        return 29
    return daysOfMonths[month-1]

def nextDay(year, month, day):

    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def isYearValid(year):
    if year <0:
        return False
    return True

def isDayValid(year, month, day): #2017, 2, 999
    validDays = daysInMonth(year, month)

    # print day=999, validDays =28
    if day<1 or day> validDays:
        return False
    return True

def dateAreValid(year1, month1, day1, year2, month2, day2):

    if  not isYearValid(year1) or  not isYearValid(year2):
        return False
    if  not isMonthValid(month1) or  not isMonthValid(month2):
        return False
    if  not isDayValid(year1, month1, day1) or  not isDayValid(year2, month2, day2):
        return False
    return True


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def testCode():


    assert (daysInMonth(2012, 1) == 31)
    assert daysInMonth(2012, 2) == 29
    assert daysInMonth(2017, 2) == 28
    assert daysInMonth(2017, 4) == 30

    assert nextDay(2017, 4, 1) == (2017, 4,2)
    assert nextDay(2016, 2, 29) == (2016, 3,1)
    assert nextDay(2017, 2, 999) == (2017, 3,1)
    assert nextDay(2016, 12, 31) == (2017, 1,1)

    assert isYearValid(1000) == True
    assert isYearValid(-1) == False

    assert isMonthValid(1) == True
    assert isMonthValid(-1) == False
    assert isMonthValid(12) == True
    assert isMonthValid(13) == False

    assert isDayValid(-1,12,32) == False
    assert isDayValid(2017,12,32) == False
    assert isDayValid(2017,13,3) == False
    assert isDayValid(2017,2,-1) == False
    assert isDayValid(2017, 2, 999) == False

    # dateAreValid(year1, month1, day1, year2, month2, day2)
    assert dateAreValid(-1,1,6,2012,12,8) == False
    assert dateAreValid(2012,12,6,-2,12,8) == False
    assert dateAreValid(2012,0,6,2012,12,8) == False
    assert dateAreValid(0,12,6,2012,13,8) == False
    assert dateAreValid(2012,12,0,2012,12,8) == False
    assert dateAreValid(2012,12,6,2012,12,0) == False
    assert dateAreValid(2012,12,32,2012,12,8) == False
    assert dateAreValid(2012,12,12,2012,2,30) == False
    assert dateAreValid(2012,12,12,2012,2,30) == False
    assert dateAreValid(2012,12,6,2012,12,8) == True
    assert dateAreValid(2012,12,12,2012,2,29) == True

    assert dateIsBefore(2012,9,30,2012,10,30) == True
    assert dateIsBefore(2017,1,1,2013,1,1) == False
    assert dateIsBefore(2012,9,12,2012,9,4) == False
    assert dateIsBefore(2012,12,6,2012,11,6) == False

testCode()
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    #dateAreValid(year1, month1, day1, year2, month2, day2)
    days = 0

    if not dateAreValid(year1, month1, day1, year2, month2, day2):
        days = -1
        return days

    assert  dateIsBefore( year2, month2, day2, year1, month1, day1) == False, "Assert Fail"

    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
    return days

def testdaysBetweenDates():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3),
                  ((2012,12,6,2012,12,8),2),
                  ((2012,6,29,2013,6,29),365),
                  ((2012,9,1,2012,9,1),0),
                  ((2012,12,6,-2,12,8),-1),
                  ((2013,1,1,1999,12,31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)

testdaysBetweenDates()
