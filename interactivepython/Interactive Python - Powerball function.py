# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.

def powerball():
    import random
    print "Today's numbers are",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ", and",
    print str(random.randrange(1, 60)) + ".",
    print "The Powerball number is",
    print str(random.randrange(1, 36)) + "."
    
    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
