# template for "Stopwatch: The Game"
import simplegui

# define global variables
WIDTH = 300
HEIGHT = 200
t = 0
stops = 0
whole_second_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """
    Format each value in the string A:BC.D using 
    modulo and int division in base 10 and 60.
    """
    
    deciseconds = t % 10
    seconds = ((t // 10) % 60) % 10
    decaseconds = ((t // 10) // 10) % 6
    minutes = (t // 10) // 60
    return str(minutes) + ":" + str(decaseconds) + str(seconds) + "." + str(deciseconds)

# define helper function that returns the score 
# of the reflex test game
def score():
    """ Returns a string with the game score """
    return str(whole_second_stops) + "/" + str(stops)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer.start()

def stop_timer():
    global stops
    global whole_second_stops
    if (t % 10) == 0 and timer.is_running():
        whole_second_stops += 1
        stops += 1
    elif timer.is_running():
        stops += 1
    timer.stop()

def reset_timer():
    timer.stop()
    global t
    global stops
    global whole_second_stops    
    t = 0
    stops = 0
    whole_second_stops = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    if t == 6000:
        timer.stop()
    else:
        t += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [WIDTH/3.5, HEIGHT/1.75], 50, "White")
    canvas.draw_text(score(), [WIDTH/1.2, HEIGHT/6.5], 25, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", WIDTH, HEIGHT)

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", reset_timer, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric