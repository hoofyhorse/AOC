import re
def filereader(file_path : str):
    with open(file_path, "r") as infile:
        data = []
        for in_line in infile:
            data.append(in_line)
    return data
schematic = filereader("day3\day3_data.txt")


def get_number_locations(schematic: str):
    number_inf = []
    line_index = 0
    for line in schematic:
        number_started = False
        number = ''
        index = 0
        for char in schematic[line_index]:
            if re.match('\d',char) and number_started == True:
                number = number + char
            if re.match('\d',char) and number_started == False:
                number = number + char
                number_started = True
                number_start_index = index
            if (re.match('\D',char) and number_started == True) or (index + 1 == len(line) and number_started == True):
                entry = {
                    "number" : int(number),
                    "start_index" : number_start_index,
                    "end_index" : index - 1,
                    "line" : line_index
                }
                number_inf.append(entry)
                number = ''
                number_started = False
            index += 1
        line_index += 1
    return number_inf

def get_gear_locations(schematic: str):
    gears = []
    line_index = 0
    for line in schematic:
        index = 0
        for char in schematic[line_index]:
            if re.match('\*',char):
                entry = {
                    "gear_index": index,
                    "gear_line": line_index
                }
                gears.append(entry)
            index += 1
        line_index += 1
    return gears

def add_gear_number_intersects(gears, number_inf):
    for gear in gears:
        adjacent_numbers = []
        gear_radius = []
        for row in range(gear["gear_line"]-1,gear["gear_line"]+2):
            for col in range(gear["gear_index"] -1, gear["gear_index"] + 2):
                gear_radius.append(f"{row},{col}")

        for entry in number_inf:
            number_locations = []
            row = entry["line"]
            for col in range(entry["start_index"], entry["end_index"] + 1):
                number_locations.append(f"{row},{col}")

            if any(item in gear_radius for item in number_locations):
                adjacent_numbers.append(entry["number"])
        
        gear["adjacent_numbers"] = adjacent_numbers



def pt1(number_inf):
    total = 0
    for entry in number_inf:
        for row in range(entry["line"]-1,entry["line"]+2):
            for col in range(entry["start_index"] -1, entry["end_index"] + 2):
                try:
                    if re.match("[^\d\.\n]",schematic[row][col]):
                        total = total + entry['number']
                        break
                except:
                    "do nothing"

    print(total)

def pt2(gears):
    total = 0
    for gear in gears:
        if len(gear["adjacent_numbers"]) == 2:
            mult = gear["adjacent_numbers"][0] * gear["adjacent_numbers"][1]
            total += mult
    print(total)

    
schematic = filereader("day3\day3_data.txt")
number_inf = get_number_locations(schematic)
pt1(number_inf)
gears = get_gear_locations(schematic)
add_gear_number_intersects(gears, number_inf)
pt2(gears)

