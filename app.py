import random

# Configuration Variables
slots_and_values = {
    "🍎": 100,
    "🍇": 200,
    "🥝": 250,
    "🍋": 300,
    "🍓": 400,
    "🦄": 500,
    "⭐": 750,
    "💎": 1000
}
initial_number_of_reels = 3
initial_wallet = 1000
bet_amount = 50


def title_screen():
# prints the title screen
    print("""
+------------------------+    
| Slot Machine Game      |
| Press 'ENTER' to Spin! |
| Type 'quit' to quit.   |
+------------------------+""")


def menu_screen(chosen_slots, prize, wallet, number_of_reels, spins):

    print(f"Wallet: {wallet}$""") # always prints wallet amount

    # prints the menu screen with slots based on number of reels
    if len(chosen_slots) == 1:
        print(f"""╔══ SLOT ══╗
⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
╚══════════╝
""")

    elif len(chosen_slots) == 2:
        print(f"""╔════ SLOTS ════╗
⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
╚═══════════════╝
""")

    elif len(chosen_slots) == 3:
        print(f"""╔══════ SLOTS ═══════╗
⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
╚════════════════════╝
""")

    elif len(chosen_slots) == 4:
        print(f"""╔═════════ SLOTS ═════════╗
⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
╚═════════════════════════╝
""")

    elif len(chosen_slots) == 5:
        print(f"""╔═══════════ SLOTS ════════════╗
⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
╚══════════════════════════════╝
""")

    elif len(chosen_slots) == 6:
        print(f"""╔═════════════ SLOTS ═══════════════╗
⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
╚═══════════════════════════════════╝

""")

    elif len(chosen_slots) == 7:
        print(f"""╔═══════════════ SLOTS ══════════════════╗
⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
╚════════════════════════════════════════╝
""")

    elif len(chosen_slots) == 8:
        print(f"""╔══════════════════ SLOTS ════════════════════╗
⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
╚═════════════════════════════════════════════╝
""")

    elif len(chosen_slots) >= 9:
        print(f"""╔════════════════════ SLOTS ═══════════════════════╗
⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
╚══════════════════════════════════════════════════╝
""")

    else:
        print("Error: Invalid number of reels.")

    # print prize money if won
    if prize > 0:
        print(f"Congratulations! you won {prize}$")


#     top_left_corner = "╔"
#     top_left_segment = "══"
#     top_right_segment = "══"
#     top_right_corner = "╗"

#     bottom_left_corner = "╚"
#     bottom_left_segment = "══"
    
#     bottom_right_segment = "══"
#     bottom_right_corner = "╝"


#     if len(chosen_slots) > 1:
#         title = " SLOTS "
#         bottom_middle_segment = "═══════"

#         multipler = len(chosen_slots)
#         width_multiplier = "═" * multipler
        
#        # width_multiplier_ex = "═"


#         print(f"""
# {top_left_corner}{top_left_segment}{width_multiplier}{title}{top_right_segment}{width_multiplier}{top_right_corner}
# ⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
# {bottom_left_corner}{bottom_left_segment}{width_multiplier}{bottom_middle_segment}{width_multiplier}{bottom_right_segment}{bottom_right_corner}
# """)


#     else:
#         title = " SLOT "
#         bottom_middle_segment = "══════"
#         print(f"""
# {top_left_corner}{top_left_segment}{title}{top_right_segment}{top_right_corner}
# ⟩⟩ | {' | '.join(chosen_slots)} | ⟨⟨
# {bottom_left_corner}{bottom_left_segment}{bottom_middle_segment}{bottom_right_segment}{bottom_right_corner}
# """)
    

def slot_spinner(slots_and_values, number_of_reels):
    # randomly selects slot icons from slots_and_values and returns them as a list
    possible_slot_icons = list(slots_and_values.keys())

    # empty list to hold chosen slot icons
    chosen_slots = []

    # randomly chooses 3 possible slot icons and appends them to chosen_slots
    for icon in range(number_of_reels):
        # randomly select a slot icon
        slot_selection = random.choice(possible_slot_icons)
        # append the selected slot icon to chosen_slots
        chosen_slots.append(slot_selection)

    return chosen_slots


def slot_calculator(chosen_slots):
    # checks if all chosen slots are the same
    if len(set(chosen_slots)) == 1:
        # if they are, return the slot icon
        return chosen_slots[0]
    # if not, return False
    return False


def prize_money(win_checker, number_of_reels):
    # checks if there was a win and returns the prize money
    multiplier = 1 * number_of_reels
    if win_checker:
        # calculate multiplier based on number of reels
        if number_of_reels == 1:
            return 0 # no prize for 1 reel
        elif multiplier > 3: # for 4 or more reels
            multiplier = 2 * number_of_reels # for 4 or more reels, multiplier is 2x
        elif multiplier < 3: # for 2 reels
            multiplier = 1 * number_of_reels # for 2 reels, multiplier is 1x

        if multiplier > 3 or multiplier < 2:
            # only print multiplier for 2 or 4+ reels
            print(f"Reel Multiplier: x{multiplier}")
        # if there was a win, get the prize money from slots_and_values
        prize_money = slots_and_values[win_checker] * multiplier
    else:
        # if there was no win, return 0
        prize_money = 0

    return prize_money


def stats(wallet, spins, money_earned, money_spent):
    # prints the player's stats
    print(f"""
+------------------------+
| Player Stats           |
+------------------------+
| Wallet: {wallet}$             |
| Spins: {spins}            |
| Money Earned: {money_earned}$   |
| Money Spent: {money_spent}$     |
+------------------------+""")
    
      
def error_handling(user_choice):
    # prints an error message for unknown inputs
    print(f"Input '{user_choice}' is unknown. Type 'help' for a list of commands.")


def game_logic(slots_and_values, initial_wallet, bet_amount):
    # main game logic function
    wallet = initial_wallet
    bet = bet_amount
    number_of_reels = initial_number_of_reels
    spins = 0
    money_earned = 0
    money_spent = 0

    title_screen() # prints title screen (once)
    while True:
        # get user input
        user_choice = input("> ").lower()
    
    
        if user_choice == "": # user pressed ENTER to spin
            # check if user has enough money to place bet
            if wallet < bet:
                print("Sorry! You don't have enough money.")
                stats(wallet, spins, money_earned, money_spent)
                break

            # increment spin counter
            spins += 1
            # deduct bet from wallet
            wallet -= bet
            money_spent += bet
            # spin the slots
            slots = slot_spinner(slots_and_values, number_of_reels)
            # check for wins
            win_checker = slot_calculator(slots)
            # calculate prize money
            prize = prize_money(win_checker, number_of_reels)
            # add prize money to wallet
            money_earned += prize
            wallet += prize
            # display menu screen
            menu_screen(slots, prize, wallet, number_of_reels, spins)


        elif user_choice == "reels": # user typed 'reels' to set number of reels
            try:
                # get user input for number of reels
                user_choice = int(input("Set number of reels: "))
                number_of_reels = user_choice
            except ValueError:
                error_handling(number_of_reels)

            # # validate user input for number of reels
            # if user_choice <= 2: # minimum number of reels is 2
            #     print(f"Minimum number of reels is 2")
            # elif user_choice > len(slots_and_values): # maximum number of reels is the number of slot icons
            #     print(f"Maximum number of reels is {len(slots_and_values)}")
            # else: # if input is valid, set number of reels
            #     number_of_reels = user_choice
            #     print(f"Number of reels set to {number_of_reels}")

        elif user_choice == "stats": # user typed 'stats' to view their stats
            stats(wallet, spins, money_earned, money_spent)

        elif user_choice == "restart": # user typed 'restart' to restart the game
            wallet = initial_wallet
            spins = 0
            money_earned = 0
            money_spent = 0
            number_of_reels = initial_number_of_reels
            print("Game restarted!")

        elif user_choice == "add": # user typed 'add' to add money to their wallet
            try:
                # get user input for amount to add
                user_choice = int(input("Amount to add: "))
            except ValueError:
                error_handling(user_choice)
                continue

            # validate user input for amount to add
            if user_choice <= 0:
                print("Amount must be greater than 0")
            else:
                wallet += user_choice
                print(f"Added {user_choice}$ to wallet. New wallet balance: {wallet}$")

        elif user_choice == "wallet": # user typed 'wallet' to view their wallet balance
            print(f"Wallet balance: {wallet}$")

        elif user_choice == "quit": # user typed 'quit' to exit the game
            print("Thanks for playing!")
            stats(wallet, spins, money_earned, money_spent)
            break # exit the game loop

        elif user_choice == "help": # user typed 'help' to get a list of commands
            print("""Commands: 
reels - Set number of reels
stats - View player stats
restart - Restart the game
add - Add money to wallet
wallet - View wallet balance
quit - Quit the game         
help - View this help message
""")

        else: # unknown input
            error_handling(user_choice)


game_logic(slots_and_values, initial_wallet, bet_amount)
