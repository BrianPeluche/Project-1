

print("\nWelcome to XXX bgarc208/hwheeler 8 puzzle solver. Type “1” \nto use a default puzzle, or “2” to enter your own puzzle.\n")

user_input = int(input("Please enter a number: "))
    
while user_input != 1 and user_input != 2 :
    print("Incorrect. ")
    user_input = int(input("Please enter a number: "))

print("Enter your puzzle, use a zero to represent the blank")
row_one = list(map(int, input("Enter the first row, use space or tabs between numbers  ").split()))
row_two = list(map(int, input("Enter the second row, use space or tabs between numbers  ").split()))
row_three = list(map(int, input("Enter the third row, use space or tabs between numbers  ").split()))

print(row_one)
print(row_two)
print(row_three)
print("\nEnter your choice of algorithm")
print("\n1) Uniform Cost Search\n2) A* with the Misplaced Tile heuristic.\n3) A* with the Euclidean distance heuristic.\n")
