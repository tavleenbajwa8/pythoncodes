print("\t\t\tSummary Table")


num_strings = ["15", "100", "55", "42"]
print("\nThe variable num_strings is a " + str(type(num_strings)))
print("It contains the elements: " + str(num_strings))
print("The element 15 is " + str(type(num_strings[0])))


num_ints = [15, 100, 55, 42]
print("\nThe variable num_ints is a " + str(type(num_ints)))
print("It contains the elements: " + str(num_ints))
print("The element 15 is " + str(type(num_ints[0])))


num_floats = [2.2, 5.0, 1.245, 0.142857]
print("\nThe variable num_floats is a " + str(type(num_floats)))
print("It contains the elements: " + str(num_floats))
print("The element 2.2 is " + str(type(num_floats[0])))


num_lists = [[1,2,3], [4,5,6], [7,8,9]]
print("\nThe variable num_lists is a " + str(type(num_lists)))
print("It contains the elements: " + str(num_lists))
print("The element [1, 2, 3] is " + str(type(num_lists[0])))


#Temporary sorting
print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: " + str(sorted(num_strings)))
print("Sorted num_ints: " + str(sorted(num_ints)))


#Permanent sorting
num_strings.sort()
num_ints.sort()

print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: " + str(num_strings))
print("Sorted num_ints: " + str(num_ints))

print("\nThe strings are sorted alphabetically while integers are sorted numerically.")
