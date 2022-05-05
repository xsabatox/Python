# SimpleGUI program template

# Import the module
import simplegui


# Define global variables (program state)
message = "My second frame!"


# Define "helper" functions
None


# Define event handler functions
def click():
    print message

    
# Create a frame
frame = simplegui.create_frame("My second frame", 200, 100)


# Register event handlers
frame.add_button("Click me!", click)


# Start frame and timers
frame.start()