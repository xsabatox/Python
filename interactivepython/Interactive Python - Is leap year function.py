# Compute whether the given year is a leap year.

###################################################
# Is leap year formula
# Student should enter function on the next lines.

def is_leap_year(year):
    """
    Takes a gregorian calendar year,
    returns True if the year is a leap year and False otherwise.
    """
    
    # Conditional expression based on the algorithm at https://en.wikipedia.org/wiki/Leap_year
    if year % 4 is not 0:
        return False
    elif year % 100 is not 0:
        return True
    elif year % 400 is not 0:
        return False
    else:
        return True
    

###################################################
# Tests
# Student should not change this code.

def test(year):
    """Tests the is_leap_year function."""
    if is_leap_year(year):
        print year, "is a leap year."
    else:
        print year, "is not a leap year."

test(2000)
test(1996)
test(1800)
test(2013)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
