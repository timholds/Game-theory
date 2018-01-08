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
    def generate_utilty_function(player, *cases):
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


    # Example of how to use
    # p1 = Player()
    # p1.utility = 'foo'  # setter called
    # foo = p1.utility  # getter called
    # del p1.utility  # deleter called


    # farmer = Player
    # farmer_profit_function = farmer_profit_function(case[0])
    # farmer.utilty = farmer_profit_function
    # farmer.maximize_utility() -returns utility function as an expression optimized for one value

    # A function for optimizing utility symbolically
    def optimize_utility_function(self, function, var):
        ''' Function to symbolically maximize a function and return the maximum value'''

        # Calculate the derivative of the post-substitution function wrt newvar
        try:
            deriv = diff(function, var)
        except Exception as e:
            print(e)
            deriv = 'Could not calculate that ish for ya rn'
        finally:
            print('In terms of {}, derivative of Retailer profit: '.format(var) + str(deriv))

        max = solve(deriv, var)
        print('Max retail profit occurs when {} = '.format(var) + 'is: ' + str(max[0]))
        return max
        #return optimized_function

class Game():
    ''' A Game Object for a single two player game'''

    def __init__(self):
        self.retailer = Player()
        self.consumer = Player()

    def solve_game(self, deciding_player):
        deciding_player = None
        result = deciding_player.optimize_utility()
        return result

class FirstStageGame(Game, decision_player):

    def __init__(self):
        Game.__init__(self)


    # Set the utility for the player objects
    def set_utility(self):
        self.retailer.utility = generate_utilty_function(cases[0], 'Retailer')
        self.consumer.utility = generate_utilty_function(cases[0], 'Consumer')

    result = Game().solve_game(decision_player)
    return result

game = Game()
FirstStageGame(game, 'Retailer').set_utility()

# all games have players, all players have utility functions
class FourthStageGame(Game):

    #
    def __init__(self, player1, player2, p1utility_function, p2utility_function):
        Game.__init__(self, player1, player2)
        self.p1utility = p1utility_function
        self.p2utility = p2utility_function


    def GetEmployee(self):
        return self.Name() + ", " + self.staffnumber

# a soln should inherit w from its game
# a soln maps multiple eq with mult variables into less eq with less variables
def substitute2(objective_equation, sub_equation, oldvar, newvar):
    f1 = objective_equation
    f2 = sub_equation
    f3 = f1.subs(oldvar, newvar)
    print('swag')
    print(f3)


#(Q = k + q - p + (a * s)), (p * Q - w * Q), p, Q)
#substitute2()


def substitute(case, player, oldvar, newvar, *mainfunc, extrafunc):
    ''' A substitution machine'''

    #Q = consumer_demand_function(case) # Q = k + q - p + (a * s)
    #print(str(Q))
    #Q = k + q - p + (a * s)

    func = player.utility
    # Substitute the new variable equation into the old variable one
    func_post_sub = func.subs(oldvar, newvar)
    # Print outhe the {name of this instance of player class, like 'retailer' or 'farmer'}
    # profit is and the new string of the profit function
    print('{} profit is : '.format(player.__name__) + str(func_post_sub))
    #print('Retailer profit in terms of {} (where {} substituted out)'.format(newvar, oldvar) + 'is: ' + str(func_post_sub))

    return func_post_sub





substitute(cases[0], Q, p)



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