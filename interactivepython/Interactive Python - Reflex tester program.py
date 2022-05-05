# Reflex tester

###################################################
# Student should add code where relevant to the following.
import simplegui 

total_ticks = 0
first_click = True

# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    
# Button handler
def click():
    global total_ticks
    global first_click
    if first_click:
        first_click = False
        timer.start()
    else:
        timer.stop()
        print 'Reflex test: ' + str(total_ticks * 10) + ' milliseconds.'
        total_ticks = 0
        first_click = True

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()