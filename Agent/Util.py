import time

def clear_console():
    print("\033c", end="")

def print_grid(grid, sep="  "):

    h = len(grid)
    w = len(grid[0]) if h else 0
    text = '---- GRID ----'
    print(text.center(21))
    for y in range(h):
        row = []
        for x in range(w):
            ch = grid[y][x]
            row.append(ch)
        print(sep.join(row))

def print_route(grid, path):
    steps = "Route: "
    for i, step in enumerate(path[0]):

        print('Total energy consumed: ', path[1][i])
        print('Total nodes explored: ', i)

        if i == 0:
            steps = steps + str(step)
            print(steps)
        else: 
            steps = steps + ' --> ' +  str(step)
            print(steps)

        newgrid = grid
        newgrid[step[0]][step[1]] = 'R'
        print_grid(newgrid)

        if i == len(path[0]) - 1:
            pass
        else:
            print("Next step in 1 second.")
            time.sleep(1)
            clear_console()
    