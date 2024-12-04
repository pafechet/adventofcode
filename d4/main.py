with open('input.txt') as file:
    fi = file.readlines()

matrix = []
for line in fi:
    row = []
    for char in line:
        row.append(char)
    matrix.append(row)

directions = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
    (-1, -1), # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1)    # down-right
]

def read_word(matrix, x, y, direction):
    word = ""
    dx, dy = direction
    while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
        if matrix[x][y] != 0:
            word += str(matrix[x][y])
            if word == "XMAS":
                return True
        x += dx
        y += dy
        

tot = 0
toto = 0

for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for direction in directions: 
                if read_word(matrix, i, j, direction):
                    tot += 1
print(tot)
print(toto)

