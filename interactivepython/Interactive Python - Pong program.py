# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PADDLE_VEL = 5

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(1, 5), random.randrange(-3, 0)]
    elif direction == LEFT:
        ball_vel = [random.randrange(-4, 0), random.randrange(-3, 0)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    # reset paddles' positions and velocities
    paddle1_pos = [[0, (HEIGHT / 2 - HALF_PAD_HEIGHT)], 
               [PAD_WIDTH, (HEIGHT / 2 - HALF_PAD_HEIGHT)], 
               [PAD_WIDTH, (HEIGHT / 2 + HALF_PAD_HEIGHT)], 
               [0, (HEIGHT / 2 + HALF_PAD_HEIGHT)]
    ]
    paddle2_pos = [[(WIDTH - PAD_WIDTH), (HEIGHT / 2 - HALF_PAD_HEIGHT)], 
               [WIDTH, (HEIGHT / 2 - HALF_PAD_HEIGHT)], 
               [WIDTH, (HEIGHT / 2 + HALF_PAD_HEIGHT)], 
               [(WIDTH - PAD_WIDTH), (HEIGHT / 2 + HALF_PAD_HEIGHT)]
    ]
    paddle1_vel = 0
    paddle2_vel = 0
    
    # reset scores
    score1 = 0
    score2 = 0
    
    # spawn ball in a random direction
    spawn_ball(random.choice([RIGHT, LEFT]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # bounce ball on the top and bottom of the screen
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    # left paddle (paddle1)
    if (paddle1_pos[1][1] + paddle1_vel >= 0) and (paddle1_pos[2][1] <= HEIGHT - paddle1_vel):
        paddle1_pos[0][1] += paddle1_vel
        paddle1_pos[1][1] += paddle1_vel
        paddle1_pos[2][1] += paddle1_vel
        paddle1_pos[3][1] += paddle1_vel
    
    # right paddle (paddle2)
    if (paddle2_pos[0][1] + paddle2_vel >= 0) and (paddle2_pos[3][1] <= HEIGHT - paddle2_vel):
        paddle2_pos[0][1] += paddle2_vel
        paddle2_pos[1][1] += paddle2_vel
        paddle2_pos[2][1] += paddle2_vel
        paddle2_pos[3][1] += paddle2_vel

    # draw paddles
    canvas.draw_polygon(paddle1_pos, 1, "White", "White")
    canvas.draw_polygon(paddle2_pos, 1, "White", "White") 
    
    # determine whether paddles and ball collide, count scores and increase ball velocity
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS) and (paddle1_pos[1][1] <= ball_pos[1] <= paddle1_pos[2][1]):
        ball_vel[0] = -(1.1 * ball_vel[0])
    elif (ball_pos[0] <=  PAD_WIDTH + BALL_RADIUS):
        score2 += 1
        spawn_ball(RIGHT)
    elif (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS) and (paddle2_pos[0][1] <= ball_pos[1] <= paddle2_pos[3][1]):
        ball_vel[0] = -(1.1 * ball_vel[0])
    elif (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS):
        score1 += 1
        spawn_ball(LEFT)

    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 3, HEIGHT/6.5], 50, "White")
    canvas.draw_text(str(score2), [(2 * WIDTH / 3) - 25, HEIGHT/6.5], 50, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -PADDLE_VEL
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = PADDLE_VEL
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -PADDLE_VEL
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = PADDLE_VEL

def keyup(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP["w"]) or (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
    elif (key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0        

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESTART", new_game, 150)

# start frame
new_game()
frame.start()