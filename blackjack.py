import random
import numpy as np

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

class Player:
    def __init__(self, firstCard, secondCard):
        self.firstCard = firstCard
        self.secondCard = secondCard

class Dealer:
    def __init__(self, firstCard, secondCard):
        self.firstCard = firstCard
        self.secondCard = secondCard

        


colors = ['hearts', 'diamonds', 'spades', 'clubs']


def dealCard(i, npDeck):
    nextCard = npDeck[i]
    return nextCard

def hit():
    print("")

def stay():
    print("")
#strategy
def strategy(player, dealer):
    
    print(totalPlayer)


class BlackJackGame:

    def __init__(self, Hands):
        self.Hands = Hands



    #create deck
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = [Card(value, color) for value in values for color in colors]
    #convert to np array
    npDeck = np.array(deck)

    #shuffle the deck
    np.random.shuffle(npDeck)

    def checkI(i, npDeck):
        if(i == 51):
            np.random.shuffle(npDeck)
            return True
        return False
    
    

    #deal
    gameLoop = True
    i = 0
    lossCounter = 0
    winCounter = 0
    totalGames = 0
    tieCounter = 0
    while(totalGames < 1000000):
        




        if(i == 0):
            dealCard(i, npDeck)
            #burn card



        playerHasAce = False
        dealerHasAce = False
        #give first card to player
        player = Player(dealCard(i, npDeck), None)
        if(player.firstCard.value == "Ace"):
            playerHasAce = True

        i = i+1
        if(checkI(i, npDeck)):
            i = 0
        

        

        dealer = Dealer(dealCard(i, npDeck), None)
        if(dealer.firstCard.value == "Ace"):
            dealerHasAce = True

        i = i+1
        if(checkI(i, npDeck)):
            i = 0
        
        

        player.secondCard = dealCard(i, npDeck)
        if(player.secondCard.value == "Ace"):
            playerHasAce = True

        i = i+1
        if(checkI(i, npDeck)):
            i = 0


        dealer.secondCard = dealCard(i, npDeck)
        if(dealer.secondCard.value == "Ace"):
            dealerHasAce = True
        i = i+1
        if(checkI(i, npDeck)):
            i = 0

        print("Player recieves a " + player.firstCard.value + " of " + player.firstCard.color)
        print("Player recieves a " + player.secondCard.value + " of " + player.secondCard.color)
        print("")
        print("Dealer is showing a " + dealer.firstCard.value + " of " + dealer.firstCard.color)
        print("Card not showing is: " + dealer.secondCard.value + " of " + dealer.secondCard.color)


        

        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        playerFC = values.index(player.firstCard.value)+2 if (values.index(player.firstCard.value)+2) <= 10 else 10
        if(player.firstCard.value == 'Ace'):
            playerFC = 11
        playerSC = values.index(player.secondCard.value)+2 if (values.index(player.secondCard.value)+2) <= 10 else 10
        if(player.secondCard.value == 'Ace'):
            playerSC = 11
        dealerFC = values.index(dealer.firstCard.value)+2 if (values.index(dealer.firstCard.value)+2) <= 10 else 10
        if(dealer.firstCard.value == 'Ace'):
            dealerFC = 11
        dealerSC = values.index(dealer.secondCard.value)+2 if (values.index(dealer.secondCard.value)+2) <= 10 else 10
        if(dealer.secondCard.value == 'Ace'):
            dealerSC = 11
        


        print("")
        print("")

        totalPlayer = playerFC + playerSC

        print("Player Total Befor Action: " + str(totalPlayer))
        totalDealer = dealerFC + dealerSC



        print("Dealer Total Before Action: " + str(totalDealer))
        print("")
        print("")
        print("")

        if(totalDealer != 21):
            while(totalPlayer < 17):
                newCard = dealCard(i, npDeck)
                print("Player hit and recieved a " + newCard.value + " of " + newCard.color)
                newCardValue = values.index(newCard.value)+2 if (values.index(newCard.value)+2) <= 10 else 10
                if(newCard.value == "Ace"):
                    newCardValue = 11
                    playerHasAce = True
                totalPlayer += newCardValue
                if(totalPlayer > 21 and playerHasAce):
                    totalPlayer -= 10
                    playerHasAce = False
                # print(totalPlayer)
                i=i+1
                if(checkI(i, npDeck)):
                    i = 0
            #if they bust dont run
            if(totalPlayer <= 21):
                while(totalDealer < 17):
                    newCard = dealCard(i, npDeck)
                    print("Dealer hit and recieved a " + newCard.value + " of " + newCard.color)
                    newCardValue = values.index(newCard.value)+2 if (values.index(newCard.value)+2) <= 10 else 10
                    if(newCard.value == "Ace"):
                        newCardValue = 11
                        dealerHasAce = True
                    totalDealer += newCardValue
                    if(totalDealer > 21 and dealerHasAce):
                        totalDealer -= 10
                    i=i+1
                    if(checkI(i, npDeck)):
                        i = 0




        print("")
        print("THE HAND RESULTS ARE: ")
        print("Player: " + str(totalPlayer))
        print("Dealer: " + str(totalDealer))


        if(totalDealer > 21):
            winCounter += 1
        elif(totalPlayer > 21):
            lossCounter +=1
        elif(totalPlayer > totalDealer):
            winCounter += 1
        elif(totalPlayer < totalDealer):
            lossCounter += 1
        elif(totalDealer == totalPlayer):
            tieCounter +=1

        totalGames += 1



        print("")
        print("")
        print("Total Games: " + str(totalGames)) 
        print("Total Losses: " + str(lossCounter))
        print("Total Won: " + str(winCounter))
        print("Total Ties: " + str(tieCounter))
        winPercentage = (winCounter * 100) / totalGames
        print("Win Percentage: " + str(winPercentage))
        gameLoop = False

