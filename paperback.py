""" Main Paperback Module
"""

import random

import pandas as pd


class Card:
    """Card Object"""

    def __init__(self, letter, score, cost, fame) -> None:
        self.letter = letter
        self.score = score
        self.cost = cost
        self.fame = fame

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.letter)


class CardLoader:
    """Card Loader Object"""

    def __init__(self, cardfile="CardInfo.xlsx") -> None:
        self.start_df = pd.read_excel(cardfile, sheet_name="StartingDeck")

    def get_starting_deck(self):
        """Generate a starting deck

        Returns:
            list[Card]: Starting deck as Card list
        """
        starting_deck = []
        for row in self.start_df.itertuples():
            starting_deck.append(Card(*tuple(row[1:])))
        return starting_deck


class Player:
    """Player Object"""

    def __init__(self, deck) -> None:
        self.deck = deck
        random.shuffle(self.deck)

        self.hand = []
        self.play = []
        self.discard = []
        self.trashed = []

        self._draw()

    def _reshuffle_deck(self):
        self.deck = self.discard
        self.discard = []
        random.shuffle(self.deck)

    def create_word(self):
        """Virtual method for word creation

        Raises:
            NotImplementedError: to be implemented by subclasses
        """
        raise NotImplementedError

    def _play_cards(self, word):
        """Play cards

        Args:
            word (str): tmp word string

        Returns:
            list[Cards]: cards played
        """
        print("Playing: ", word)
        return self.play

    def _draw(self, num_cards=5, modifier=0):
        for _ in range(num_cards + modifier):
            if len(self.deck) == 0:
                self._reshuffle_deck()

            assert len(self.deck) > 0

            self.hand.append(self.deck.pop())

    def turn(self):
        """player turn
        """
        # Create Word
        word = self.create_word()
        self.play = self._play_cards(word)

        # Check word length

        # Resolve Abilities

        # Score your word

        # Buy Cards

        # Discard Cards
        self.discard = self.discard + self.hand
        self.hand = []

        # Draw Cards
        self._draw()

    def __str__(self) -> str:
        return (
            "{Deck: "
            + str(self.deck)
            + "\nHand: "
            + str(self.hand)
            + "\nDisc: "
            + str(self.discard)
            + "}"
        )


class HumanPlayer(Player):
    """Human player"""

    def __init__(self, deck) -> None:
        super().__init__(deck)

        player_name = "Test Human"
        print("Created", player_name)

    def create_word(self):
        # print("Current Hand: ", self.hand)
        # return input("Input word: ")
        return "test"


loader = CardLoader()
p1 = HumanPlayer(loader.get_starting_deck())
p2 = HumanPlayer(loader.get_starting_deck())

print(p1)
print(p2)
