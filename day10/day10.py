data = [list(line.strip()) for line in open('day10\\day10_data.txt', 'r')]

def determine_start_loc(grid, start_char):
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if grid[i][j] == start_char:
                return i,j


def start_tiles_and_shape(grid,start_row, start_col):
    up = down = left = right = False
    tiles = []
    if grid[start_row+1][start_col] in ('|','J','L'): 
        down = True
        tiles.append({"row" : start_row + 1, "col": start_col, "prev_movement" : 'down', "steps" : 1}) 
    if grid[start_row-1][start_col] in ('|','F','7'): 
        up = True
        tiles.append({"row" : start_row - 1, "col": start_col, "prev_movement" : 'up', "steps" : 1}) 
    if grid[start_row][start_col+1] in ('-','7','J'): 
        right = True
        tiles.append({"row" : start_row, "col": start_col + 1, "prev_movement" : 'right', "steps" : 1}) 
    if grid[start_row][start_col-1] in ('-','F','L'): 
        left = True
        tiles.append({"row" : start_row, "col": start_col -1, "prev_movement" : 'left', "steps" : 1}) 

    if up and down : shape = '|'
    if up and right : shape = 'L'
    if up and left : shape = 'J'
    if down and right : shape = 'F'
    if down and left : shape = '7'
    if left and right : shape = '-'

    return tiles, shape


def go_to_next_tile(tile, grid):
    shape = grid[tile["row"]][tile["col"]]
    if shape == '|' and tile["prev_movement"] == 'down': movement = 'down'
    if shape == '|' and tile["prev_movement"] == 'up': movement = 'up'

    if shape == 'L' and tile["prev_movement"] == 'down': movement = 'right'
    if shape == 'L' and tile["prev_movement"] == 'left': movement = 'up'

    if shape == 'J' and tile["prev_movement"] == 'down': movement = 'left'
    if shape == 'J' and tile["prev_movement"] == 'right': movement = 'up'

    if shape == 'F' and tile["prev_movement"] == 'up': movement = 'right'
    if shape == 'F' and tile["prev_movement"] == 'left': movement = 'down'

    if shape == '7' and tile["prev_movement"] == 'up': movement = 'left'
    if shape == '7' and tile["prev_movement"] == 'right': movement = 'down'

    if shape == '-' and tile["prev_movement"] == 'left': movement = 'left'
    if shape == '-' and tile["prev_movement"] == 'right': movement = 'right'

    if movement == 'right': tile["col"] += 1
    if movement == 'left': tile["col"] += -1
    if movement == 'up': tile["row"] += -1
    if movement == 'down': tile["row"] += 1

    tile["steps"] += 1
    tile["prev_movement"] = movement

    
path = []

start_row, start_col = determine_start_loc(data,'S')
tiles, start_shape = start_tiles_and_shape(data,start_row,start_col)

path.append((start_row,start_col))
path.append((tiles[0]["row"],tiles[0]["col"]))
path.append((tiles[1]["row"],tiles[1]["col"]))


while not (tiles[0]["row"] == tiles[1]["row"] and tiles[0]["col"] == tiles[1]["col"]):
    for tile in tiles:
        go_to_next_tile(tile,data)
        path.append((tile["row"],tile["col"]))

print(tiles[0]["steps"])

#replace start shape so we can find volume
data[start_row][start_col] = start_shape

delims = ('|','L','J')

volume = 0
for i in range(0,len(data)):
    open = 0
    for j in range(0,len(data[i])):
        if data[i][j] in delims and (i,j) in path and open > 0: 
            open = 0
            continue
        if open > 0 and (i,j) not in path : 
            volume += 1
            data[i][j] = 'I'
        
        if open <= 0 and (i,j) not in path : 
            data[i][j] = 'O'

        if data[i][j] in delims and (i,j) in path: 
            open += 1

for line in data:
    print(''.join(line))
print(volume)