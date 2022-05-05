# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

game_range = 100

# helper function to start and restart the game
def new_game():
    global game_range
    global secret_number
    global rem_guesses
    secret_number = random.randrange(0, game_range)
    rem_guesses = int(math.ceil(math.log((game_range - 0 + 1), 2)))
    print "New game. Range is [0," + str(game_range) + ")"
    print "Number of remaining guesses is " + str(rem_guesses)
    print ""

# define event handlers for control panel
def range100():
    global game_range 
    game_range = 100
    new_game()

def range1000():
    global game_range
    game_range = 1000
    new_game()
    
def input_guess(guess):
    print "Guess was " + guess
    if int(guess) == secret_number:
        print "Correct!"
        print ""
        new_game()
    else:
        global rem_guesses
        rem_guesses -= 1
        if rem_guesses > 0:
            print "Number of remaining guesses is " + str(rem_guesses)
            guess = int(guess)
            if guess > secret_number:
                print "Lower"
                print ""
            elif guess < secret_number:
                print "Higher"
                print ""
        else:
            print "You ran out of guesses.  The number was",
            print secret_number
            print ""
            new_game()

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Input guess", input_guess, 144)
frame.add_button("Range is [0,100)", range100, 150)
frame.add_button("Range is [0,1000)", range1000, 150)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric