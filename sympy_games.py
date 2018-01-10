# File to experiment with turning user keyboard input into sympy strings
from sympy import sympify, Eq, symbols, diff, solve
from sympy.parsing.sympy_parser import parse_expr

x, y, z, p, Q, w = symbols("x y z p Q w")

def solve_this(obj_func= p*Q - w*Q , decisionVar=Q, lemmaVariable=p, lemmaEq=1 - Q):

    obj_func_pre_sub = obj_func
    decVar = decisionVar
    lemmaVar = lemmaVariable
    lemma = lemmaEq

    obj_func_post_sub = obj_func_pre_sub.subs(lemmaVar, lemma)
    print('objective function post sub is {}'.format(obj_func_post_sub))
    deriv = diff(obj_func_post_sub, decVar)
    solution = solve(deriv, decVar)
    print('Solution for {} that makes d({})/d{} = 0 is Q = {}'.format(decVar, obj_func_post_sub, decVar, solution))

solve_this(obj_func=, decisionVar=, lemmmaVariable=, lemmaEq=)





# Vars is a list of variables
#vars = []
#x, y, z  = symbols("x y z ")
#vars = symbols(vars)

#Eq(p, 1 - Q)
#p
'''
pi_r = p*Q - w*Q
print('Objective function to optimize is {}'.format(pi_r))
#varLemma = Eq(p, 1 - Q)
#print('Variable lemma is {}'.format(varLemma))
expr1 = pi_r.subs(p, 1-Q)
print('Expression after substituting {} for {} is {}'.format(1-Q, p, expr1))
deriv = diff(expr1, Q)
print('Derivative of {} with respect to {} is {}'.format(expr1, Q, deriv))
solution = solve(deriv, Q)
print('Solution for {} that makes deriv = 0 is Q = {}'.format(Q, solution))

'''

#user_input = input('Enter a function')
#parse_expr(user_input
#print(Eq('q', '1 - p'))
#print(parse_expr('q = 1 - p'))
#main_func = 'pi = p*q - w*Q'
