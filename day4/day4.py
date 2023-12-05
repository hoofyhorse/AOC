import re

data = [line.strip() for line in open("day4\day4_data.dat", 'r')]

def pt1(data):
    
    total_score = 0
    for line in data:

        winning_numbers = line.split(':')[1].split('|')[0].replace('  ',' ').strip().split(' ')
        my_numbers = line.split(':')[1].split('|')[1].replace('  ',' ').strip().split(' ')

        score = 0

        for number in my_numbers:
            if number in winning_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total_score += score
    print(total_score)

def pt2(data):
    i = 1
    cards = {}
    for line in data:
        cards[f"{i}"] = 1
        i += 1


    for line in data:

        winning_numbers = line.split(':')[1].split('|')[0].replace('  ',' ').strip().split(' ')
        my_numbers = line.split(':')[1].split('|')[1].replace('  ',' ').strip().split(' ')
        card_number = int(re.sub('\D','',line.split(':')[0]))

        score = 0
        for number in my_numbers:
            if number in winning_numbers:
                score += 1
        
        for i in range(1,score+1):
            card_number_to_add_to = card_number + i
            number_of_cards_to_add = cards[f"{card_number}"]
            cards[f"{card_number_to_add_to}"] += number_of_cards_to_add

    total = 0
    for key in cards:
        total += cards[key]

    print(total)

pt1(data)
pt2(data)
