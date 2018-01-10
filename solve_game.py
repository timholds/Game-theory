# Tim Holdsworth and University of San Diego Decision Sciences
# This code is intended to run a series of prewritten functions to 'solve' a single round of a game theory game
import sys
from sympy import *
from solver_functions import get_endog_variables, get_exog_variables, get_decision_variables, get_objective_func, get_lemma_func, make_symbols_for_variables, optimize, substitute_functions, solve_one_game

def make_symbols(*args):
    # Make a list to store the symbols
    symbols = []
    for item in args:
        for arg in item:
            symbols.append(Symbol(arg))
    return symbols

#Make symbols(main_func has to be of type expression in sympy rather than as a string)

def solve():

    endog_variables = get_endog_variables()
    exog_variables = get_exog_variables()
    dec_vars = get_decision_variables()  # Variables you want to have out aka solved aka ready to substitute in the nxt round
    lemma_var = ['Q']
    vars = dec_vars + exog_variables + endog_variables + lemma_var

    print('Calling make symbols')
    symbols = make_symbols(vars)
    sympy.parsing.sympy_parser.parse_expr(symbols)

    obj_func_list = get_objective_func()
    print(obj_func_list[0])
    # Parse objective function for left, = and right side fo eq
    # for functions in obj_func_list:
    #var = left
    #var_lemma = right
    # main_func must be simpy('ed) and Eq(x, y) or
    # Eq(var, varlemma)

    # Need to make one of these equations a sympy expression
    #util_func = obj_func_list[0]
    print('FunctionType is {}'.format(type(obj_func_list[0])))

    parse_expr(obj_func_list[0])
    #expre = f(sympy symbols)
    #main_func = sympify(util_func)

    p = Symbol('p')
    side_eq = 1 ** p

    print('objective func and dec vars are {} {}'.format(obj_func_list[0], dec_vars[0])

    # substitute
    # Object_func_list needs to be an expr or sympy object that can do subs(oldvar, newlemma)
    post_sub_func = substitute_functions(obj_func_list[0], dec_vars[0], side_eq)
    print("shoulf print")
    print(p)
    # optimize
    solution = optimize(post_sub_func, dec_vars[0])

    print('The solution for {} wrt variable {} is {}'.format(obj_func_list[0], dec_vars, solution))
    return solution

#sympy - sub(main_func, oldvar, lemma)
#   sub is expr.subs(oldvar, newvar) or expr.subs(oldvar, newlemma/newexpr)

if __name__ == '__main__':
    #pass
    solve()

#make_symbols_for_variables('a b')
#make_symbols_for_variables('a', 'b')



# Get command line arguments to function arguments.
#make_symbols_for_variables(*sys.argv[1:])

#get_objective_func()