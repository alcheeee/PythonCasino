import random
import os
from SaveHandling import *

num_cards = [2,3,4,5,6,7,8,9,10]
face_cards = ['Jack','Queen','King']
ace_card = ['Ace']

Deck = (num_cards + face_cards + ace_card) * 4

def BlackJack(coins):
    user_returned = False
    while True:
        adjust_coins(coins)
        print(f"To go back just type 'return'\n")
        print('Coin Balance:', coins)

        user_input: str = input("Bet Amount: ")
        if user_input.lower() == 'return':
            user_returned = True
            break

        while True:
            try:
                bet = int(user_input)
                break

            except ValueError:
                print("Please enter a valid integer.")
                user_input: str = input("Bet Amount (or 'return'): ")
                if user_input.lower() == 'return':
                    user_returned = True
                    break

        if user_returned:
            break

        valid_bet = BetCheck(bet, coins)

        if valid_bet:
            random.shuffle(Deck)
            dealer_hand = [Deck.pop(), Deck.pop()]
            player_hand = [Deck.pop(), Deck.pop()]

            PlayerBlackJack = False
            DealerBlackjack = False
            PlayerBust = False
            PlayerStand = False
            PlayerDoubledDown = False

            if GetHandValue(dealer_hand) == 21:
                DealerBlackjack = True

            if GetHandValue(player_hand) == 21:
                PlayerBlackJack = True

            options = ['hit','h','stand','s','double down','dd']

            Clear()
            print('Coin Balance:', (coins - bet))
            print('Bet Amount:', bet)
            print('Dealer Face Up Card:', dealer_hand[0])
            print('Player Cards:', show_hand_and_value(player_hand))

            while not PlayerBlackJack:
                player_value = GetHandValue(player_hand)
                if player_value > 21:
                    Clear()
                    print('Bust! Your total is over 21.')
                    print('Hand:', show_hand_and_value(player_hand))
                    PlayerBust = True
                    break

                UserChoice = input('Options: Hit(H)/Stand(S)/Double Down(DD): ').lower()
                if UserChoice in ['hit', 'h']:
                    Deal(player_hand, Deck)
                    print('Current Hand:', show_hand_and_value(player_hand))

                elif UserChoice in ['stand', 's']:
                    print('You stood with:', show_hand_and_value(player_hand))
                    PlayerStand = True
                    break

                elif UserChoice in ['double down', 'dd']:
                    if coins >= bet * 2:
                        Deal(player_hand, Deck)
                        print('You Doubled Down with:', show_hand_and_value(player_hand))
                        PlayerDoubledDown = True
                        break
                    else:
                        print('Not enough coins')
                else:
                    print('Not Valid')

            if PlayerDoubledDown:
                bet = bet * 2

            if PlayerBust:
                coins -= bet
                continue

            player_value = GetHandValue(player_hand)
            if PlayerBlackJack and not DealerBlackjack:
                Clear()
                print('BlackJack!')
                print('You won', (bet*3), 'coins!')
                ShowHands(player_hand, dealer_hand)
                coins += (bet * 3)
                continue

            elif PlayerBlackJack and DealerBlackjack:
                Clear()
                ShowHands(player_hand, dealer_hand)
                print('You pushed')
                continue

            elif not PlayerBlackJack and DealerBlackjack:
                Clear()
                ShowHands(player_hand, dealer_hand)
                print('You lost', (coins - bet), 'coins.')
                coins -= bet
                continue

            DealerPlaying = True
            while DealerPlaying:
                dealer_value = GetHandValue(dealer_hand)
                if dealer_value > 21:
                    Clear()
                    print('Dealer Bust!')
                    ShowHands(player_hand, dealer_hand)
                    coins += bet
                    DealerPlaying = False

                elif dealer_value < 17:
                    Deal(dealer_hand, Deck)
                    Clear()
                    ShowHands(player_hand, dealer_hand)

                elif dealer_value > player_value:
                    Clear()
                    ShowHands(player_hand, dealer_hand)
                    print('You lost', bet, 'coins.')
                    coins -= bet
                    DealerPlaying = False

                elif dealer_value == player_value:
                    Clear()
                    ShowHands(player_hand, dealer_hand)
                    print('You push')
                    DealerPlaying = False
            continue
        else:
            print('Invalid Bet')
            continue

    if user_returned:
        return coins


def Deal(hand, deck):
    return hand.append(deck.pop())

def ShowHands(player, dealer):
    print('Player Cards:', player)
    print('Dealer Cards:', dealer)

def show_hand_and_value(hand):
    return f"{hand}\nValue: {GetHandValue(hand)}"

def GetHandValue(hand):
    value = 0
    aces = 0

    for card in hand:
        if card in face_cards:
            value += 10
        elif card == 'Ace':
            value += 11
            aces += 1
        else:
            value += card

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value


def BetCheck(bet: int, coins: int):
    """
    Check user bet to make sure its valid
    """
    if bet.is_integer() and bet <= coins and bet != 0:
        return True
    else:
        return False

def Clear():
    """
    Clear Terminal
    """
    os.system('cls')