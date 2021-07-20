print("Welcome to Quadratic solver App")
print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is a real number and bj is an imaginary portion")

import cmath

x = input("\n\tHow many equations would you like to solve today?: ")
for i in range(int(x)):
    print("\nSolving equation #" + str(i + 1))
    a = float(input("\nPlease enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
   
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
    print("The solutions to " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 are:")    
    print("\n\tx1 = " + str(x1))
    print("\tx2 = " + str(x2))
    print("-------------------------------")
print("\n\nThankyou for using the Quadratic Solver App!")
