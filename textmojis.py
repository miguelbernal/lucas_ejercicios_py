grid = [
    ['.','.','.','.','.','.'],
    ['.','O','O','.','.','.'],
    ['O','O','O','O','.','.'],
    ['O','O','O','O','O','.'],
    ['.','O','O','O','O','O'],
    ['O','O','O','O','O','.'],
    ['O','O','O','O','.','.'],
    ['.','O','O','.','.','.'],
    ['.','.','.','.','.','.']
]

for columna in range(0, len(grid[0])):
    linea = ""
    for fila in range(0, len(grid)):
        linea += grid[fila][columna]
    print(linea)