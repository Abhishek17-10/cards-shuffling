import itertools, random
deck = list(itertools.product(range (1, 14), ['spade', 'heart', 'clubs', 'diamond' ]))
random.shuffle(deck)

#Draw 5 cards
print('The 5 combiination of cards is')
for i in range(5):
    print(deck[i][0], "of", deck[i][1])