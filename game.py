# Code to solve a single game between two players
# Tim Holdsworth, January 7st, 2018

from sympy import *
Q = Symbol('Q')
p = Symbol('p')
k = Symbol('k')
q = Symbol('q')
a = Symbol('a')
s = Symbol('s')
w = Symbol('w')
x = Symbol('x')

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

class Player():
    ''' An object to hold a player '''

    def __init__(self):
        self._utility = None

    @property
    def utility(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._utility

    @utility.setter
    def utility(self, value):
        print("setter of x called")
        self._utility = value

    @utility.deleter
    def utility(self):
        print("deleter of x called")
        del self._utility

    # A function to get the utility function for a given player in a given case
    @classmethod
    def generate_utilty_function(cls, player, *cases):
        '''
        :param player: 'Retailer', 'Farmer', or 'Consumer'
        :param cases: 'FTOrg', 'FTConv', 'NFTOrg', 'NFTConv'
        :return: utility function that is symbolically differentiable
        '''

        wholesale_price = None
        retail_price = None

        Q = Symbol('Q')
        p = Symbol('p')
        k = Symbol('k')
        w = Symbol('w')
        wg = Symbol('wg')
        wc = Symbol('wg')
        w = wg + wc

        # Consumer demand function. I don't think I need this here, but I need it somewhere
        # Q = k + q + as - p


        # TODO fill in the different values in the different cases
        for case in cases:
            if player == 'Retailer':
                if case == 'FTOrg':
                    w =
                elif case == 'FTConv':
                    p =
                    w =
                    q = 0
                    a = 1
                # The non fair trade cases
                elif case == 'NFTOrg':
                    w = wg
                    a = 1
                elif case == 'NFTConv':
                    w = wc
                    q = 0
                    s = 0
                else:
                    print('Case not recognized')

            utility = p * q - w * q  # Retailer profit function
            return utility

            elif player == 'Farmer':
            if case == 'FTOrg':
                w =
            elif case == 'FTConv':
                p =
                w =
                q = 0
                a = 1
            # The non fair trade cases
            elif case == 'NFTOrg':
                w = wg
                a = 1
            elif case == 'NFTConv':
                w = wc
                q = 0
                s = 0
            else:
                print('Case not recognized')

        farmer_profit_function = (w * q) - (a + b * qhat) * qhat
        utility = farmer_profit_function
        return utility

        # TODO decide if we need to do this for customer, since we dont have to optimize cust utility function
            '''
            elif player == 'Consumer':
                if case == 'FTOrg':
                    w =
                elif case == 'FTConv':
                    p =
                    w =
                    q = 0
                    a = 1
                # The non fair trade cases
                elif case == 'NFTOrg':
                    w = wg
                    a = 1
                elif case == 'NFTConv':
                    w = wc
                    q = 0
                    s = 0
                else:
                    print('Case not recognized')

            utility =   # Consumer utility function
            return utility
            '''

    # A function for optimizing symbolically
    def optimize(function, varib):
        ''' Function to symbolically maximize a function and return the maximum value
            :returns the (hopefully) global max of the function with respect to varib
        '''

        # Calculate the derivative of the post-substitution function wrt newvar
        try:
            deriv = diff(function, varib)
        except Exception as e:
            print(e)
            deriv = 'Could not calculate that ish for ya rn'
        finally:
            print('In terms of {}, derivative of profit: '.format(varib) + str(deriv))

        max = solve(deriv, varib)
        print('Max retail profit occurs when {} = '.format(varib) + 'is: ' + str(max[0]))
        return max

# Overall high level solution
# Based on a GUI, get the overall structure of a problem, including type of game and # of nodes/forks/etc
# (In the future maybe this auto structure generation could be done by NLP)
# Generate the game tree data structure
# Start solving the game tree recursively. put all nodes in a path depth wise in queue
# For each game, solve the subgame perfect equilibrium by:
# Create an NthGameObject
# Set utilities, optimize someone, get a new function in terns of the variable that's next in your chain
# Important -- need to know order of decisions in order to know which variables you are trying to substitute in & out for
# use this new sub'ed in function to solve the problem for the next variable in the q
# repeat this until you only have a certain amount of variables left

class Game():
    ''' A Game Object for a single two player game'''

    # Should initialize and store the exogenous variables here

    def __init__(self):
        self.retailer = Player()
        self.consumer = Player()

    def solve_game(self, deciding_player):
        deciding_player = None
        result = deciding_player.optimize_utility()
        return result

# Use the substitutions in the solver algorithm. thats what it means to solve a subgame? - get the constrained maximum
def substitute_functions(mainfunction, oldvar, newvar, newvarLemma):
    ''' A substitution machine for functions'''

    # Substitute newvarLemma for oldvar in mainfunction
    func = mainfunction
    func_post_sub = func.subs(oldvar, newvarLemma)
    print('Function in terms of {} (where {} substituted out)'.format(newvar, oldvar) + 'is: ' + str(func_post_sub))

    return func_post_sub

def solver(func, oldvar, newvar, *args):
    # Args here are the lemma equations we can use to substitute
    for arg in args:
        updated_func = substitute_functions(func, arg, oldvar, newvar)
    return updated_func

    # How to solve a game with constraints? How to optimize for a variable under constraints?

def main():
    game = Game()
    for game in game_tree:
        solve(game)
    FirstStageGame(game, 'Retailer').set_utility()


# TODO resolve NthStageGame to be able to work as tempalte for FirstStageGame and delete FirstStageGame code
class NthStageGame(Game, cases[0], player1, player2, decision_player):
    # Each stage has players
    p1 = player1
    p2 = player2
    # Each stage has its own payoffs - set the payoffs by
    p1.generate_utility_function()

class FirstStageGame(Game, decision_player):

    def __init__(self):
        Game.__init__(self)


    # Set the utility for the player objects
    def set_utility(self):
        self.retailer.utility = generate_utilty_function(cases[0], 'Retailer')
        self.consumer.utility = generate_utilty_function(cases[0], 'Consumer')

    result = Game().solve_game(decision_player)
    return result

# ---------- A bunch of optimization stuff that might be better done with a library
# TODO figure out what data structure to pass around constraints with
def unconstrained_optimization(function, variable):
    deriv = diff(function, variable)
    return deriv

def fits(*args):
    for arg in args:
        constraint = arg
        if function >= constraint:
            return True
        else:
            return False

# Let the args be the constraints
# TODO decide if I need to pass variable here also
def fits_constraints(function, *args):
    # For each constraint, get the function of the max that fits the constraint
    for arg in args:
        fits(arg)

# Let the arguments be the constraints
def constrained_optimzation(function, variable, **kwargs):
    # Do stuff with Lagrangian optimization
    unconstrained_max = unconstrained_optimization(function, variable)
    for arg in kwargs:
        pass
    #if unconstrained_max.fits_constraints() == True

# Let the arguments be the constraints, if they exist
def find_max(function, variable, **kwargs):
    # If no constraints were passed in, get the unconstrained_max
    if kwargs is None:
        unconstrained_optimization()
    else:
        constrained_optimzation(function, variable, **kwargs)


# A function to solve for the nash equilibrium of a game
    def solver(self):
        solution = None
        # What type of thing is a solution to a game? Its the circumstances
        return solution

    # Function to calculate consumer_demand Q in a given case for Stage4Games
    def consumer_demand_function(*cases):
        ''' Function to determine Q in a given case for a given set of params q, a, s, and k
            Example function call would be consumer_demand_function(cases[0]) for FTOrg case'''

        for case in cases:
            # The fair trade cases
            if case == 'FTOrg':
                q = q
            elif case == 'FTConv':
                q = 0  # since
                a = 1
            # The non fair trade cases
            elif case == 'NFTOrg':
                a = 1
            elif case == 'NFTConv':
                q = 0
                s = 0
            else:
                print('Case not recognized')

            # Q is consumer demand function that is true in all cases. Values of a, s,
            Q = k + q - p + (a * s)

            print('The consumer demand in case {} '.format(case) + 'is ' + str(Q))
            return Q

    # Function to calculate retailer_profit pi_r in a given case for Stage4Games
    def retailer_profit_function(*cases):
        w = Symbol('w')
        wg = Symbol('wg')
        wc = Symbol('wg')
        w = wg + wc
        wholesale_price = None
        for case in cases:
            # The fair trade cases
            if case == 'FTOrg':
                consumer_demand = consumer_demand_function(case)
                wholesale_price = w
            elif case == 'FTConv':
                consumer_demand = consumer_demand_function(case)
                wholesale_price = w
            # The non fair trade cases
            elif case == 'NFTOrg':
                consumer_demand = consumer_demand_function(case)
                wholesale_price = wg
            elif case == 'NFTConv':
                consumer_demand = consumer_demand_function(case)
                wholesale_price = wc
            else:
                print('Case not recognized')

            # Retail price is known since we know p* from stage4game, yes?
            retail_price = p

            retailer_profit = (retail_price - wholesale_price) * consumer_demand
            return retailer_profit


            # consumer = Player()
            # consumer.utility = consumer_utility_function(cases[0[)
            # retailer = Player()
            # retailer.utility = retailer_profit_function(cases[0])
            # farmer = Player()
            # farmer.utilty = farmer_profit_function(cases[0])

    # Function to calculate farmer_profit pi_f in a given case for Stage2&3Games
    def farmer_profit_function(*cases):
        ''' Calculate a farmer's profut function in a given case'''

        # Define w as marginal price increase for fair trade, wg as marginal price increase for organic
        for case in cases:
            # The fair trade cases
            if case == 'FTOrg':
                pass
            elif case == 'FTConv':
                wg = 0
            # The non fair trade cases
            elif case == 'NFTOrg':
                w = 0
            elif case == 'NFTConv':
                w = 0
                wg = 0
            else:
                print('Case not recognized')

            # TODO figure out how to store these Symbol things so all functions have access to them
            Qhat = Symbol('Qhat')
            b = Symbol('b')
            wc = Symbol('wc')
            w = Symbol('w')
            wg = Symbol('wg')

            wholesale_price = wc + w + wg
            production_cost = a + b * Q
            quantity_sold = Q
            quantity_produced = Qhat

            farmer_profit = wholesale_price * quantity_sold - production_cost * quantity_produced
            print('In case {}, farmer profit function is '.format(case) + str(farmer_profit))
            return farmer_profit

    farmer_profit_function(cases[0])

#retailer_profit = p * Q - w * Q
# Example of how to use
    # p1 = Player()
    # p1.utility = 'foo'  # setter called
    # foo = p1.utility  # getter called
    # del p1.utility  # deleter called


    # farmer = Player
    # farmer_profit_function = farmer_profit_function(case[0])
    # farmer.utilty = farmer_profit_function
    # farmer.maximize_utility() -returns utility function as an expression optimized for one value

# Instantiate all exogenous variables
# TODO decide if this should be part of Game class or NthStageGame class
# Thought - game because they will be shared across the iteration of games
def __init__(self, q, a, s, k):
    self.q = a
    self.a = a
    self.s = s
    self.k = k

# utility functions are already determined for all players*game*stage
# --- For any game at any stage, we know the utility for any player
# players have different utility at different game*stages
# players optimize their utility functions
# What is the most obvious inheritance - maybe players persist only in a stage -game
# for example, in each game, creates two player objects, assign each one a utility function accordingly

# Player objects must be able to set, get, update utility function
# Player objects must be able to optimize utility function

# What is the outcome of a stage-game? Decision maker has a decision boundary piecewise


"""
for case in cases:

    consumer = Player()
    retailer = Player()
    farmer = Player()

    game4 = 4thStageGame(consumser, retailer)
    sol4 = game4.solver()
    game3 = 3rdstagegame(retailer, farmer)
    sol3 = game3.solver()
    game2 = 2thstagegame(retailer, farmer)
    sol2 = game2.solver()
    game1 = 1ststagegame(farmer, retailer)
    sol1 = game1.solver()
"""

def substitute2(objective_equation, sub_equation, oldvar, newvar):
    f1 = objective_equation
    f2 = sub_equation
    f3 = f1.subs(oldvar, newvar)
    print('swag')
    print(f3)