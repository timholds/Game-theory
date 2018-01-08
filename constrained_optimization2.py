from optlang import Variable, Constraint, Objective, Model

# Define problem parameters
# Note this can be done using any of Python's data types. Here we have chosen dictionaries
supply = {"Seattle": 350, "San_Diego": 600}
demand = {"New_York": 325, "Chicago": 300, "Topeka": 275}

distances = {  # Distances between locations in thousands of miles
    "Seattle": {"New_York": 2.5, "Chicago": 1.7, "Topeka": 1.8},
    "San_Diego": {"New_York": 2.5, "Chicago": 1.8, "Topeka": 1.4}
}

freight_cost = 9  # Cost per case per thousand miles

# Define variables
variables = {}
for origin in supply:
    variables[origin] = {}
    for destination in demand:
        # Construct a variable with a name, bounds and type
        var = Variable(name="{}_to_{}".format(origin, destination), lb=0, type="integer")
        variables[origin][destination] = var

# Define constraints
constraints = []
for origin in supply:
    const = Constraint(
        sum(variables[origin].values()),
        ub=supply[origin],
        name="{}_supply".format(origin)
    )
    constraints.append(const)
for destination in demand:
    const = Constraint(
        sum(row[destination] for row in variables.values()),
        lb=demand[destination],
        name="{}_demand".format(destination)
    )
    constraints.append(const)

# Define the objective
obj = Objective(
    sum(freight_cost * distances[ori][dest] * variables[ori][dest] for ori in supply for dest in demand),
    direction="min"
)
# We can print the objective and constraints
print(obj)
print("")
for const in constraints:
    print(const)

print("")

# Put everything together in a Model
model = Model()
model.add(constraints)  # Variables are added implicitly
model.objective = obj

# Optimize and print the solution
status = model.optimize()
print("Status:", status)
print("Objective value:", model.objective.value)
print("")
for var in model.variables:
    print(var.name, ":", var.primal)