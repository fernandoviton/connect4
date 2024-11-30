GAME_SIZE = 10

def create_empty_matrix(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def my_turn(matrix):
    column = int(input("Please enter a number: "))
    print(f"You entered: {column}")
    #if (matrix[0][0] == 0)
    row = 0
    for row in range(len(matrix)):
        if matrix[row][column] != 0: 
            row = row-1
            break;        
    if row > 0:
        matrix[row][int(column)] = 1

def check_for_winner(matrix, row, column, number):
    for row in range(len(matrix)):
        pass
    
    return True

def take_turns(matrix):
    while True: 
        my_turn(matrix)
        my_turn(matrix)
        my_turn(matrix)
        my_turn(matrix)
        if check_for_winner(matrix, 0, 0, 0) == True:
            print(f"You win!")
            break

# Example usage

if __name__ == "__main__":
    matrix = create_empty_matrix(GAME_SIZE)
    take_turns(matrix)

    for row in matrix:
        print(row)

