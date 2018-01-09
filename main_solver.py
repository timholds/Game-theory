from sympy import *
import unittest

Q = Symbol('Q')
p = Symbol('p')
k = Symbol('k')
q = Symbol('q')
a = Symbol('a')
s = Symbol('s')
w = Symbol('w')

### ------ Input Functions
def get_endog_variables(*args):
    '''Get exog variables through arguments or user input if no args'''

    if args is None:
        variables = input('Please enter your exogenous variables, as lowercase letters')
    else:
        variables = []
        for arg in args:
            variables.append(args)
    print('Variables are {}'.format([var for var in variables]))

    return variables

def get_exog_variables(*args):
    ''' Get exog variables through arguments or user input if no args'''

    if args is None:
        variables = input('Please enter your exogenous vaiables, as lowercase letters')
    else:
        variables = []
        for arg in args:
            variables.append(args)
    print('Variables are {}'.format([var for var in variables]))

    return variables

def get_decision_variables(*args):
    ''' Returns a list of decision variables'''

    decision_vars = []
    if args is None:
        print('please enter a lowercase string seperated by a comma and space')
        arg = input('what decision variable do you want to use for this round?'
                    'Who is the player that is optimizing their utility using this variable?')
        for item in arg:
            try:
                decision_vars.append(item)
            except Exception as e:
                print(e)
                print('Problem with the input and appending to a list.')
    else:
        for arg in args:
            decision_vars.append(arg)
    return decision_vars

def get_objective_func(*args, **kwargs):

    ''' Get the objective function through arguments or by user input if no args
        Objective function is:
            When the argument is one or more functions
                *args like P*Q - 1
            When the argument is one or more k,v pairs of identifier and function
                **kwardgs like tim_util = x * 2'''

    if args is None:
        obj_func_list = input('Please enter your exogenous vaiables, as lowercase letters')
    else:
        # How to handle being passed multiple objective functions?
        obj_func_list = []
        for arg in args:
            print('adding {} to list or dict of objective functions'.format(str(arg)))
            obj_func_list.append(arg)

        for key, value in kwargs.items():
            print("The value of {} is {}".format(key, value))

    print('Functions are are {}'.format([func for func in obj_func_list]))

    return obj_func_list

### ------- Calculation functions
def make_symbols_for_variables(*args):
   ''' Make symbols for sympy to manipulate based in user inputs '''
   for arg in args:
        arg = Symbol(arg)
        print(arg)
        return arg

def optimize(function, varib):
    ''' Function to symbolically maximize a function
        :returns the (hopefully) global max of the function in terms of the varib
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

def substitute_functions(main_func, oldvar, varLemma):
    ''' Take two functions with overlapps vars and substitute the lemma into the main
        :returns a symbolic function, which can be used as newVarLemma in next stage game'''
    # Substitute newvarLemma for oldvar in mainfunction
    func_post_sub = main_func.subs(oldvar, varLemma)
    #print('Function in terms of {} (where {} substituted out)'.format(newvar, oldvar) + 'is: ' + str(func_post_sub))

    return func_post_sub

def solve_one_game():
    ''' Should get all user inputs and solve a single optimization '''

    # Get user inputs for variables, objective fuctions, which to optimize
    endog_variables = get_endog_variables()
    exog_variables = get_exog_variables()
    obj_func_list = get_objective_func()
    dec_vars = get_decision_variables() # Variables you want to have out aka solved aka ready to substitute in the nxt round

    make_symbols_for_variables(endog_variables, exog_variables)
    side_eq_Q = 1 - p

    # substitute
    post_sub_func = substitute_functions(obj_func_list[0], dec_vars[0], side_eq_Q)
    # optimize
    solution_for_dec_variable_aka_new_var_lemma = optimize(post_sub_func, dec_vars[0])

    print('The solution for {} wrt variable {} is {}'.format(obj_func_list[0], dec_vars, solution_for_dec_variable_aka_new_var_lemma))
    return solution_for_dec_variable_aka_new_var_lemma

# Algo
# for game in game_tree:solve edge cases, get newvarlemma, use them to solve previous case
#traverse tree, store game data in tree nodes, traverse until you get to base
# traverse for back to front (one full branch) before moving onto other branches

cases = ['FTOrg', 'FTConv', 'NFTOrg', 'NFTConv']

''' In every problem there exists the same common elements:
    Endogenous variables
    Exogenous variables
    Decision function (util_function as f(endogvar, exogvar). players will maximixe this with certain endog variables
    Decision Maker - player who is optimizing their own utility in a given subgame
    Decision variable - endogenous variable to be maximized in a given subgame
    Decision - player sets some decision variable to an value that maximizes their util_function
'''

# If I could run one function that would analyze the who game, what would it take in and out
'''
In: all payoffs for all branches, functions in terms of what variables are available
function_in(*variables,

exog_variables = [k, q, a, s, w]
endog_variables = [Q, p]
decision_variable = p #the variable to be maximized in a given round

# To maximize utility with respect to the deicision variable
deriv = diff(util_function, decision_variable)
# Max is the value of the decision variable that gives the maximum utility
max = solve(deriv, decision_variable)

'''


class Tests(unittest.TestCase):
    # Test variables
    dec_var = Q
    obj_func = w * Q - a * Q + p * (Q ** 2)

    def test_optimize_objective_func(self, obj_func, dec_var):
        result = optimize_objective_func(obj_func, dec_var)
        # TODO figure out how to use an assert statement in the test to make sure the function works right
        # assert result is

    def test_get_exog_variables(*args):
        # Should create a list of variables and add a and b to list
        variables_list = get_exog_variables('a', 'b')
        assert variables_list is type(list)

        # Should prompt user to input variables, then display them back
        variables_list1 = get_exog_variables()
        assert variables_list1 is type(list)

    # TODO decide if I still need this later since its a duplicate of get_exog_variables
    def test_get_endog_variables(*args):
        # Should create a list of variables and add a and b to list
        variables_list = get_exog_variables('a', 'b')
        assert variables_list is type(list)

        # Should prompt user to input variables, then display them back
        variables_list1 = get_exog_variables()
        assert variables_list1 is type(list)

    def test_get_obj_func(self):
        # The case of 0 args, 2 kwargs with key1 = retailer_util and key2 = farmer_util
        get_obj_func(retailer_util=p - w, farmer_util=w - a)


def optimize_obj_func_solve_for_dec_var(obj_func, dec_var):
    ''' :returns expression for a variable
        Takes derivative of objecive function, sets it = 0, and tells you what
        the value of that expression is in terms of the decision variables


    '''

    deriv = diff(obj_func, dec_var)
    print('The derivative wrt {} of the ({}) function is '.format(dec_var, obj_func) + str(deriv))
    dec_var_maximizes_obj_func = solve(deriv)
    print('The function of {} that maximizes {} is '.format(dec_var, obj_func) + str(dec_var_maximizes_obj_func[0]))
    return dec_var_maximizes_obj_func


# The case of 0 args, 2 kwargs with key1 = retailer_util and key2 = farmer_util
#get_obj_func(retailer_util= p - w, farmer_util= w - a)
#get_obj_func(p-w)
#get_obj_func(p-w, a)