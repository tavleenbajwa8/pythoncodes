print("Welcome to the Binary/Hexadecimal Converter App")

x = int(input(" Compute Binary and Hexadecimal values up to the following decimal number: "))
decimal = list(range(1, x+1))
binary = []
hexadecimal = []
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Generating lists..complete!")

#Get slicing index from user
print("Using Slices, we will now show a portion of each list")
y = int(input("What decimal would you like to start at: "))
z = int(input("What decimal would you like to stop at: "))

print("\nDecimal values from " + str(y) + " to " + str(z) + ":") 
for num in decimal[y-1:z]:
    print(num)
print("\nBinary values from " + str(y) + " to " + str(z) + ":") 
for num in binary[y-1:z]:
    print(num)
print("\nHexadecimal values from " + str(y) + " to " + str(z) + ":") 
for num in hexadecimal[y-1: z]:
    print(num)
    
#Output the whole list to the screen
input("\nPress enter to see all values from 1 to " + str(x) + ".")
print("Decimal----Binary----Hexadecimal")
print("---------------------------------")
for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d) + "----" + str(b) + "----" + str(h))
      



