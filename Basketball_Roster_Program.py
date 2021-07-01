print("Welcome to the Basketball Roster Program")
rosters = []

#Taking the user input
p_guard = input("\nWho is your point guard: ")
rosters.append(p_guard.title())
s_guard = input("Who is your shooting guard: ")
rosters.append(s_guard.title())
s_forward = input("Who is your small forward: ")
rosters.append(s_forward.title())
p_forward = input("Who is your power forward: ")
rosters.append(p_forward.title())
center = input("Who is your Center: ")
rosters.append(center.title())

#Summary
print("\n")
print("\t\tYour starting " + str(len(rosters)) + " for the upcoming basketball season")
print("\t\t\tPoint guard: " + "\t\t" + str(rosters[0]))
print("\t\t\tShooting guard: " + "\t" + str(rosters[1]))
print("\t\t\tSmall forward: " + "\t\t" + str(rosters[2]))
print("\t\t\tPower forward: " + "\t\t" + str(rosters[3]))
print("\t\t\tCenter: " + "\t\t" + str(rosters[4]))

#Simulating roster
print("\nOh no " + str(rosters[2]) + " injured.")
removed_player = rosters.pop(2)
print("Your roster only has " + str(len(rosters)) + " players.")

#Taking user input
new_player = input("Who will take " + removed_player + "'s spot: ").title()
rosters.insert(2, new_player)

#Finalresult
print("Good luck " + str(rosters[2]) + " you will do great!")
print("Your roster now has " + str(len(rosters)) + " players.")
