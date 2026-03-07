n = int(input("Enter board size N: "))
values = [[' ' for i in range(n)] for i in range(n)]

def board(values, n):
    horizontal_line = "+" + "-----+" * n
    for i in range(n):
        print(horizontal_line)
        for j in range(n):
            print("| ", values[i][j], end='  ')
        print("|")
    print(horizontal_line)

def add_queen(values, row, col):
    values[row][col] = 'Q'

def remove_queen(values, row, col):
    values[row][col] = ' '

def clear_board(values, n):
    for i in range(n):
        for j in range(n):
            values[i][j] = ' '

def is_safe(values, row, col, n):
    # Check column above current position
    for i in range(row): 
        if values[i][col] == 'Q':
            return False
    
    # Check upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if values[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if values[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
    
    return True 

def solve_all_n_queens(values, row, n, solutions):
    if row >= n:
        # Found a solution  save it
        solution_copy = [row[:] for row in values]  # Deep copy
        solutions.append(solution_copy)
        return
    
    for col in range(n):
        if is_safe(values, row, col, n):
            add_queen(values, row, col)
            solve_all_n_queens(values, row + 1, n, solutions)
            remove_queen(values, row, col)

solutions = []
solve_all_n_queens(values, 0, n, solutions)

print(f"\nFound {len(solutions)} solutions!\n")
for idx, sol in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    board(sol, n)
    print()