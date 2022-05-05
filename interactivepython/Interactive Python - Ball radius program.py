# Move a ball

###################################################
# Student should add code where relevant to the following.
import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    canvas.draw_circle([(HEIGHT/2), (WIDTH/2)], ball_radius, 10, "Green", "Green")
    
# Event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius += RADIUS_INCREMENT
    
def decrease_radius():
    global ball_radius
    if ball_radius > 5:
        ball_radius -= RADIUS_INCREMENT
    else:
        ball_radius = ball_radius

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.add_button("Increase radius", increase_radius, 200)
frame.add_button("Decrease radius", decrease_radius, 200)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()