import re


def spread_galaxies(universe, points, spread = 1):
    for i in range(len(universe)-1,-1,-1):
        if re.match('^\.*$',''.join(universe[i])):
            for point in points:
                if point[0] > i: point[0] += spread
    
    universe = [list(x) for x in zip(*universe)]

    for i in range(len(universe)-1,-1,-1):
        if re.match('^\.*$',''.join(universe[i])):
            for point in points:
                if point[1] > i: point[1] += spread


def get_galaxies(universe):
    star_locations = []
    for row in range(0,len(universe)):
        for col in range(0,len(universe[row])):
            if universe[row][col] == '#':
                star_locations.append([row,col])

    return star_locations

def calc_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

def all_pair_distances(galaxies):
    temp_galaxies = galaxies.copy()
    total_sum = 0
    for point_1 in galaxies:
        temp_galaxies.remove(point_1)
        for point_2 in temp_galaxies:
            total_sum += calc_distance(point_1,point_2)
    return total_sum

universe = [list(line.strip()) for line in open('day11\\day11_data.txt', 'r')]

galaxies = get_galaxies(universe)

spread_galaxies(universe, galaxies, 1)
print(all_pair_distances(galaxies))

galaxies = get_galaxies(universe)

spread_galaxies(universe, galaxies, 999999)
print(all_pair_distances(galaxies))
