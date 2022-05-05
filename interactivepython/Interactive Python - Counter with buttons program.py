# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons    
def start_counter():
    timer.start()

def stop_counter():
    timer.stop()

def reset_counter():
    global counter
    counter = 0
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)
frame.add_button("Start", start_counter, 100)
frame.add_button("Stop", stop_counter, 100)
frame.add_button("Reset", reset_counter, 100)

# Start frame and timer
frame.start()
timer.start()