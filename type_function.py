#3 variables
#Casting helps in changing one datatype to another: str(), int(), float()


name = "john"
fav_num = 13
tax_rate = 0.4

print(type(name))
print(type(fav_num))
print(type(tax_rate))

tax_rate = str(tax_rate)
print(type(tax_rate))

print(name.title() + "'s favourite number is " + str(fav_num) + ".")

#we can only concatenate strings, not integers

print(name.title(), "'s favourite number is", fav_num, ".")


#arithmatic

added_value = fav_num + 5 
print(added_value)
 
