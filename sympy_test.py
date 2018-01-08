from sympy.solvers import solve
from sympy import Symbol, diff
from sympy import *
from optlang import Model, Variable, Constraint, Objective



# solution = solve(function, variable)
# Solve finds the value of the variable that makes the derivative of the function = 0)

x = Symbol('x')
sol = solve(x**2 - 1, x)
#print(sol)

Q = Symbol('Q')
p = Symbol('p')
k = Symbol('k')
q = Symbol('q')
a = Symbol('a')
s = Symbol('s')
w = Symbol('w')

def substitute_utility(case, player_utility, oldvar, newvar, *mainfunc, extrafunc):
    ''' A substitution machine'''

    func = player_utility
    # Substitute the new variable equation into the old variable one
    func_post_sub = func.subs(oldvar, extrafunc)
    print('yo')
    print('{} profit is : '.format(player_utility.__name__) + str(func_post_sub))
    #print('Retailer profit in terms of {} (where {} substituted out)'.format(newvar, oldvar) + 'is: ' + str(func_post_sub))

    return func_post_sub

def substitute_functions(opfunc, lemmafunc, invar, outvar):
    ''' Use with:
    One function you wan to optimize later (oldvec) is the variable
        util = 1 + p + Q**2
    One function in terms of the variable you want to sub:
        Q = 1 - p
    :returns
    '''
    pre_sub_func = opfunc
    post_substitution_func = pre_sub_func.subs(outvar, invar)
    return post_substitution_func


# a soln should inherit w from its game
# a soln maps multiple eq with mult variables into less eq with less variables
# Already copied this to game.py and put it in player class i think and renamed
def soln(oldvar, newvar, case='FTOrg'):
    ''' A solver for a single backwards induction game'''

    # Q = consumer_demand_function(case) # Q = k + q - p + (a * s)
    Q = k + q - p + (a * s)

    # TODO make retailer_profit_function(case) that returns p*Q - w*Q
    #r_profit = retailer_profit_function(case) #p*Q - w*Q
    r_profit = p*Q - w*Q
    #print('Retailer profit is: ' + str(r_profit))

    # Substitute old variables in for new one in the profit equation
    r_profit_sub = r_profit.subs(oldvar, newvar)
    #print('Retailer profit in terms of {} (where {} substituted out)'.format(newvar, oldvar) + 'is: ' + str(r_profit_sub))

    deriv = diff(r_profit_sub, newvar)
    print('In terms of {}, derivative of Retailer profit: '.format(newvar) + str(deriv))

    max = solve(deriv, newvar)
    print('Max retail profit occurs when {} = '.format(newvar) + 'is: ' + str(max[0]))
    return max

soln(Q, p)

# Get the computer to take the symbolic derivative

# Solve for the derivative to find the max
#sol = solve(deriv, x)

#soln2 = solve(k + q - p + a * s, p)
#soln = solve(Q**3 - 1, Q)
#print(soln2)

