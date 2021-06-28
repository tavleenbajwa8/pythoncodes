#String Formatting methods


name = "Penny"
age = 24
money = 9.85

#print using string concatenation
print(name + " is " + str(age) + " and has $" + str(money) + " dollars.")

#print using the .format method for strings
print("{0} is {1} and has ${2} dollars.".format(name, age, money))

#print using f-strings
print(f"{name} is {age} and has ${money} dollars.")

