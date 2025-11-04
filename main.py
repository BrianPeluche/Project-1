#main.py
from algorithm.heuristic import a_star, uniform_cost, count, euclidean
from puzzle.puzzleNode import PuzzleNode
def main():

    print("\nWelcome to bgarc208/hwhee004 8 puzzle solver. Type '1' \nto use a default puzzle, or '2' to enter your own puzzle.\n")

    user_input = int(input("Please enter a number: "))
        
    while user_input != 1 and user_input != 2 :
        print("Incorrect. ")
        user_input = int(input("Please enter a number: "))
    if user_input == 1:
        initial = (1, 2, 3, 4, 8, 0, 7, 6, 5)
    else:
        print("Enter your puzzle, use a zero to represent the blank")
        row_one = list(map(int, input("Enter the first row, use space or tabs between numbers  ").split()))
        row_two = list(map(int, input("Enter the second row, use space or tabs between numbers  ").split()))
        row_three = list(map(int, input("Enter the third row, use space or tabs between numbers  ").split()))
        combined_list = row_one + row_two + row_three # checking if list combines
        initial = tuple(combined_list)
        print(combined_list)
        print(row_one)
        print(row_two)
        print(row_three)

    # Create initial puzzle state
    puzzle = PuzzleNode(list(initial), None, 3, "Initial State")
    
    print("\nEnter your choice of algorithm")
    print("\n1) Uniform Cost Search\n2) A* with the Misplaced Tile heuristic.\n3) A* with the Euclidean distance heuristic.\n")

    user_input = int(input("Please enter a number: "))
    while user_input != 1 and user_input != 2 and user_input != 3:
        print("Incorrect. ")
        user_input = int(input("Please enter a number: "))

    if user_input == 1:
        h = uniform_cost
        a_star(puzzle, h, trace=True)
    elif user_input == 2:
        h = count
        a_star(puzzle, h, trace=True)
    elif user_input == 3:
        h = euclidean
        a_star(puzzle, h, trace=True)

    return

if __name__ == "__main__":
    main()
