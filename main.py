import sympy as sy

x = sy.symbols('x')

t1 = sy.simplify(sy.sin(x)**2 + sy.cos(x)**2)
print("sin(x)^2 + cos(x)^2 =", t1 )
t2 = sy.simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
print("(x^3 + x^2 - x-1)/(x^2+2x+1)=", t2 )
