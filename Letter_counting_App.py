print("Welcome to the Letter Counter App!")

name = input("What's your name?: ").title().strip()
print("Hello " + name + "!" + " I'll count the number of occurences of a specific letter for you in the message")

message = input("\nType your message here: ")
letter = input("\nWhich letter you want to count the occurences for?: ")
message = message.lower()
letter = letter.lower()

letter_count = message.count(letter)
print("Dear " + name + "!" + " Your message has " + str(letter_count) + " " + letter + "'s in it.")

print("\nThanks for using the Letter counting App, " + name + "!") 

