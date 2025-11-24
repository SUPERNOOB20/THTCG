def load_deck(path):

    deck: list = []



    file = open(path, "r")

    for card in file:
        deck.append(card)
    
    file.close()



    return deck