print("Welcome to the Grocery Store App")
import datetime
x = datetime.datetime.now()
print("Current date and time is " + x.strftime("%d") + "/" + x.strftime("%m") + " " + x.strftime("%H") + ":" + x.strftime("%M"))

current_list = ["Meat", "Cheese"]

print("You currently have Meat and Cheese in your list.")

current_list.append(input("Type the food item to add in the grocery list: "))
current_list.append(input("Type the food item to add in the grocery list: "))
current_list.append(input("Type the food item to add in the grocery list: "))

print("Here is your grocery list: ")
print(current_list)

print("Here is your sorted grocery list: ")
print(sorted((current_list)))

print("Simulating grocery shopping..")

print("\nCurrent grocery list has " + str(len(current_list)) + " items.")
print(current_list)
current_list.remove(input("\nWhat food did you buy: "))
print(current_list)

print("\nCurrent grocery list has " + str(len(current_list)) + " items.")
print(current_list)
current_list.remove(input("\nWhat food did you buy: "))
print(current_list)

print("\nCurrent grocery list has " + str(len(current_list)) + " items.")
print(current_list)
current_list.remove(input("\nWhat food did you buy: "))
print(current_list)

print("Sorry, the store is out of " + current_list[1])

del current_list[1]
print(current_list)

current_list.append(input("\nWhat food would you like instead: "))

print(current_list)



                 
