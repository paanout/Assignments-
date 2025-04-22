import math  # I'm using the math module for sin, cos, and exp since I can't use numpy

# This is my Newton-Raphson function
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0  # starting point
    for i in range(max_iter):
        fx = f(x)       # value of function at current x
        dfx = df(x)     # value of derivative at current x

        if dfx == 0:
            # I added this to avoid dividing by zero
            raise ZeroDivisionError("Derivative is zero. No solution found.")
        
        # Newton-Raphson formula
        x_new = x - fx / dfx

        # checking if the result is close enough to stop
        if abs(x_new - x) < tol:
            return x_new

        x = x_new  # update x and try again

    # if we reach here, the loop didn't converge
    raise Exception("Max iterations exceeded. No solution found.")

# Now defining the function f(x) = 4x + sin(x) - exp(x)
def f(x):
    return 4*x + math.sin(x) - math.exp(x)

# Derivative of the function: f'(x) = 4 + cos(x) - exp(x)
def df(x):
    return 4 + math.cos(x) - math.exp(x)

# I'm starting with an initial guess
x0 = 0.5

# Now I call the Newton-Raphson method
root = newton_raphson(f, df, x0)

# Printing the result
print("Root of 4x + sin(x) - exp(x) = 0 is approximately:", root)
