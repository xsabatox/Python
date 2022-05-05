# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
def reset():
    """ Sets the variable 'count' to zero. """
    
    global count
    count = 0
    
    
# Increment global count.
def increment():
    """ Adds one to the variable 'count'. """
    
    global count
    count = count + 1
    
    
# Decrement global count.
def decrement():
    """ Subtracts one from the variable 'count'. """
    
    global count
    count = count - 1
    
    
# Print global count.
def print_count():
    """ Prints the variable 'count' to the console. """
       
    print count


    
###################################################
# Test

# note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
#1
#2
#-2