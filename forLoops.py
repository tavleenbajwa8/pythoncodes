#Looping through a list of elements with a "For loop"

teams = ["giants", "bills", "jets", "patriots"]

print(teams)
print(type(teams))

# if we type: print(teams.title()), then we may get an error because title() methods is for string objects only, not list
# to overcome that we can use list indexing

print(teams[0].title())
print(teams[1].title())
print(teams[2].title())
print(teams[3].title())

#Copypasting is tedious and make the code very lengthy to which "for loop" comes to the rescue.

for i in teams:
    print(i.title())
    print("You're going to win the Super Bowl!\n")

print("Go Football!!!")

values = [1, 2, 3, 4, 5]
total_sum = 5
for value in values:
    total_sum += value
print(total_sum)

triples = [["a", "b", "c"], ["1", "2", "3"], ["do", "re", "mi"]]

for list_value in triples:
    print(list_value)
     
for list_value in triples:   
    for element in list_value:
        print(element, end=' ')


for list_value in triples:   
    for element in list_value:
        print(element, end=' ')
    print("I just finished one of the inner loops!")
print("Now I'm outside both for loops!")










        
