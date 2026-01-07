import random

# Configuration Variables
slots_and_values = {
    "🍎": 100,
    "🍊": 150,
    "🍇": 200,
    "🥝": 250,
    "🍋": 300,
    "🦄": 425,
    "💎": 500,
    "⭐": 675,
    "🐉": 750,
    "🌈": 800,
    "🐍": 1000,
    "👑": 1500,
    "🕹️": 3000,
    "🚀": 5000   
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


def menu_screen(chosen_slots, prize, wallet):
# prints the menu screen with current wallet and chosen slots
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


def prize_money(win_checker):
    # checks if there was a win and returns the prize money
    if win_checker:
        # if there was a win, get the prize money from slots_and_values
        prize_money = slots_and_values[win_checker]
    else:
        # if there was no win, return 0
        prize_money = 0

    return prize_money


def error_handling(user_choice):
    # prints an error message for unknown inputs
    print(f"Input '{user_choice}' is unknown. Type 'help' for a list of commands.")


def game_logic(slots_and_values, initial_wallet, bet_amount):
    # main game logic function
    wallet = initial_wallet
    bet = bet_amount
    number_of_reels = initial_number_of_reels

    title_screen() # prints title screen (once)
    while True:
        # get user input
        user_choice = input("> ").lower()
    
    
        if user_choice == "": # user pressed ENTER to spin
            # check if user has enough money to place bet
            if wallet < bet:
                print("Sorry! You don't have enough money.")
                break

            # deduct bet from wallet
            wallet -= bet
            # spin the slots
            slots = slot_spinner(slots_and_values, number_of_reels)
            # check for wins
            win_checker = slot_calculator(slots)
            # calculate prize money
            prize = prize_money(win_checker)
            # add prize money to wallet
            wallet += prize
            # display menu screen
            menu_screen(slots, prize, wallet)


        elif user_choice == "reels": # user typed 'reels' to set number of reels
            try:
                # get user input for number of reels
                user_choice = int(input("Set number of reels: "))
            except ValueError:
                error_handling(number_of_reels)

            # validate user input for number of reels
            if user_choice <= 2: # minimum number of reels is 2
                print(f"Minimum number of reels is 2")
            elif user_choice > len(slots_and_values): # maximum number of reels is the number of slot icons
                print(f"Maximum number of reels is {len(slots_and_values)}")
            else: # if input is valid, set number of reels
                number_of_reels = user_choice
                print(f"Number of reels set to {number_of_reels}")


        elif user_choice == "quit": # user typed 'quit' to exit the game
            print("Thanks for playing!")
            print(f"You walked away with {wallet}$")
            break # exit the game loop

        elif user_choice == "help": # user typed 'help' to get a list of commands
            print("Press 'ENTER' to Spin! Type 'reels' to set number of reels. Type 'quit' to Quit.")

        else: # unknown input
            error_handling(user_choice)


game_logic(slots_and_values, initial_wallet, bet_amount)


"""
--- SAMPLE OUTPUT ---

wallet 1000$
Bet 50$

╔═══════ SLOTS ════════╗

⟩⟩  | 🥝 | 🍎 | 🍇 |  ⟨⟨

╚══════════════════════╝

>
"""

"""
--- SAMPLE OUTPUT ---
╔═══════ SLOTS ════════╗

⟩⟩  | 🥝 | 🍎 | 🍇 |  ⟨⟨

╠══════════════════════╣
║                      ║
║ Wallet 1000$         ║
║ You won 0$           ║
║ BET 50$              ║
╚══════════════════════╝
>
"""

