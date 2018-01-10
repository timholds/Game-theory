# File to experiment with turning user keyboard input into sympy strings
from sympy import sympify, Eq, symbols, diff, solve
from sympy.parsing.sympy_parser import parse_expr

# Vars is a list of variables
#vars = []
x, y, z, p, Q, w = symbols("x y z p Q w")
#x, y, z  = symbols("x y z ")
#vars = symbols(vars)

#Eq(p, 1 - Q)
#p

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


#user_input = input('Enter a function')
#parse_expr(user_input
#print(Eq('q', '1 - p'))
#print(parse_expr('q = 1 - p'))
#main_func = 'pi = p*q - w*Q'
