#Tuples are immutable, uses parenthesis()

marks = [100, 55, 44]
score = (100, 55, 44)

print(marks)
print(score)

print(type(marks))
print(type(score))

marks.append(33)
print(marks)

#If we try changing the tuple, we get, "Attribute Error: 'tuple' object has no attribute 'append'." like score.append(); score.pop()

#Only way we can change a tuple is overwriting or totally redefining it. 

score = (99, 66, 55)
print(score)
