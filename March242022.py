# cw1
grid = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
for value in grid[:3]:
    for valueTwo in range(8):
        value[valueTwo] = 1
for value in grid[5:]:
    for valueTwo in range(8):
        value[valueTwo] = 1
print(grid)
        