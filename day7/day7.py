import re


def hand_to_array(hand, jokers = False):
    out_array = []
    for c in hand:
        if re.match('\d',c):
            out_array.append(int(c))
        if c == 'T': out_array.append(10)
        if c == 'J':
            if jokers == True:
                out_array.append(1)
            else:
                out_array.append(11)
        if c == 'Q': out_array.append(12)
        if c == 'K': out_array.append(13)
        if c == 'A': out_array.append(14)
    return out_array


def get_hand_strength(hand):
    hand_inf = {}
    for c in hand:
        try:
            hand_inf[c] += 1
        except KeyError:
            hand_inf[c] = 1
    counts = list(hand_inf.values())
    counts.sort(reverse=True)
    if 1 not in hand_inf.keys():
        if counts == [5]: return 7
        if counts == [4,1]: return 6
        if counts == [3,2]: return 5
        if counts == [3,1,1]: return 4
        if counts == [2,2,1]: return 3
        if counts == [2,1,1,1]: return 2
        if counts == [1,1,1,1,1]: return 1
    else:
        if counts == [5]: return 7
        if counts == [4,1]: return 7
        if counts == [3,2]: return 7
        if counts == [3,1,1]: return 6
        if counts == [2,2,1]: 
            if hand_inf[1] == 2:
                return 6
            else : return 5
        if counts == [2,1,1,1]: return 4
        if counts == [1,1,1,1,1]: return 2

    
    
def get_hands(jokers = False):
    data = [line.strip() for line in open('day7\day7_data.txt', 'r')]
    hands = []
    for line in data:
        num_hand = hand_to_array(line.split(' ')[0], jokers)
        bid = int(line.split(' ')[1])
        hands.append({
            "hand_strength" : get_hand_strength(num_hand),
            "hand_cards" : num_hand,
            "bid" : bid
        })
    return hands


def compare_arrays(arr1, arr2):
    for i in range(0,len(arr1)):
        if arr1[i] > arr2[i] : return True
        if arr1[i] < arr2[i] : return False

def sort_hands(hands):
    swapped = False
    for n in range(len(hands)-1, 0, -1):
        for i in range(n):
            if (hands[i]["hand_strength"] < hands[i + 1]["hand_strength"]) or \
                (hands[i]["hand_strength"] == hands[i + 1]["hand_strength"] and compare_arrays(hands[i]["hand_cards"],hands[i +1]["hand_cards"]) == False):
                swapped = True
                hands[i], hands[i + 1] = hands[i + 1], hands[i]        
        if not swapped:
            return


def get_total(hands):
    for n in range(0,len(hands)):
        hands[n]["rank"] = len(hands) - n

    total = 0
    for hand in hands:
        total += hand["bid"] * hand["rank"]
    return total



pt1_hands = get_hands()
sort_hands(pt1_hands)
print(get_total(pt1_hands))

pt2_hands = get_hands(jokers=True)
sort_hands(pt2_hands)
print(get_total(pt2_hands))



