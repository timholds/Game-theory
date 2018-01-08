# Code to solve a single game between two players
# Tim Holdsworth, January 7st, 2018
import scipy.optimize

# What are the variables a class should share
# What are the variables an instance of a class should share
# What is the role of getter/setter's here and properties
    # Need to get and set utility functions at each stage


# -------------------- EXOGENOUS VARIABLES ----------------------
# k is the market size,
# --- k is between 0 and unbounded on the high side.
# --- k could be between [0, 1] if market size is normalized

# q is the consumer's marginal utility of organic quality over convention.
# ---0 in cases if conventional cotton

# s is the consumer's utility for perceived ethically sourced goods
# --- 0 in case of non fair-trade, conventional cotton
# --- Exists for both fair trade and organic
# ------ Multiplied by a in case of both fair trade and organic

# a is the consumer's utility's sensitivity to fair trade, org over conventional
# --- a is between [1, 2]
# --- High a means the consumer gets more utility out of


# -------------------- ENDOGENOUS VARIABLES ----------------------
# Q is consumer demand of cotton
# --- Q is different for all four cases

# P is the retail price a consumer buys at
# --- Q and P are inversely related -> P = 1 - Q

# TODO figure out where to put these variables

cases = ['FTOrg', 'FTConv', 'NFTOrg', 'NFTConv']

def consumer_demand_function(*cases=cases[0]):
    ''''''

    q, a, s, k = None
    P = None

    # Q is consumer demand function that is true in all cases
    Q = q + a * s + k - P
    for case in cases:
    # The fair trade cases
    if case == 'FTOrg':
        pass
    else if case == 'FTConv':
        q = 0 # since
        a = 1
    # The non fair trade cases
    else if case == 'NFTOrg':
        a = 1
    else if case == 'NFTConv':

    return demand


# Instantiate all exogenous variables
def __init__(self, q, a, s, k):
    self.q = a
    self.a = a
    self.s = s
    self.k = k


class Player():
    ''' An object to hold a player '''

    # A function that defines utility function
    def utility_function(self):


class Game():
    ''' A Game Object for a single two player game'''

    # A function to solve for the nash equilibrium of a game
    def solver(self):
        solution = None
        # What type of thing is a solution to a game? Its the circumstances
        return solution


def find_unconstrained_max(utilility_function):
    utility_function.optimize


# Let the arguments be the constraints
def find_constrained_max(*args):
    # Do stuff with Lagrangian optimization
    for arg in args:

        pass


# TODO figure out what data structure to pass around constraints with

# Let the arguments be the constraints, if they exist
def find_max(**kwargs):
    # If no constraints were passed in, get the unconstrained_max
    if kwargs is not None:
        find_unconstrained_max()
    else:
        find_constrained_max(args)


def main():

    consumer = Player()
    retailer = Player()
    farmer = Player()

    4thstageGameCase1 = Game()
    4thstageGameCase2 = Game()

# utility functions are already determined for all players*game*stage
# --- For any game at any stage, we know the utility for any player
# players have different utility at different game*stages
# players optimize their utility functions
# What is the most obvious inheritance - maybe players persist only in a stage -game
# for example, in each game, creates two player objects, assign each one a utility function accordingly

# Player objects must be able to set, get, update utility function
# Player objects must be able to optimize utility function

# What is the outcome of a stage-game? Decision maker has a decision boundary piecewise

for case in cases:

    consumer = Player()
    retailer = Player()
    farmer = Player()

    game4 = 4thStageGame(conumser, retailer)
    sol4 = game4.solver()
    game3 = 3rdstagegame(retailer, farmer)
    sol3 = game3.solver()
    game2 = 2thstagegame(retailer, farmer)
    sol2 = game2.solver()
    game1 = 1ststagegame(farmer, retailer)
    sol1 = game1.solver()

#Class Game() -> subclass nthstagegame (which has utility builtin)
# all games have players, all players have utility functions
class 4thStageGame(Game):


    def __init__(self, player1, player2):
        super(Game)