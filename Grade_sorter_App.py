print("Welcome to the Grade Sorter App")

grades = []

grades.append(input("\nWhat is your first grade(0-100): "))
grades.append(input("What is your second grade(0-100): "))
grades.append(input("What is your third grade(0-100): "))
grades.append(input("What is your fourth grade(0-100): "))

print("\nYour grades are: " + str(grades))
print("Your grades from highest to lowest are: " + str(sorted(grades, reverse = True)))
print("\nThe lowest grades will now be dropped.")

new_grades = sorted(grades, reverse = True)

removed_grade1 = new_grades.pop(3)
removed_grade2 = new_grades.pop(2)

print("\nFirst dropped grade is: " + removed_grade1)
print("Second dropped grade is: " + removed_grade2)
print("\nYour remaining grades are: " + str(new_grades))

print("Nice work! Your highest grade is " + new_grades[0])
