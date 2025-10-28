

print("\nWelcome to XXX bgarc208/hwheeler 8 puzzle solver. Type “1” \nto use a default puzzle, or “2” to enter your own puzzle.\n")

user_input = int(input("Please enter a number: "))
    
while user_input != 1 and user_input != 2 :
    print("Incorrect. ")
    user_input = int(input("Please enter a number: "))