#from sympy import *
from sympy import *
import unittest

Q = symbol('Q')
p = symbol('p')
k = symbol('k')
q = symbol('q')
a = symbol('a')
s = symbol('s')
w = symbol('w')

### ------ Input Functions
def get_endog_variables(*args):
    '''Get exog variables through arguments or user input if no args'''

    var_list = []
    if not args:
        input_variables = input('Please enter your endogenous variables, as lowercase letters')
        variables_one_string = ''.join([var for var in input_variables])
        variables = variables_one_string.split(', ')

    else:
        print('I was given arguments, and I shall use them!')
        variables = []
        for arg in args:
            variables.append(args)

    print('Endogenous Variables are {}'.format(variables))
    return variables

def get_exog_variables(*args):
    ''' Get exog variables through arguments or user input if no args'''

    if not args:
        input_variables = input('Please enter your exogenous vaiables, as lowercase letters')
        variables_one_string = ''.join([var for var in input_variables])
        variables = variables_one_string.split(', ')
        print(type(variables))

    else:
        variables = []
        for arg in args:
            variables.append(args)

    print('Exogenous Variables are {}'.format(variables))
    return variables

def get_decision_variables(*args):
    ''' Returns a list of decision variables'''

    decision_vars = []

    if not args:

        input_variables = input('What decision variable do you want to use for this round?')
        variables_one_string = ''.join([var for var in input_variables])
        variables = variables_one_string.split(', ')

        for item in variables:
            try:
                decision_vars.append(item)
            except Exception as e:
                print(e)
                print('Problem with the input and appending to a list.')
    else:
        for arg in args:
            decision_vars.append(arg)

    print('Decision variables(s) for this round are: {}'.format(str(decision_vars)))
    return decision_vars

def get_funcs():
    ''' Get objective and lemma functions
    A version of get_objective_func and get_lemma_func that is way shorter and takes no funcs in args'''
    user_input = input('Enter all functions you want, including lemma functions')
    variables_one_string = ''.join([var for var in user_input])
    funcs = variables_one_string.split(', ')
    return funcs

def get_objective_func(*args, **kwargs):
    ''' Get the objective function through arguments or by user input if no args
    :param args: like P*Q - 1
    :param kwargs: like tim_util = P*Q - 1
    :return: objective function as an equation (symbols)
    :rtype: equation representing a function (y = m*x**2 + b)'''

    obj_func_list = []
    obj_func_dict = {}

    if not args:
        # Passed neither args nor kwargs
        if not kwargs:
            input_variables = input('Enter one or more obj functions as args or kwargs')# Get functions through the user keyboard as items or k,v pairs
            variables_one_string = ''.join([var for var in input_variables])
            variables = variables_one_string.split(', ')
            for item in variables:
                obj_func_list.append(item)

        # Passed only kwargs
        else:
            for key, value in kwargs.items():
                print("The value of {} is {}".format(key, value))
                # Put the keys and values into a dictionary
                obj_func_dict[key] = value
                # Put the dict inside the list of obj functions
                obj_func_list.append(obj_func_dict.copy())

    else:
        # Passed only args
        if not kwargs:
            for arg in args:
                obj_func_list.append(args)

        # Passed both args and kwargs
        else:
            for arg in args:
                obj_func_list.append(args)
            for key, value in kwargs.items():
                # Put the keys and values into a dictionary
                obj_func_dict[key] = value
                # Put the dict inside the list of obj functions
                obj_func_list.append(obj_func_dict.copy())

    print('Functions are are {}'.format([func for func in obj_func_list]))

    return obj_func_list

def get_lemma_func(*args, **kwargs):
        ''' Get the lemma function through arguments or by user input if no args
        :param args: like P*Q - 1
        :param kwargs: like tim_util = P*Q - 1
        :return: objective function as an equation (symbols)
        :rtype: equation representing a function (y = m*x**2 + b)'''

        lemma_func_list = []
        lemma_func_dict = {}

        if not args:
            # Passed neither args nor kwargs
            if kwargs is None:
                user_input = input('Enter one or more obj functions as args or kwargs')  # Get functions through the user keyboard as items or k,v pairs
                variables_one_string = ''.join([var for var in user_input])
                funcs = variables_one_string.split(', ')
                for item in funcs:
                    lemma_func_list.append(item)

            # Passed only kwargs
            elif kwargs is not None:
                for key, value in kwargs.items():
                    print("The value of {} is {}".format(key, value))
                    # Put the keys and values into a dictionary
                    lemma_func_dict[key] = value
                    # Put the dict inside the list of obj functions
                    lemma_func_list.append(lemma_func_dict.copy())

        else:
            # Passed only args
            if kwargs is None:
                for arg in args:
                    lemma_func_list.append(args)

            # Passed both args and kwargs
            elif kwargs is not None:
                for arg in args:
                    lemma_func_list.append(args)
                for key, value in kwargs.items():
                    # Put the keys and values into a dictionary
                    lemma_func_dict[key] = value
                    # Put the dict inside the list of obj functions
                    lemma_func_list.append(lemma_func_dict.copy())

        print('Functions are are {}'.format([func for func in lemma_func_list]))

        return lemma_func_list

### ------- Calculation functions
def make_symbols_for_variables(*args):
   '''
    :description:  Make symbols for sympy to manipulate based in user inputs
    :param accepts strings separated by comma and no space.
    # TODO make this accept strings separated by comma and space also '''
   for arg in args:
        for item in arg:
            for thing in item:
                print(type(thing))
                #expr =
                #thing1 = expr(thing)
                arg = symbols(thing)
                print(thing)
                return thing
            x = Symbol('x')


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
        :param main_func must be a sympy expression
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

class Tests(unittest.TestCase):
    # Test variables
    dec_var = Q
    obj_func = w * Q - a * Q + p * (Q ** 2)

    def test_optimize_objective_func(self, obj_func, dec_var):
        result = optimize(obj_func, dec_var)
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

    def test_get_objective_func(self):
        # The case of 0 args, 2 kwargs with key1 = retailer_util and key2 = farmer_util
        get_objective_func(retailer_util=p - w, farmer_util=w - a)

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

#####Old code replace in get_obj_func
   if args is None:
        obj_func_list = input('Please enter your exogenous variables, as lowercase letters')
    else:
        # How to handle being passed multiple objective functions?
        obj_func_list = []
        for arg in args:
            print('adding {} to list or dict of objective functions'.format(str(arg)))
            obj_func_list.append(arg)

    if kwargs is None:
    obj_func_dict = {}
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
        obj_func_dict[key] = value

'''




def optimize_objective_func_solve_for_dec_var(obj_func, dec_var):
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