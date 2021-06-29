#Lists can be sorted either Temporarily or permanently

#sorted(list, reverse = True) (If we want to sort the list in reverse order)

#Sorting list of string elements

sports = ["baseball", "golf", "soccer", "football"]
print(sports)
print(sorted(sports))
print(sorted(sports, reverse = True))
print(sports)

#Sorting list of integer elements

marks = [44, 36, 98, 7]
print(marks)
print(sorted(marks))
print(sorted(marks, reverse = True))
print(marks)

#len() function

marks_length = len(marks)
print(marks_length)
print(type(marks_length))

removed_marks = marks.pop()
print("Removing grade " + str(removed_marks))
print(len(marks))

#Permanent sorting: .sort(), .reverse() methods

print(sports)
sports.sort()
print(sports)

 print(sports)
sports.sort(reverse = True)
print(sports)


print(marks)
marks.sort()
print(marks)

print(marks)
marks.sort(reverse = True)
print(marks)

print(sports)
sports.reverse()
print(sports)


#Keep the notations consistent while sorting lists, all elements shall be lowercase or uppercase. 


















