# List reference problem

###################################################
# Student should enter code below

# Original list "a"
a = [5, 3, 1, -1, -3, 5]
print "a =", a

# Referenced list "b"
b = a
print "b =", b

# Updating the first value of "b" to zero
b[0] = 0
print "b[0] = 0"
print "b =", b

# Checking the first value of "a"
print "a =", a

###################################################
# Explanation
# Updating a value in a referenced list also updates 
# the value in the original list.