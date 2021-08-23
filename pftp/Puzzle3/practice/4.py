deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S', '3_C', '3_D', '3_H', '3_S',
        '4_C', '4_D', '4_H', '4_S', '5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S',
        '7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S', '9_C', '9_D', '9_H', '9_S',
        '10_C', '10_D', '10_H', '10_S', 'J_C', 'J_D', 'J_H', 'J_S',
        'Q_C', 'Q_D', 'Q_H', 'Q_S', 'K_C', 'K_D', 'K_H', 'K_S']


def computerAssistant4Cards():
    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = 0
    while number < 99999:
        number = int(input('Please give random number' +
                               ' of at least 6 digits:'))
    for i in range(4):
        number = number * (i + 1) // (i + 2)
        n = number % 52
        cards.append(deck[n])
        cind.append(n)
    subCards = {}
    for i in cind:
        for j in cind:
            if i - j != 0:
                subCards[abs(i - j)] =  (min(i,j), max(i,j))
    first = sorted(subCards.items())[0]
    firstCind, hidden = int(first[1][0]), int(first[1][1])
    rangeNum = first[0]
    firstOutput = deck[firstCind]
    hiddenOutput = deck[hidden]

    cards.remove(firstOutput)
    cards.remove(hiddenOutput)
    cind.remove(firstCind)
    cind.remove(hidden)
    if rangeNum <= 6:
        frontOrBack = 'front'
    else:
        frontOrBack = 'back'
        rangeNum -= 6

    sideCase = {1: ['右', '右', '右'], 2: ['右', '右', '左'],
                3: ['右', '左', '右'], 4: ['左', '右', '左'],
                5: ['左', '右', '右'], 6: ['左', '左', '左']}

    for idx, case in enumerate(sideCase[rangeNum]):
        if idx == 0:
            print ('First card is:', firstOutput, case, frontOrBack)
        else:
            print (idx, 'nd card is:', cards[idx-1] , case)

    guess = input('What is the hidden card?')
    if guess == hiddenOutput:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed!')

computerAssistant4Cards()