data = [line.strip() for line in open('day9\\day9_data.txt', 'r')]

def get_history(line):
    row = line.split(' ')

    layers = {}
    layers[0] = [int(entry) for entry in row]


    while sum(layers[max(layers.keys())]) != 0:
        current_row = layers[max(layers.keys())]
        differences = []
        for i in range(0,len(current_row)-1):
            differences.append(int(current_row[i+1]) - int(current_row[i]))
        layers[max(layers.keys()) + 1] = differences
    return layers

def get_next_entry(layers):
    for i in range(max(layers.keys()),0,-1):
        last_value = layers[i][-1]
        previous_last_value = layers[i-1][-1]
        layers[i-1].append(last_value + previous_last_value)
    return layers[0][-1]


def get_previous_entry(layers):
    for i in range(max(layers.keys()),0,-1):
        first_value = layers[i][0]
        previous_first_value = layers[i-1][0]
        layers[i-1].insert(0,previous_first_value - first_value)
    return layers[0][0]



next_total = 0
previous_total = 0
for line in data:
    layers = get_history(line)
    next_total += get_next_entry(layers)
    previous_total += get_previous_entry(layers)

print(next_total, previous_total)
    


