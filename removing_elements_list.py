#removing elements from a list

#.remove() method: Helpful when you know the name of the element in a string.

colors = ["red", "blue", "yellow", "blue"]
print(colors)
colors.remove("yellow")
print(colors)

colors.remove("blue")
print(colors)
colors.remove("blue")
print(colors)

#Another method is .pop(): Helpful when you know the index of the element in a string.

new_colors = ["red", "green", "brown", "orange"]
removed_color = new_colors.pop()
print("Removing the color " + removed_color)

bad_color = new_colors.pop(1)
print("A bad color is " + bad_color)

#del

print(colors)
del colors[0]
print(colors)

fruits = []
fruits.append(input("Enter a fruit: "))
fruits.append(input("Enter a fruit: "))
fruits.append(input("Enter a fruit: "))
print(fruits)


