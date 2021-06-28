print("\nWelcome to the Temperature converter App!")

celcius = float(input("\nWhat is your temperature in celcius?: "))
kelvin = celcius*float(1.8)
kelvin = float(kelvin + 32) 
kelvin = round(kelvin, 1)
farenheit = float(kelvin - 459.67)
farenheit = round(farenheit, 1)

print("\nYour temperature in celcius is: " + str(celcius) + " " + "C.")
print("\nYour temperature in kelvin is: " + str(kelvin) + " " + "K.")
print("\nYour temperature in farenheit is: " + str(farenheit) + " " + "F.")

print("\nThanks for using the Temperature converter App!")
