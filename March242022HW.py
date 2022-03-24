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
for count, value in enumerate(grid):
    for valueTwo in value:
        if count % 2 == 0:
         value[valueTwo] = 1
for count, value in enumerate(grid):
    if value % 2 == 1:
        for valueTwo in value:
            if count % 2 == 0:
                value[valueTwo] = 1

