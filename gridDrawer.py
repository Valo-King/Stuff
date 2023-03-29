grid = []
num = 14
num2 = 0
for i in range(15):
    grid.append([' '] * 15)
def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))
def get_valid_index(prompt):
    while True:
        try:
            index = int(input(prompt))
            if index >= 1 and index <= 15:
                return index
            print("Must be 1 - 15!")
        except ValueError:
            print("Must be an integer!")

print("Let me draw something for you.")
for i in range(15):
    grid[0][i] = 0
    grid[i][14] = 0
for i in range(14 , 0 , -1):
    grid[14][i] = 0
for i in range(2 , 14 , 1):
    grid[i][1] = 0
for i in range(2 , 13 , 1):
    grid[2][i] = 0
    grid[i][12] = 0
for i in range(12 , 2 , -1):
    grid[12][i] = 0
for i in range(12 , 3 , -1):
    grid[i][3] = 0
for i in range(10 , 3 , -1):
    grid[4][i] = 0
    grid[i][10] = 0
for i in range(9 , 4 , -1):
    grid[10][i] = 0
for i in range(10 , 5 , -1):
    grid[i][5] = 0
for i in range(8 , 5 , -1):
    grid[6][i] = 0
for i in range(8 , 6 , -1):
    grid[i][8] = 0
grid[8][7] = 0
grid[7][7] = 0
while num != -1:
    grid[num][num] = "x"
    num = num - 1
num = 14
while num != -1:
    grid[num][num2] = "x"
    num = num - 1
    num2 = num2 + 1
for i in range(0 , 15 , 1):
    grid[i][7] = "x"
    grid[7][i] = "x"
while True:
    print_board(grid)
    char = input("What do you want to draw with? ")
    row = get_valid_index("Row: ")
    col = get_valid_index("Col: ")
    grid[row - 1][col - 1] = char
    yn = input("Do you want to continue? ")
    if yn == "yes" or yn == "YES" or yn == "Y" or yn == "y":
        continue
    else:
        break
print_board(grid)
