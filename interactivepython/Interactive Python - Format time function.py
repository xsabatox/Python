# Define a function that returns formatted minutes and seconds
def format_time(input_seconds):
    """
    Takes an integer in the range (0, 3600) as the input,
    converts it to a string that states the number of 
    minutes and seconds.
    """
    
    #Use the integer division for minutes and modulo for seconds.
    minutes = input_seconds // 60
    seconds = input_seconds % 60
    return str(minutes) + " minutes and " + str(seconds) + " seconds"
    
###################################################
# Circle area formula
# Student should enter function on the next lines.



###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds