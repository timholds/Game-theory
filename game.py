# Code to solve a single game between two players
# Tim Holdsworth, January 7st, 2018


class Player():
    ''' An object to hold a player '''

    # A function that calculates payoff
    def payoff_function(self):


class Game():
    ''' A Game Object for a single two player game'''

    # A function to solve for the nash equilibrium of a game
    def solver(self):
        solution = None
        # What type of thing is a solution to a game? Its the circumstances
        return solution


def find_unconstrained_max():
    pass


# Let the arguments be the constraints
def find_constrained_max(*args):
    # Do stuff with Lagrangian optimization
    for arg in args:

        pass


# TODO figure out what data structure to pass around constraints with

# Let the arguments be the constraints, if they exist
def find_max(*args, **kwargs):
    # If no constraints were passed in, get the unconstrained_max
    if (args = None):
        find_unconstrained_max()
    else:
        find_constrained_max(args)
