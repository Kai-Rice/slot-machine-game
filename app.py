import random

def title_screen():
    print("""
+------------------------+    
| Slot Machine Game      |
| Press 'ENTER' to Spin! |
| Type 'quit' to quit.   |
+------------------------+""")


def menu_screen(chosen_slots, prize, wallet):
    print(f"""
+------------------------+   
| wallet {wallet}$            |
| {chosen_slots}     |
|                        |
| Press 'ENTER' to Spin! |
+------------------------+""")
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
    win_checker = False
    slot_1 = chosen_slots[0]
    slot_2 = chosen_slots[1]
    slot_3 = chosen_slots[2]

    # checks if all slots are the same.
    if slot_1 == slot_2 and slot_2 == slot_3:
        win_checker = slot_1 # if so, awards money.

    return win_checker


def prize_money(win_checker):
    if win_checker == "🍎":
     prize_money = 100
    elif win_checker == "🍊":
        prize_money = 300
    elif win_checker == "🍇":
        prize_money = 500
    elif win_checker == "🥝":
        prize_money = 800
    elif win_checker == "🍋":
        prize_money = 1000
    else:
        prize_money = 0

    return prize_money


def error_handling(user_choice):
    print(f"Input '{user_choice}' is unknown. Type 'help' for a list of commands.")


def game_logic():

    wallet = 1000
    bet = 50

    title_screen()
    while True:
        user_choice = input("> ").lower()

        if user_choice == "":
            if wallet < bet:
                print("Sorry! You don't have enough money.")
                break

            wallet -= bet
            slots = slot_spinner()
            win_checker = slot_calculator(slots)
            prize = prize_money(win_checker)
            wallet += prize
            menu_screen(slots, prize, wallet)

        elif user_choice == "quit":
            print("Thanks for playing!")
            print(f"You walked away with {wallet}$")
            break

        elif user_choice == "help":
            print("Press 'ENTER' to Spin! Type 'quit' to Quit.")

        else:
            error_handling(user_choice)


game_logic()
