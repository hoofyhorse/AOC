import re



def validator(spring_string: str, distribution: list) -> bool:
    split_by_space = spring_string.split('.')
    remove_empty = list(filter(None, split_by_space))
    if len(remove_empty) != len(distribution): return False
    for i in range(0,len(distribution)):
        if len(remove_empty[i]) == distribution[i]: continue
        else : return False
    return True

def build_sub_table(length: int) -> list:
    sub_table = []
    num = 0
    while True:
        binary_list = list(str(format(num, 'b')))
        binary_list.reverse()
        if len(binary_list) > length: break

        while len(binary_list) < length:
            binary_list.append('0')

        sub_table.append(binary_list)
        num += 1
    return sub_table


def substitutor(spring_string: str) -> int:
    valid_subs = []
    
    line = spring_string.split(' ')[0]
    distribution = [int(x) for x in spring_string.split(' ')[1].split(',')]
    sub_table = build_sub_table(len(re.findall('\?',line)))

    q_positions = []
    for i in range(0,len(line)):
        if line[i] == '?': q_positions.append(i)

    for sub in sub_table:
        list_str = list(line)
        for i in range(0,len(q_positions)):
            if sub[i] == '0' : list_str[q_positions[i]] = '.'
            if sub[i] == '1' : list_str[q_positions[i]] = '#'
        
        substitution = ''.join(list_str)
        if validator(substitution,distribution): valid_subs.append(substitution)
    return len(valid_subs)
    

data = [line.strip() for line in open('day12\\day12_data.txt', 'r')]

count = 0
for line in data:
    fl = line.split(' ')[0]
    fl = fl+'?'+fl+'?'+fl+'?'+fl+'?'+fl
    fd = line.split(' ')[1]
    fd = fd+','+fd+','+fd+','+fd+','+fd

    bigun = fl + ' ' + fd

    count += substitutor(bigun)
print(count)


