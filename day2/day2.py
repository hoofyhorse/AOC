import re
def filereader(file_path : str):
    with open(file_path, "r") as infile:
        for in_line in infile:
            yield in_line

total = 0
for game in filereader("day2\day2_data.txt"):
    game_number = game.split(':')[0].split(' ')[1]
    sets = game.split(':')[1].split(';')

    min_required = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    for set in sets:
        current_set = sets[0]
        draws = set.split(',')
        for draw in draws:
            colour = re.sub('[^a-zA-Z]','',draw)
            number = re.sub('\D','',draw)
            if int(number) > min_required[colour]:
                min_required[colour] = int(number)

    total += min_required['blue'] * min_required['red'] * min_required['green']

print(total)
