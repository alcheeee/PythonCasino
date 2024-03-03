import os
import random
import time
from SaveHandling import *

REQUIRED = 8
SPEED = 0.3
MIN_BET = 5
TURBO = False

slot_items = ['1','2','3','V','O','F','B']
slot_values = {
    '1': 8,
    '2': 10,
    '3': 12,
    'V': 18,
    'O': 26,
    'F': 30,
    'B': 0
}
WEIGHTS = (26, 24, 20, 15, 10, 3, 2)
free_spin_amounts = [3, 5, 10, 20]

def Slots(coins):
    user_returned = False
    while True:
        adjust_coins(coins)
        print(f"To go back just type '0'(zero) in both fields.\n")
        print(f'Coin Amount: ', coins)
        while True:
            try:
                bet = int(input('Bet Amount(5 Min): '))
                spins = int(input('Auto-Spins Amount: '))
                if bet == 0 or spins == 0:
                    user_returned = True
                break
            except ValueError:
                print("Please enter a valid integer.")

        if user_returned:
            break

        if BetCheck(bet, coins):
            adjust_coins(coins)

            FREE_SPINS_ACTIVE = False
            FEATURE_ACTIVE = False

            spin_count = 0
            amount_won = 0

            while spin_count != spins:

                adjust_coins(coins)
                spin_count += 1
                total_score = 0
                track_score = {}

                roll, raw_roll = generate_roll()
                for row in roll:
                    print(row)
                    time.sleep(SPEED)

                for i in raw_roll:
                    if i in track_score:
                        track_score[i] += 1
                    else:
                        track_score[i] = 1

                for key, value in track_score.items():
                    if value >= REQUIRED:
                        total_score += calculate_values(key, value)

                    elif value >= 3 and key in ['F', 'B']:
                        if key == 'F':
                            FREE_SPINS_ACTIVE = True
                        else:
                            FEATURE_ACTIVE = True

                amount_won = round((total_score / 10) * bet)

                if FREE_SPINS_ACTIVE:
                    FREE_SPINS = random.choices(
                        free_spin_amounts, weights=(50, 30, 15, 5), k=1)
                    spins += FREE_SPINS[0]
                    print(f'Free Spins, {FREE_SPINS[0]} spins added!')
                    FREE_SPINS_ACTIVE = False

                if FEATURE_ACTIVE:
                    random_multi = random.randint(3,50)
                    amount_won = amount_won * random_multi
                    print('Feature Active, win multiplied by', random_multi)
                    FEATURE_ACTIVE = False

                if amount_won > 0:
                    coins += amount_won
                    print(f'You Won {amount_won} coins!\n')

                elif amount_won <= 0:
                    amount_won = 0
                    coins -= bet
                    print('')

                print(f'Spins Left: {spins-spin_count}\nCoins: {coins}')

                time.sleep(2)
                Clear()
            continue

        #If not valid, restart
        else:
            Clear()
            print('Not Valid')
            continue
    if user_returned:
        return coins


def calculate_values(value, count):
    if value in ['B', 'F']:
        return value
    else:
        extra_points = count - REQUIRED
        base_value = slot_values[value]
        total_score = base_value + ((base_value * extra_points)/2)
        return total_score

def generate_roll():
    random_results = random.choices(
        slot_items,
        weights=WEIGHTS,
        k=25
    )
    rows = []
    for index, item in enumerate(random_results):
        if index % 5 == 0:
            current_row = []
            rows.append(current_row)
        current_row.append(item)

    return rows, random_results


def BetCheck(bet: int, coins: int):
    """
    Check user bet to make sure its valid
    """
    if bet.is_integer() and bet <= coins and bet >= MIN_BET:
        return True
    else:
        return False

def Clear():
    """
    Clear Terminal
    """
    os.system('cls')