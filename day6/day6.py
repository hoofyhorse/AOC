import re

def get_races(file, kerning = False):
    data = [line.strip() for line in open('day6\day6_data.txt', 'r')]
    races = []
    if kerning == False:
        times = re.sub('\ +',' ',data[0].split(':')[1]).strip().split(' ')
        distances = re.sub('\ +',' ',data[1].split(':')[1]).strip().split(' ')
    else:
        times = [re.sub('\ +','',data[0].split(':')[1]).strip()]
        distances = [re.sub('\ +','',data[1].split(':')[1]).strip()]

    for i in range(0,len(times)):
        races.append(
        {
            "time": int(times[i]),
            "distance": int(distances[i])
        })
    return races

def calc_dists(time,target):
    counter = 0
    for i in range(0,time):
        distance = i * (time - i)
        if distance > target:
            counter += 1
    return counter

def get_number_of_ways(file,kerning = False):
    races = get_races(file, kerning)
    total = 0
    for race in races:
        number_of_ways = calc_dists(race["time"],race["distance"])
        if total == 0:
            total = number_of_ways
        else:
            total *= number_of_ways
    return total

my_file = 'day6\day6_data.txt'
print(get_number_of_ways(my_file,kerning=False))
print(get_number_of_ways(my_file,kerning=True))