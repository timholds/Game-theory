# File to experiment with turning user keyboard input into sympy strings
from sympy import symbols, diff, solve, Piecewise, Eq
from sympy.abc import *

f, g, P, Q, Qbar, Qstar, Qhat = symbols("f g P Q Qbar Qstar Qhat")
b, x, q, y, z, w, wg, k, al, s = symbols("b, x q y z w wg k al s")

# Note lemmEq is = to the out_var here, so Q = k - P + q + al*s
# TODO at some point we should add a function to solve lemmaEq in terms of out_var automatically
# so one could enter P = f(Q, exog) and it would solve to Q = f(P, exog) if W was out_var

def solve_this(obj_func= P*Q - w*Q - wg*Q, dec_var=P,  out_var=Q, lemmaEq= k - P + q + al*s):

    obj_func_pre_sub = obj_func
    dec_var = dec_var
    out_var = out_var
    lemma = lemmaEq

    obj_func_post_sub = obj_func_pre_sub.subs(out_var, lemma)
    print('objective function (post sub) is {}'.format(obj_func_post_sub))


    deriv = diff(obj_func_post_sub, dec_var)
    #print('Deriv: {}'.format(deriv))

    solution = solve(deriv, dec_var)
    print('When d(obj_func)/d{} = 0, the solution {}* = {}'.format(dec_var, dec_var, solution))

    #print('solution is {}'.format(solution))
    # Evaluate the lemma when the decision variable is maximized
    #print('the starting lemma function is {} '.format(lemma))
    if solution is type(list):
        solution = solution[0]
    #print('solution  is {}'.format(solution))
    lemma_plugged = lemma.subs(dec_var, solution)
    print('The lemma func {}={} evaluated at {}*={} is {}({}*)={}'.format(out_var, lemma, dec_var, solution, out_var, dec_var, lemma_plugged))

    #print()
    return dec_var, solution, lemma_plugged

# Solve for fair trade conventional
#if 'case' == '1':
pi_r = P*Q - w*Q
pi_f = w*Q - a*Q
decision_var = P
outvar = Q
lems = k - P + s

# lems needs to be a sympy expression so we can call subs later

# Retailer optimizes profit by choosing p
print('Solving Game 4')
FTC_g4 = solve_this(obj_func = pi_r, dec_var=decision_var, out_var=outvar, lemmaEq=lems)
print('Solution from Fait Trade Conventional Game 4 was {}*={}'.format(decision_var, FTC_g4[1]))
print()
print('Solving Game 3')
print('FTC_g4[1][0] is P={}'.format(FTC_g4[1][0]))
FTC_g3 = solve_this(obj_func = pi_f, dec_var=Q, out_var= P, lemmaEq= FTC_g4[1][0])

# Define the farmers profit function as a sympy piacewise expression
# so we can call it as main_func in substitute(main_func, oldvar, varlemma)
# since in main_func.subs main_func must be an expression

# What is the piecewise for the farmers profit function
# If farmer makes less than Qbar, he sells all his stuff
f =  w * Qhat - a * Qhat
# If farmers makes more than Qbar, he has leftover he pays for
g = w * Qbar - a * Qhat
#p = Piecewise((f, Qhat < Qbar), (g, Qhat >= Qbar))

# Split into 2 cases because
# Case one is when Qhat < Qbar, case2 when Qhat >= Qbar
#pi_f = w*Q + wg*Q - a*q - b*Q*Q

# Function from f(Q, P) to p = f(Q)
#b1g4 = solve_this()
#print(b1g4)
# Fumction from f(
#b1g3 = solve_this(obj_func=pi_f, dec_var=Q, out_var=P, lemmaEq=b1g4[1])
#print(b1g3)
#solve_this(obj_func=, decisionVar=, lemmmaVariable=, lemmaEq=)

# how to use lemma at the end to finish substitution loop
# for example if i sub





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
