# Counter with buttons

###################################################
# Student should add code where relevant to the following.
import simplegui 

# Global variables
color = "Red"

# Timer handler
def tick():
    global color
    if color == "Red":
        color = "Blue"
    else:
        color = "Red"
    frame.set_canvas_background(color)

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(3000, tick)
frame.set_canvas_background(color)

# Start timer
frame.start()
timer.start()