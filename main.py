#main.py
from algorithm.heuristic import a_star, uniform_cost, count, euclidean
from puzzle.puzzleNode import PuzzleNode
def main():

    # print("\nWelcome to bgarc208/hwhee004 puzzle solver. Enter the size of the puzzle you wish to solve (e.g., '3' for 3x3): ")

    # size = int(input("Please enter a number: "))
    # while size < 2:
    #     print("Size must be at least 2.")
    #     size = int(input("Please enter a number: "))

    # print("Enter your puzzle, use a zero to represent the blank")
    # while True:
    #     rows = []
    #     for i in range(size):
    #         row = list(map(int, input(f"Enter row {i + 1}, use space or tabs between numbers: ").split()))
    #         rows.extend(row)
    #     if len(rows) != size * size:
    #         print(f"Incorrect number of tiles. Expected {size * size} tiles.")
    #         continue
    #     if sorted(rows) != list(range(size * size)):
    #         print(f"Puzzle must contain all numbers from 0 to {size * size - 1} exactly once.")
    #         continue
    #     initial = tuple(rows)
    #     break 
    # 
    # for row in range(size):
    #     print(rows[row*size:(row+1)*size])
    

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

    size = 3
    # Create initial puzzle state
    puzzle = PuzzleNode(list(initial), size, "Initial State")
    
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
