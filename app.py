# version 1.0
# 1-1-26

import random

wallet = 1000

def title_screen():
    print("""
Slot Machine Game
Press 'ENTER' to Spin!
Type 'quit' to quit.
            """)


def menu_screen(chosen_slots, prize):
    print(f"""
wallet {wallet}$
{chosen_slots}

Press 'ENTER' to Spin!
    """)
    # checks if prize was won. if so it prints to screen.
    if prize > 0:
        print(f"Congratulations! you won {prize}$")


def slot_spinner():
    possible_slot_icons = ["🍎", "🍊", "🍇", "🥝", "🍋"]
    chosen_slots = []
    # randomly chooses 3 possible slot icons and appends them to chosen_slots
    for icon in range(3):
        slot_selection = random.choice(possible_slot_icons)
        chosen_slots.append(slot_selection)

    return chosen_slots


def slot_calculator(chosen_slots):
    win_checker = True
    # iterates to determine if slot icons are the same
    for i in range(len(chosen_slots)):
        if chosen_slots[i] != chosen_slots[i-1]:
            win_checker = False

    return win_checker


def prize_money(win_checker):
    # awards player money if win_checker is True
    prize_money = 0
    if win_checker:
        prize_money += 500

    return prize_money


def error_handling():
    print("")


def game_logic():
    title_screen()
    global wallet

    while True:
        user_choice = input("> ")

        if user_choice == "":
            if wallet <= 0:
                print("Sorry! You are out of money.")
                break
            else:
                wallet -= 50
                slots = slot_spinner()
                win_checker = slot_calculator(slots)
                prize = prize_money(win_checker)
                wallet += prize
                menu_screen(slots, prize)
        elif user_choice == "quit":
            break
        else:
            # error_message()
            print("unknown")


game_logic()
