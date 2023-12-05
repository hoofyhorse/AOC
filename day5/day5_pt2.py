
def range_splitter(in_range,rule):
    range_start  = int(in_range.split("-")[0])
    range_end  = int(in_range.split("-")[1])
    result = []
    remainder = []
    #case_1 range entirely within rule
    if range_start >= rule["start"] and range_end <= rule["end"]:
        result = f"{range_start + rule['rule']}-{range_end  + rule['rule']}"
    #case_2 range partially within rule
    if range_start >= rule["start"] and range_end > rule["end"] and range_start <= rule["end"]:
        result = f"{range_start + rule['rule']}-{rule['end'] + rule['rule']}"
        remainder.append(f"{rule['end'] + 1}-{range_end}")

    if range_start < rule["start"] and range_end <= rule["end"] and range_end >= rule["start"]:
        remainder.append(f"{range_start}-{rule['start'] - 1}")
        result = f"{rule['start'] + rule['rule']}-{range_end + rule['rule']}"

    #case_3 range overlaps rule
    if range_start < rule["start"] and range_end > rule["end"]:
        remainder.append(f"{range_start}-{rule['start'] - 1}")
        result = f"{rule['start'] + rule['rule']}-{rule['end']  + rule['rule']}"
        remainder.append(f"{rule['end'] + 1}-{range_end}")

    #case_4 range not in rule
    if (range_start < rule["start"] and range_end < rule["start"]) or (range_end > rule["end"] and range_start > rule["end"]):
        remainder.append(in_range)
    return result,remainder


def generate_rules(map):
    rules = []
    for line in map:
        start = int(line.split(' ')[1])
        end = start + int(line.split(' ')[2]) - 1
        rule = int(line.split(' ')[0]) - start
        rules.append({
            'start': start, 
            'end': end, 
            'rule': rule
        })
    return rules



def process_rules(input,map):
    rules = generate_rules(map)
    results = []
    remains = []
    for rule in rules:
        if len(remains) > 0:
            input = []
            for r in remains:
                input.append(r)
            remains = []
        for item in input:
            result,remainder = range_splitter(item,rule)
            if len(result) > 0:
                results.append(result)
            for r in remainder:
                remains.append(r)
    for item in remains:
        results.append(item)

    return results

def reader(file_name):
    return [line.strip() for line in open(file_name, 'r')]

seeds_input= reader("day5\\pt2_seeds.txt")
seeds = []
for seed in seeds_input:
    start = int(seed.split(' ')[0])
    length = int(seed.split(' ')[1])
    seeds.append(f"{start}-{start + length-1}")



soils = process_rules(seeds,reader('day5\\seeds_to_soil_map.txt'))
fertilizers = process_rules(soils,reader('day5\\soil_to_fertilizer_map.txt'))
waters = process_rules(fertilizers,reader('day5\\fertilizer_to_water_map.txt'))
lights = process_rules(waters,reader('day5\\water_to_light_map.txt'))
temperatures = process_rules(lights,reader('day5\\light_to_temperature_map.txt'))
humidities = process_rules(temperatures,reader('day5\\temperature_to_humidity_map.txt'))
locations = process_rules(humidities,reader('day5\\humidity_to_location_map.txt'))

min_val = float('inf')
for location in locations:
    number_1 = int(location.split('-')[0])
    number_2 = int(location.split('-')[1])
    if number_1 < min_val:
        min_val = number_1
    if number_2 < min_val:
        min_val = number_2

print(min_val)