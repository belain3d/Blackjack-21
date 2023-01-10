import random
import math

def checkIfTenOrAce(userDeck):
    for i in userDeck:
        if i in ["Q", "J", "K"]:
            userDeck.remove(i)
            userDeck.append(10)
    for i in userDeck:
        if i in ["A"]:
            if playerCount <= 10:
                userDeck.remove(i)
                userDeck.append(11)
            elif playerCount >= 11:
                userDeck.remove(i)
                userDeck.append(1)

deck = ["Q", "J", "K", "A",
        2, 3, 4, 5, 6, 7, 8, 9, 10]

playerDeck = []
dealerDeck = []

isPlayerStanding = 0
isDealerStanding = 0

playerDeckWithFaces = []
dealerDeckWithFaces = []

playerCount = 0
dealerCount = 0

dealerChoice = ""
dealerOptions = ["draw", "stand"]

for _ in range(2):
    playerDeck.append(random.choice(deck))
    dealerDeck.append(random.choice(deck))
    playerDeckWithFaces = playerDeck
    dealerDeckWithFaces = dealerDeck
    checkIfTenOrAce(playerDeck)
    checkIfTenOrAce(dealerDeck)
    playerCount = sum(playerDeck)
    dealerCount = sum(dealerDeck)

while True:
    if isPlayerStanding == 0:
        print(playerDeckWithFaces, end=" ")
        if playerCount == 21:
            print("Blackjack for Player!")
            break
        elif dealerCount == 21:
            print("Blackjack for Dealer!")
            break
        elif playerCount > 21:
            print("You lost!")
            break
        elif dealerCount > 21:
            print("The dealer has lost!")
            break

        elif playerCount < 21:
            drawCard = input("draw/stand/doubledown: ")
            if drawCard == "draw":
                playerDeck.append(random.choice(deck))
                playerDeckWithFaces = playerDeck
                checkIfTenOrAce(playerDeck)
                playerCount = sum(playerDeck)

                if dealerCount <= 17:
                    dealerChoice = random.choice(dealerOptions)

                    if dealerChoice == "draw":
                        dealerDeck.append(random.choice(deck))
                        dealerDeckWithFaces = dealerDeck
                        checkIfTenOrAce(dealerDeck)
                        dealerCount = sum(dealerDeck)
                        print(dealerDeckWithFaces)
                    elif dealerChoice == "stand":
                        print("Dealer is standing whilst Player is not standing")



            elif drawCard == "stand":
                isPlayerStanding = 1
            elif drawCard == "doubledown":
                playerDeck.append(random.choice(deck))
                isPlayerStanding = 1

    elif isPlayerStanding == 1:
            if dealerCount <= 17:
                dealerChoice = random.choice(dealerOptions)
                if dealerChoice == "draw":
                    dealerDeck.append(random.choice(deck))
                    dealerDeckWithFaces = dealerDeck
                    checkIfTenOrAce(dealerDeck)
                    dealerCount = sum(dealerDeck)
                    print(dealerDeckWithFaces)
                elif dealerChoice == "stand":
                    print("Dealer is standing whilst player is standing")
    
    elif isDealerStanding == 0:
         if dealerCount <= 17:
                dealerChoice = random.choice(dealerOptions)
                if dealerChoice == "draw":
                    dealerDeck.append(random.choice(deck))
                    dealerDeckWithFaces = dealerDeck
                    checkIfTenOrAce(dealerDeck)
                    dealerCount = sum(dealerDeck)
                    print(dealerDeckWithFaces)
                elif dealerChoice == "stand":
                    print("Dealer is standing whilst he is standing")

    elif isDealerStanding == 1:
        print(playerDeckWithFaces)
        print(dealerDeckWithFaces)