import random
import os
import json
import time
from CoinFlip import CoinFlip
from BlackJack import BlackJack
from Slot import Slots
from SaveHandling import *

def PickUserOptions(choice, coins):
    options = [
            '1', #Coin FLip
            '2', #BlackJack
            '3', #Slot
            'work' #Getting coins
    ]

    Clear()
    if choice in options:
        if choice == '1':
            handle_game(CoinFlip, coins)
        elif choice == '2':
            handle_game(BlackJack, coins)
        elif choice == '3':
            handle_game(Slots, coins)
        elif choice == 'work':
            handle_game(working, coins)
    else:
        #not an option, return error
        Clear()
        MainMenu('Not A Valid Option')

#Main Menu of game
def MainMenu(ErrorMessage: str):
    while True:
        Clear()
        if ErrorMessage:
            print('ERROR: ', ErrorMessage, '\n')

        UserData = get_user_data()
        coins = UserData['coins']

        print("Get Coins by typing 'Work'")
        print('Coin Amount: ', coins)
        print('Coin Flip: 1 \nBlackJack: 2 \nSlot Machine: 3')
        print("Type the # of the game you'd like to play below.")

        user_input: str = input('Type an Option: ').lower()
        PickUserOptions(user_input, coins)
        continue

def working(coins):
    total_count = 0
    count = 0
    while True:
        Clear()
        total_count += 50
        count += 1
        print('You got', total_count, 'coins!')
        time.sleep(1)
        if count >= 5:
            user_input = input('Type (Yes/No) if you want to continue: ').lower()
            if user_input == 'yes':
                count = 0
                continue
            elif user_input == 'no':
                break
    return total_count + coins

def handle_game(game, coins):
    coin_change = game(coins)
    adjust_coins(coin_change)
    return MainMenu(None)

def Clear():
    """
    Clear Terminal
    """
    os.system('cls')


if __name__ == '__main__':
    UserData = get_user_data()
    coins = UserData['coins']
    MainMenu(None)