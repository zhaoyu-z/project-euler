def load_file(path):
    lines = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines

def get_hands(string):
    splits = string.split(" ")
    return splits[:5], splits[5:]

value_map = {
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14
}

def get_high_card(hand):
    return max([value_map[s[0]] for s in hand])

def is_straight(values):
    highest = max(values)
    if highest - 1 in values and \
        highest - 2 in values and \
        highest - 3 in values and \
        highest - 4 in values:
        return True
    return False

def is_same_suit(suits):
    return len(set(suits)) == 1

def count_values(values):
    temp = {}
    for v in values:
        temp[v] = temp.get(v, 0) + 1
    items = sorted(temp.items(), key=lambda item: item[1], reverse=True)
    if items[0][1] == 4:
        return ['Four of a Kind', items[0][0]]
    elif items[0][1] == 3 and items[1][1] == 2:
        return ['Full House', items[0][0], items[1][0]]
    elif items[0][1] == 3:
        return ['Three of a Kind', items[0][0]]
    elif items[0][1] == 2 and items[1][1] == 2:
        return ['Two Pairs', items[0][0], items[1][0]]
    elif items[0][1] == 2:
        return ['One Pair', items[0][0]]
    else:
        return ['High Card']

def get_rank(hand):
    """
        1 High Card: Highest value card.
        2 One Pair: Two cards of the same value.
        3 Two Pairs: Two different pairs.
        4 Three of a Kind: Three cards of the same value.
        5 Straight: All cards are consecutive values.
        6 Flush: All cards of the same suit.
        7 Full House: Three of a kind and a pair.
        8 Four of a Kind: Four cards of the same value.
        9 Straight Flush: All cards are consecutive values of same suit.
        10 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    """
    values = [value_map[s[0]] for s in hand]
    suits = [s[1] for s in hand]
    counts = count_values(values)

    if is_same_suit(suits) and is_straight(values) and sorted(values)[0] == 10:
        return [10, 14]
    elif is_same_suit(suits) and is_straight(values):
        return [9, max(values)]
    elif counts[0] == 'Four of a Kind':
        return [8, counts[1]]
    elif counts[0] == 'Full House':
        return [7, counts[1], counts[2]]
    elif is_same_suit(suits):
        return [6]
    elif is_straight(values):
        return [5]
    elif counts[0] == 'Three of a Kind':
        return [4, counts[1]]
    elif counts[0] == 'Two Pairs':
        return [3, counts[1], counts[2]]
    elif counts[0] == 'One Pair':
        return [2, counts[1]]
    elif counts[0] == 'High Card':
        return [1]
    else: 
        print("error hand:", hand)
        return [-1]

def get_highest_cards_from_two(hand1, hand2, wins1, wins2):
    max1 = get_high_card(hand1)
    max2 = get_high_card(hand2)

    if max1 > max2:
        wins1 += 1
        return wins1, wins2
    elif max1 < max2:
        wins2 += 1
        return wins1, wins2
    else:
        hand1 = [x for x in hand1 if value_map[x[0]] != max1]
        hand2 = [x for x in hand2 if value_map[x[0]] != max2]
        return get_highest_cards_from_two(hand1, hand2, wins1, wins2)

def higher(hand1, hand2, wins1, wins2):
    return get_highest_cards_from_two(hand1, hand2, wins1, wins2)

def poker_hands():
    data = load_file("../p054_poker.txt")

    wins1 = wins2 = 0
    for line in data:
        hand1, hand2 = get_hands(line)
        rank1 = get_rank(hand1)
        rank2 = get_rank(hand2)
        if rank1[0] > rank2[0]:
            wins1 += 1
        elif rank1[0] < rank2[0]:
            wins2 += 1
        elif len(rank1) == 3: # get_rank case 3 and 7
            if rank1[1] > rank2[1]:
                wins1 += 1
            elif rank1[1] < rank2[1]:
                wins2 += 1
            else:
                if rank1[2] > rank2[2]:
                    wins1 += 1
                elif rank1[2] < rank2[2]:
                    wins2 += 1
                else:
                    wins1, wins2 = higher(hand1, hand2, wins1, wins2)
        elif len(rank1) == 2: # other cases
            if rank1[1] > rank2[1]:
                wins1 += 1
            elif rank1[1] < rank2[1]:
                wins2 += 1
            else:
                wins1, wins2 = higher(hand1, hand2, wins1, wins2)
        else:
            wins1, wins2 = higher(hand1, hand2, wins1, wins2)
    return wins1

print(poker_hands())