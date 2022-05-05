# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
def name_to_number(name):
    """
    Converts the player's choice into a number between 0 and 4 as follows:
    0 - rock
    1 - Spock
    2 - paper
    3 - lizard
    4 - scissors
    """
    
    if name is "rock":
        return 0
    elif name is "Spock":
        return 1
    elif name is "paper":
        return 2
    elif name is "lizard":
        return 3
    elif name is "scissors":
        return 4
    else:
        return "Error: Invalid choice"

def number_to_name(number):
    """
    Converts the computer's choice into a name as follows:
    0 - rock
    1 - Spock
    2 - paper
    3 - lizard
    4 - scissors
    """
    
    if number is 0:
        return "rock"
    elif number is 1:
        return "Spock"
    elif number is 2:
        return "paper"
    elif number is 3:
        return "lizard"
    elif number is 4:
        return "scissors"

# main function
def rpsls(player_choice): 
    import random
    # print a blank line to separate consecutive games
    print " "
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if difference == 1 or difference == 2:
        print "Computer wins!"
    elif difference == 3 or difference == 4:
        print "Player wins!"
    else:
        print "Player and computer tie!"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric