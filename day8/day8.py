import re
from math import lcm

def define_map(network):
    map = {}
    for line in network:
        map[line.split(' = ')[0]] = {
                "L" : re.sub('[\(\)]','',(line.split(' = ')[1])).split(', ')[0],
                "R" : re.sub('[\(\)]','',(line.split(' = ')[1])).split(', ')[1]
            }
        
    return map


def steps_to_z(start_loc,directions,direction_map, only_last_z = False):
    location = start_loc
    switches = 0

    while True:
        for direction in directions:
            location = direction_map[location][direction]
            switches += 1
            if only_last_z == False and location == 'ZZZ':
                return switches
            if only_last_z == True and location[-1] == 'Z':
                return switches





directions = [line.strip() for line in open('day8\\directions.txt', 'r')][0]
network = [line.strip() for line in open('day8\\network.txt', 'r')]
map = define_map(network)
print(steps_to_z('AAA',directions, map))


locations = [key for key in list(map.keys()) if key[-1] == 'A']
end_locs = [steps_to_z(loc,directions,map,True) for loc in locations]
print(lcm(*end_locs))
