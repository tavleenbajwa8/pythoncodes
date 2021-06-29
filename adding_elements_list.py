#changing or adding elements to a list

colors = ["red", "orange", "green"]
print(colors)
print(colors[2])
print(colors[-1])

#to alter the main list
colors[2] = "yellow"
print(colors)

#to expand the list we use .append()

colors.append("blue")
print(colors)

new_colors = []
new_colors.append("red")
new_colors.append("pink")
new_colors.append("purple")
print(new_colors)

#to add an element at a specified index

new_colors.insert(1, "brown")
print(new_colors[1]) 
print(new_colors)

new_colors.insert(3, "blue")
print(new_colors)
