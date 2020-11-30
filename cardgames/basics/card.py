class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.representation = f"{self.numberRepresentation()}{self.suit}"
        # self.cardRepresentation = f"{self.representation}{self.suit}"

    def numberRepresentation(self):
        if self.value == 1:
            return "A"
        elif self.value == 11:
            return "J"
        elif self.value == 12:
            return "Q"
        elif self.value == 13:
            return "K"
        else:
            return str(self.value)
        return


# Para sortear uma única carta / To pick a single card
if __name__ == "__main__":
    from cardgames.basics.deck import Deck
    import random
    deck = Deck()
    while True:
        card = random.choice(deck)
        print(f"Pulled card: {card.representation}")
        if deck.length() == 0:
            confirmation = input("You have no more cards to pull. Press Enter to start a new deck or 'n' to exit. ")
            if confirmation == "n":
                break
            else:
                deck = Deck()
        else:
            confirmation = input(f"Press 'n' to quit or 'Enter' to pull another card. {deck.length()} cards remaining. ")
            if confirmation == "n":
                break
            else:
                continue