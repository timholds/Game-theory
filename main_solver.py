from sympy import *
import unittest

Q = Symbol('Q')
p = Symbol('p')
k = Symbol('k')
q = Symbol('q')
a = Symbol('a')
s = Symbol('s')
w = Symbol('w')

# Get the exogenous variables from the user and make symbols for each
def make_symbols_for_variables(*args):
    for arg in args:
        arg = Symbol(arg)
        print(arg)
        return arg


def get_endog_variables(*args):

    if args is None:
        variables = input('Please enter your exogenous variables, as lowercase letters')
    else:
        variables = []
        for arg in args:
            variables.append(args)
    print('Variables are {}'.format([var for var in variables]))

    return variables

def get_exog_variables(*args):

    if args is None:
        variables = input('Please enter your exogenous vaiables, as lowercase letters')
    else:
        variables = []
        for arg in args:
            variables.append(args)
    print('Variables are {}'.format([var for var in variables]))

    return variables


def run_all():
    #make_symbols_for_variables('k', 'q', 'a', 's', 'w')
    endog_variables = get_endog_variables()
    exog_variables = get_exog_variables()
    make_symbols_for_variables(endog_variables, exog_variables)


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

def optimize_objective_func(obj_func, dec_var):
    deriv = diff(obj_func, dec_var)
    print('The derivative wrt {} of the ({}) function is '.format(dec_var, obj_func) + str(deriv))
    dec_var_maximizes_obj_func = solve(deriv)
    print('The value of {} that maximizes {} is '.format(dec_var, obj_func) + str(dec_var_maximizes_obj_func[0]))
    return dec_var_maximizes_obj_func

class Tests(unittest.TestCase):
    # Test variables
    dec_var = Q
    obj_func = w * Q - a * Q + p * (Q ** 2)

    def test_optimize_objective_func(self, obj_func, dec_var):
        result = optimize_objective_func(obj_func, dec_var)
        # TODO figure out how to use an assert statement in the test to make sure the function works right
        #assert result is

    def test_get_exog_variables(*args):
        # Should create a list of variables and add a and b to list
        variables_list = get_exog_variables('a', 'b')
        assert variables_list is type(list)

        # Should prompt user to input variables, then display them back
        variables_list1 = get_exog_variables()
        assert variables_list1 is type(list)