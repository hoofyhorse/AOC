
def mapreader(map_file, in_value):
    map = [line.strip() for line in open(map_file, 'r')]
    for line in map:
        in_start = int(line.split(' ')[1])
        out_start = int(line.split(' ')[0])
        number_range = int(line.split(' ')[2])
        if in_value >= in_start and in_value <= in_start + number_range - 1:
            return in_value + (out_start - in_start)
    return in_value



pt1_seeds = [int(line.strip()) for line in open("day5\\seeds.txt", 'r')]
soils = []
for seed in pt1_seeds:
    soils.append(mapreader('day5\\seeds_to_soil_map.txt',seed))

fertilizers  = []
for soil in soils:
    fertilizers.append(mapreader('day5\\soil_to_fertilizer_map.txt',soil))

waters = []
for fertilizer in fertilizers:
    waters.append(mapreader('day5\\fertilizer_to_water_map.txt',fertilizer))

lights = []
for water in waters:
    lights.append(mapreader('day5\\water_to_light_map.txt',water))

temperatures = []
for light in lights:
    temperatures.append(mapreader('day5\\light_to_temperature_map.txt',light))

humidities = []
for temperature in temperatures:
    humidities.append(mapreader('day5\\temperature_to_humidity_map.txt',temperature))

locations = []
for humidity in humidities:
    locations.append(mapreader('day5\humidity_to_location_map.txt',humidity))

print(locations)
print(min(locations))


