import random

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return " of ".join((self.face, self.suit))

    def __lt__(self, other):
        return self.getValue() < other.getValue()
    def __gt__(self, other):
        return self.getValue() > other.getValue()
    def __eq__(self, other):
        return self.getValue() == other.getValue()
    
    def getValue(self):
        d1 = {"A":1, "J":11, "Q":12, "K":13}
        if self.face.isdigit():
            return int(self.face)
        return d1.get(self.face)

class BlackJackCard(Card):
    def getValue(self):
        d1 = {"A":11, "J":10, "Q":10, "K":10}
        if self.face.isdigit():
            return int(self.face)
        return d1.get(self.face)

class Deck:
    FACES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ('Diamonds', "Clubs", "Spades", "Hearts")
    NUMFACES = 13
    NUMSUITS = 4
    NUMCARDS = 52

    def __init__(self):
        # initialize data - stackOfCards - topCardIndex
        self.topCardIndex = 52
        # self.stackOfCards = [BlackJackCard(f, s) for s in Deck.SUITS for f in Deck.FACES]
        self.stackOfCards = []
        for f in Deck.FACES:
            for s in Deck.SUITS:
                bj = BlackJackCard(f, s)
                self.stackOfCards.append(bj)

    def nextCard(self):
        self.topCardIndex -= 1
        return self.stackOfCards[self.topCardIndex]

    def shuffle(self):
        random.shuffle(self.stackOfCards)
        self.topCardIndex = 52

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.win = 0
    
    def __repr__(self):
        return self.name + ": " + str(self.hand) + ": " + str(self.getHandValue()) + ": win " + str(self.win)

    def addCardToHand(self, card):
        self.hand.append(card)

    def getHandValue(self):
        total = 0
        hasA = False
        for c in self.hand:
            if c.face == "A":
                hasA = True
            total += c.getValue()
            if total > 21 and hasA:
                total -= 10
                hasA = False
        return total

    def hit(self):
        value = self.getHandValue()
        if value >= 20:
            return False
        elif value <= 10:
            return True
        answer = input(f"{self.name}: Do you want to hit? (y/n)")
        return True if answer == 'y' else False

    def cleanHand(self):
        self.hand = []

    def increaseWin(self):
        self.win += 1

    def showHand(self):
        return self.name + ": " + str(self.hand) + ": " + str(self.getHandValue())

    def getHandSize(self):
        return len(self.hand)

class Dealer(Player):
    def __init__(self):
        self.deck = Deck()
        self.name = "Dealer"
        self.hand = []
        self.win = 0

    def hit(self):
        value = self.getHandValue()
        if value < 17:
            return True
        return False

    def deal(self):
        return self.deck.nextCard()

    def showHand(self):
        output = self.name + "["
        count = 1
        for c in self.hand:
            if count != len(self.hand):
                output += str(c) + ", "
            else:
                output += "Hidden]"
            count += 1
        return output

    def shuffle(self):
        self.deck.shuffle()

class Game:
    def __init__(self):
        self.players = []
        self.dealer = Dealer()

    def addPlayer(self, player):
        self.players.append(player)

    def dealCardToAllPlayers(self):
        count = 0
        while count<2:
            for p in self.players:
                p.addCardToHand(self.dealer.deal())
            self.dealer.addCardToHand(self.dealer.deal())
            count += 1

    def showAllPlayerHand(self):
        for p in self.players:
            print(p.showHand())
        print(self.dealer.showHand())

    def cleanAllPlayerHand(self):
        for p in self.players:
            p.cleanHand()
        self.dealer.cleanHand()

    def isDealerWin(self, playerTotal, dealerTotal):
        if (playerTotal>21 and dealerTotal<=21) or (playerTotal<21 and  dealerTotal<=21 and playerTotal<dealerTotal):
            return True
        return False

    def isPlayerWin(self, playerTotal, dealerTotal):
        if (playerTotal<=21 and dealerTotal>21) or (playerTotal<=21 and  dealerTotal<21 and playerTotal>dealerTotal):
            return True
        return False

    def determineWiner(self):
        dealerTotal = self.dealer.getHandValue()
        for player in self.players:
            playerTotal = player.getHandValue()
            if self.isDealerWin(playerTotal, dealerTotal):
                self.dealer.increaseWin()
            if self.isPlayerWin(playerTotal, dealerTotal):
                player.increaseWin()

    def showResults(self):
        for p in self.players:
            print(p)
        print(self.dealer)

    def addPlayers(self):
        morePlayer = True
        while morePlayer:
            name = input("Please enter player's name: ")
            player = Player(name)
            self.addPlayer(player)
            answer = input("More player? (y/n) ")
            if answer != 'y':
                morePlayer = False

    def play(self):
        self.addPlayers()
        gameOver = False
        while not gameOver:
            self.dealer.shuffle()
            self.cleanAllPlayerHand()
            
            self.dealCardToAllPlayers()
            self.showAllPlayerHand()

            for p in self.players:
                hit = p.hit()
                while hit:
                    p.addCardToHand(self.dealer.deal())
                    print(p.showHand())
                    hit = p.hit()
            while self.dealer.hit():
                self.dealer.addCardToHand(self.dealer.deal())

            self.determineWiner()
            self.showResults()

            answer = input("Do you want to play again? (y or n) ").lower()
            if answer != 'y':
                gameOver = True


if __name__ == '__main__':
    game = Game()
    game.play()

    # game.addPlayer()
    # for p in game.players:
    #     print(p)

    # dealer = Dealer()
    # b1 = BlackJackCard("2","Spades")
    # b2 = BlackJackCard("J","Hearts")
    # b3 = BlackJackCard("4","Clubs")
    # dealer.addCardToHand(b1)
    # dealer.addCardToHand(b2)
    # dealer.addCardToHand(b3)
    # print(dealer.showHand())
