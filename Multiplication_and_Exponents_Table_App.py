print("Welcome to the Multiplication and Exponents Table App")

name = input("Enter your name: ").title().strip()
print("Hello " + name + "!")
num = float(input("Enter the number: "))
message = name + ", Math is cool!"


print("\n\tMultiplication table of " + str(num))

for i in range(1, 9):
    print(str(num) + " x " + str(i) + " = " + str(num*i))

print("\n\tExponents table of " + str(num))

for i in range(1, 9):
    print(str(num) + " x " + str(i) + " = " + str(num**i))



print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.lower())
print("\t\t\t" + message.lower())
             
