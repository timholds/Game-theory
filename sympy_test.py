from sympy.solvers import solve
from sympy import Symbol, diff
from sympy import *
from optlang import Model, Variable, Constraint, Objective


# solution = solve(function, variable)
# Solve finds the value of the variable that makes the derivative of the function = 0)

x = Symbol('x')
sol = solve(x**2 - 1, x)
print(sol)

Q = Symbol('Q')
p = Symbol('p')
k = Symbol('k')
q = Symbol('q')
a = Symbol('a')
s = Symbol('s')
w = Symbol('w')

soln2 = solve(k + q - p + a * s, p)
soln = solve(Q**3 - 1, Q)
print(soln2)

Q = k + q - p + (a*s)

def soln(wrtvariable=None):
    # Need to have all the exog variables here
    # should be help by some data thing somewhere and give by user
    pi_r = p*Q - w*Q
    pi_r_wrt_Q = pi_r.subs(p, Q)
    var = wrtvariable
    print('Retailer profit in terms of' + '{}'.format(var) + 'is: ' + str(pi_r_wrt_Q))
    deriv = diff(pi_r_wrt_Q, p)
    max = solve(deriv)
    print(max)
    return max

soln(p)
# Get the computer to take the symbolic derivative

# Solve for the derivative to find the max
#sol = solve(deriv, x)


