print("Welcome to the Factorial Calculator App")
import math
x = int(input("What number would you like to compute the factorial of?: "))
print(str(x) + "! = " , end="")
for i in range(1, x):
    print(str(i) , end="*")
print(str(x))

fact = math.factorial(x)
print("\n\nYour answer using math library is: ", end="")
print(str(fact) + "!")

fact = 1
print("\n\nYour answer using my own algorithm is: ", end="")
for i in range(1, x+1):
    fact = fact*i
print(str(fact) + "!")
    

  
    
        
