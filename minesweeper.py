# DS T15 Compulsory Task 1 - Introduction to Python — Data Structures - 2D Lists

# This program takes a grid of # and -, where each # represents a mine and each dash (-)represents a mine-free spot.
# Returning a grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot.

# This functions has data manipulation on how will the grid be displayed
def mine_sweeper(grid):
# Firstly we initialise rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # Define a helper function to count mines in adjacent positions (I have refer this in stackoverflow.com)
    def count_adjacent_mines(row, col):
        count = 0
        #  the loop iterates over the three rows: the row above the current row, the current row, and the row below the current row.
        for i in range(row - 1, row + 2):   
            #  the nested loop iterates over the three columns: the column to the left of the current column, the current column, and the column to the right of the current column.    
            for j in range(col - 1, col + 2):   
                if (0 <= i < rows) and (0 <= j < cols) and grid[i][j] == "#":
                    count += 1
        return count

    # Create a new grid to store the results
    result = [[0] * cols for _ in range(rows)]

    # Iterate over the grid and update the result grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "-":
                result[i][j] = str(count_adjacent_mines(i, j))
            else:
                result[i][j] = "#"

    return result

grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Function is called and new grid is displayed 
result = mine_sweeper(grid)
for row in result:
    print(row)
