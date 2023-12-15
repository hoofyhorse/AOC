data = [line.strip() for line in open('day13\\day13_data.txt', 'r')]

def get_puzzle(puzzle_number : int) -> list:
    empty_lines = 0
    return_puzzle = []
    
    for line in data:
        if line == '':
            empty_lines += 1
            if empty_lines > puzzle_number:
                break
            else: return_puzzle = []
        else: return_puzzle.append(line)
        
    return return_puzzle




def get_possibilities(line, in_possibilities):
    possibile_mids = []
    for i in in_possibilities:
        left_side = line[0:i][::-1]
        
        right_side = line[i:]
        min_len = min(len(left_side),len(right_side))
        left_side = left_side[:min_len]
        right_side = right_side[:min_len]

        if left_side == right_side:
            possibile_mids.append(i)
    if 0 in possibile_mids:
        possibile_mids.remove(0)


    return possibile_mids


def find_reflection(puzzle, transpose= False):

    if transpose:
        puzzle = [list(x) for x in zip(*puzzle)]

    possibilities = range(0,len(puzzle[0]))

    for line in puzzle:
        possibilities = get_possibilities(line,possibilities)
    
    print(possibilities)



puzzle = get_puzzle(1)
find_reflection(puzzle, transpose=True)