import os
import random
from SaveHandling import *

def CoinFlip(coins):
    user_returned = False
    while True:
        #Sides and random pick
        sides = ['heads','h','tails','t']
        rand_int = random.randint(0, 1)
        adjust_coins(coins)

        print(f"To go back just type 'return'\n")
        print(f'Coin Amount: ', coins)
        print('Options: Heads(H) & Tails(T)')

        #Get user input, check if 'return'
        user_input: str = input('Pick side: ')
        if user_input.lower() == 'return':
            user_returned = True
            break

        while True:
            try:
                bet = int(input('Bet Amount: '))
                break
            except ValueError:
                print("Please enter a valid integer.")

        #Make sure user pick is a valid color
        if user_input.lower() in sides and BetCheck(bet, coins):
            print('Side Flipped:', sides[rand_int])

            #Win/Lose condition
            if sides[rand_int] == user_input.lower():
                coins += bet
                Clear()
                print(f'You won {bet} coins!')
                continue
            else:
                coins -= bet
                Clear()
                print(f'You lost {bet} coins.')
                continue

        #If not valid, restart
        else:
            Clear()
            print('Not Valid')
            continue
    if user_returned:
        return coins


def BetCheck(bet: int, coins: int):
    """
    Check user bet to make sure its valid
    """
    if bet <= coins and bet != 0:
        return bet
    else:
        return None

def Clear():
    """
    Clear Terminal
    """
    os.system('cls')