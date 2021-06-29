#Data types: Strings(Series of characters), Integers(Whole numbers), Floats(Decimal numbers), Lists(MUTABLE COLLECTION), TUPLES(IMMUTABLE COLLECTION).
#Built-in functions: print(), type(), str(), int(), float(), input(), round(), sorted(), len().
#Methods in lists: .append(), .insert(), .pop(), .remove(), .sort(), reverse().
#Mehods in strings: .upper(), .lower(), .title(), .strip(), .count()
#External libraries: math, datetime
#Challenge Problems: Grade Sorter App, Different types of lists program, Grocery list app, Basketball roster program, favourite teachers program


#An introduction to list: [1, 2, 3, 4]

#Lists of strings

topics = ["Physics", "Computer science", "Art", "Maths"]
print(topics)
print(type(topics))

topics_2 = ["Maths", "Art", "Computer science", "Physics"]
print(topics_2)

#indexing

print(topics[0])
print(topics_2[0])

print(topics[3])
print(type(topics[3]))

#Negative elements start reading lists from end [-1 = last element of list], [-2 = second last element of list]


print(topics[-1])
print(topics_2[-2])

print("My favourite area of study is " + topics[1].upper() + " !")


