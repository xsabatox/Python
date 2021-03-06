# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import simplegui

# Define event handlers for four buttons
def reset():
    global count
    count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

def print_count():
    print count
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Count operations", 200, 200)
frame.add_button("Reset", reset, 100)
frame.add_button("Increment", increment, 100)
frame.add_button("Decrement", decrement, 100)
frame.add_button("Print", print_count, 100)

# Start the frame animation
frame.start()
    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
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
# Expected output from test

#1
#2
#-2
