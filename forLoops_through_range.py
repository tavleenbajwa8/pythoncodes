#Looping through numerical range

values = range(1,10)
print(values)
print(type(values))

for i in range(1,11):
    print(i)

for num in range(5):
    print(num)
print("\n") 
for i in range(2,11,2):
    print(i)

word = "Hello World"
list_word = list(word)
print(word)
print(list_word)

list_word[5] = "NEW"
print(list_word) 

#To turn list back into a string

new_word = "".join(list_word)
print(new_word)

numbers = list(range(10, 101, 10))
print(numbers)

for number in numbers:
    print(number)

squares =  []
for num in numbers:
    square = num**2
    squares.append(square)

print("Populating squares complete!")
for square in squares:
    print (square)


#List comprehension

cubes = [num**3 for num in numbers]
for cube in cubes:
    print(cube)

#min(),max(),sum() functions
     
print(min(cubes))
print(max(cubes))
print(sum(cubes))
















    
     
