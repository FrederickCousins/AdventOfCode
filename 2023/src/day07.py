import aocd

CARD_RANKING1 = ['2', '3', '4', '5', '6',
                 '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

CARD_RANKING2 = ['J', '2', '3', '4', '5', '6',
                 '7', '8', '9', 'T', 'Q', 'K', 'A']

TYPE_RANKING = ['HC', '1P', '2P', '3K', 'FH', '4K', '5K']


def loadInput():
    data = aocd.get_data(year=2023, day=7).split("\n")
    hands = [line.split()[0] for line in data]
    bids = [int(line.split()[1]) for line in data]
    return hands, bids


def classifyHand(hand, joker=False):
    hand = list(hand)
    counts = {rank: hand.count(rank)
              for rank in CARD_RANKING1 if hand.count(rank) > 0}

    if joker:
        joker_count = counts.pop("J", 0)

    counts_values = sorted(counts.values(), reverse=True)
    if not counts_values:
        counts_values = [0]

    if joker:
        counts_values[0] += joker_count

    hand_classification = {
        (5,): '5K',
        (4, 1): '4K',
        (3, 2): 'FH',
        (3, 1, 1): '3K',
        (2, 2, 1): '2P',
        (2, 1, 1, 1): '1P'
    }.get(tuple(counts_values), 'HC')  # type: ignore

    return hand_classification


def solve(hands, bids, joker):
    classifications = [classifyHand(hand, joker) for hand in hands]

    # Combine hands, bids, and classifications into a list of tuples
    combined_data = list(zip(hands, bids, classifications))

    # Sort by type ranking and card ranking
    if not joker:
        combined_data.sort(key=lambda x: (TYPE_RANKING.index(x[2]), [
            CARD_RANKING1.index(card) for card in x[0]]))
    else:
        combined_data.sort(key=lambda x: (TYPE_RANKING.index(x[2]), [
            CARD_RANKING2.index(card) for card in x[0]]))

    # Unpack sorted data
    hands, bids, classifications = zip(*combined_data)

    # Calculate total
    total = sum(bid * i for i, bid in enumerate(bids, 1))

    return total


def part1(data):
    hands, bids = data
    print(f"Part 1: {solve(hands, bids, joker=False)}")


def part2(data):
    hands, bids = data
    print(f"Part 2: {solve(hands, bids, joker=True)}")


INPUT = loadInput()
part1(INPUT)
part2(INPUT)
