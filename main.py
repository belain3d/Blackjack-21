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

def whoWon(playerCount, dealerCount):
    if dealerCount < playerCount < 21:
        print("Player has won!")

    elif playerCount < dealerCount < 21:
        print("Dealer has won!")
    
    elif playerCount == dealerCount:
        print("Equal")

def checkIfOver21(playerCount, dealerCount):
    if playerCount > 21:
        print("Player has lost!")
    elif dealerCount > 21:
        print("Dealer has lost!")

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
            print("Your deck:", playerDeckWithFaces)
            print("Dealer's deck:", dealerDeckWithFaces)
            break
        elif dealerCount == 21:
            print("Blackjack for Dealer!")
            print("Your deck:", playerDeckWithFaces)
            print("Dealer's deck:", dealerDeckWithFaces)
            break
        elif playerCount > 21:
            print("Player went over 21")
            print("Your deck:", playerDeckWithFaces)
            print("Dealer's deck:", dealerDeckWithFaces)
            break
        elif dealerCount > 21:
            print("The dealer has lost!")
            print("Dealer went over 21")
            print("Your deck:", playerDeckWithFaces)
            print("Dealer's deck:", dealerDeckWithFaces)
            break

        elif playerCount < 21:
            print(dealerDeckWithFaces)
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

                        print("Dealer drew a card whilst player was not standing.")
                        print("Your deck:", playerDeckWithFaces)
                        print("Dealer's deck:", dealerDeckWithFaces)
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

                    print("Dealer drew a card whilst player was standing.")
                    print("Your deck:", playerDeckWithFaces)
                    print("Dealer's deck:", dealerDeckWithFaces)

                    checkIfOver21(playerCount, dealerCount)

                elif dealerChoice == "stand":
                    print("Dealer is standing whilst player is standing")
                    isDealerStanding = 1
            elif dealerCount > 17:
                checkIfOver21(playerCount, dealerCount)



    elif isDealerStanding == 0:
         if dealerCount <= 17:
                dealerChoice = random.choice(dealerOptions)
                if dealerChoice == "draw":
                    dealerDeck.append(random.choice(deck))
                    dealerDeckWithFaces = dealerDeck
                    checkIfTenOrAce(dealerDeck)
                    dealerCount = sum(dealerDeck)

                    print("Dealer drew a card whilst he wasnt standing.")
                    print("Your deck:", playerDeckWithFaces)
                    print("Dealer's deck:", dealerDeckWithFaces)
                elif dealerChoice == "stand":
                    print("Dealer is standing whilst he is standing")

    elif isDealerStanding == 1:
        if dealerCount > 21:
            print("Dealer Lost!")
        elif playerCount > 21:
            print("Player Lost!")
        
        elif dealerCount < playerCount < 21:
            print("Player Won!")
        
        elif playerCount < dealerCount < 21:
            print("Dealer Won!")