import random

# Configuration Variables
slots_and_values = {
    "🍎": 100,
    "🍇": 200,
    "🥝": 250,
    "🍋": 300,
    "🍓": 400,
}
initial_number_of_reels = 3
initial_wallet = 1000
bet_amount = 50


def title_screen():
    # prints the title screen
    print("""
+---------------------------+    
| Slot Machine Game         |
| Press 'ENTER' to Spin!    |
| Type 'quit' to quit.      |
| Type 'help' for commands. |          
+---------------------------+""")


def menu_screen(chosen_slots, prize, wallet, number_of_reels, spins, game_running):
    if game_running:
        print(f"Wallet: {wallet}$ Spins: {spins}")  # always prints wallet amount

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

        print("Press 'ENTER' to Spin!") # always printed

        # print prize money if won
        if prize > 0:
            print(f"Congratulations! you won {prize}$")


def unlockable_slots(wallet, slots_and_values, money_spent):
    # slot packs and values
    pack_one_icons = {"🐮": 150, "🐷": 150, "🐔": 150}
    pack_one_price = 300
    pack_one_unlocked = True

    pack_two_icons = {"🕹️": 250, "🎮": 250, "🖥️": 250}
    pack_two_price = 500
    pack_two_unlocked = True


    pack_three_icons = {"🚗": 500, "🏍️": 500, "🛵": 500}
    pack_three_price = 1000
    pack_three_unlocked = True


    pack_four_icons = {"♠️": 1200, "♣️": 1200, "♥️": 1200, "♦️": 1200}
    pack_four_price = 2200
    pack_four_unlocked = True


    pack_five_icons = {"👑": 5000, "💎": 5000, "🪙": 5000}
    pack_five_price = 10000
    pack_five_unlocked = True

    print(f"""
= = = = STORE = = = =
Wallet: {wallet}$
Enter the number of the slot pack you want to purchase!

1) {pack_one_price}$   Slot pack: {pack_one_icons}
2) {pack_two_price}$   Slot pack: {pack_two_icons}
3) {pack_three_price}$  Slot pack: {pack_three_icons}
4) {pack_four_price}$  Slot pack: {pack_four_icons}
5) {pack_five_price}$ Slot pack: {pack_five_icons}

Type 'exit' to leave the store.
""")

    while True:
        user_choice = input("> ").lower()

        # process user choice
        if user_choice == "1":
            if wallet < pack_one_price:
                print("Sorry! You don't have enough money.")
                continue
            wallet -= pack_one_price
            money_spent += pack_one_price
            slots_and_values = slots_and_values | pack_one_icons
            print(f"Purchased (-{pack_one_price}$): {pack_one_icons} ")
            print(f"Wallet: {wallet}$")

        elif user_choice == "2":
            if wallet < pack_two_price:
                print("Sorry! You don't have enough money.")
                continue
            wallet -= pack_two_price
            money_spent += pack_two_price
            slots_and_values = slots_and_values | pack_two_icons
            print(f"Purchased (-{pack_two_price}$): {pack_two_icons} ")
            print(f"Wallet: {wallet}$")

        elif user_choice == "3":
            if wallet < pack_three_price:
                print("Sorry! You don't have enough money.")
                continue
            wallet -= pack_three_price
            money_spent += pack_three_price
            slots_and_values = slots_and_values | pack_three_icons
            print(f"Purchased (-{pack_three_price}$): {pack_three_icons} ")
            print(f"Wallet: {wallet}$")

        elif user_choice == "4":
            if wallet < pack_four_price:
                print("Sorry! You don't have enough money.")
                continue
            wallet -= pack_four_price
            money_spent += pack_four_price
            slots_and_values = slots_and_values | pack_four_icons
            print(f"Purchased (-{pack_four_price}$): {pack_four_icons} ")
            print(f"Wallet: {wallet}$")

        elif user_choice == "5":
            if wallet < pack_five_price:
                print("Sorry! You don't have enough money.")
                continue

            wallet -= pack_five_price
            money_spent += pack_five_price
            slots_and_values = slots_and_values | pack_five_icons
            print(f"Purchased (-{pack_five_price}): {pack_five_icons} ")
            print(f"Wallet: {wallet}$")

        elif user_choice == "exit":
            print("Exiting store.")
            print("")
            title_screen()
            break

        elif user_choice == "":
            print("To leave the store, type 'exit'")

        else:
            print("Error.")

    return wallet, slots_and_values, money_spent


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


def prize_money(win_checker, number_of_reels, slots_and_values):
    # checks if there was a win and returns the prize money
    multiplier = 1 * number_of_reels
    if win_checker:
        # calculate multiplier based on number of reels
        if number_of_reels == 1:
            return 0  # no prize for 1 reel
        elif multiplier > 3:  # for 4 or more reels
            multiplier = 2 * number_of_reels  # for 4 or more reels, multiplier is 2x
        elif multiplier < 3:  # for 2 reels
            multiplier = 1 * number_of_reels  # for 2 reels, multiplier is 1x

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
→ Wallet: {wallet}$
→ Spins: {spins}
→ Money Earned: {money_earned}$
→ Money Spent: {money_spent}$
""")


def error_handling(user_choice):
    # prints an error message for unknown inputs
    return print(f"Input '{user_choice}' is unknown. Type 'help' for a list of commands.")


def game_logic(slots_and_values, initial_wallet, bet_amount):
    # main game logic function
    wallet = initial_wallet
    bet = bet_amount
    number_of_reels = initial_number_of_reels
    spins = 0
    money_earned = 0
    money_spent = 0
    profit = 0
    game_running = True

    title_screen()
    while game_running:

        # get user input
        user_choice = input("> ").lower()

        if user_choice == "":  # user pressed ENTER to spin
            # check if user has enough money to place bet
            if wallet <= 0 or wallet - bet <= 0: # checks if wallet is less than or equal to 0 or if wallet minus bet is less than or equal to 0
                print("Sorry! You don't have enough money.")
                stats(wallet, spins, money_earned, money_spent)
                print("")
                while True:
                    user_choice = input('Play again? (Yes/No) or type "continue" to retain stats: ').lower()
                    if user_choice == "yes":
                        wallet = initial_wallet
                        spins = 0
                        money_earned = 0
                        money_spent = 0
                        number_of_reels = initial_number_of_reels
                        print("Game restarted!")
                        print("")
                        title_screen()
                        print("")
                        break  # exits (this) loop

                    elif user_choice == "continue":
                        wallet += 1000 # retains stats but adds 1000$ to wallet
                        print("")
                        title_screen()
                        print("")
                        print("Continuing with current stats. Added 1000$ to wallet.")
                        print("")
                        break  # exits (this) loop

                    elif user_choice == "no":
                        # prints stats
                        stats(wallet, spins, money_earned, money_spent)
                        # checks if player made a profit or loss
                        if wallet > initial_wallet:
                            print(f"You made a profit of {wallet - initial_wallet}$!")
                        elif wallet < initial_wallet:
                            print(f"You lost {initial_wallet - wallet}$")
                        print("Thanks for playing!")
                        game_running = False
                        break  # exit the game loop

                    else:
                        error_handling(user_choice)

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
            prize = prize_money(win_checker, number_of_reels, slots_and_values)
            # add prize money to wallet
            money_earned += prize
            wallet += prize
            # display menu screen
            menu_screen(slots, prize, wallet, number_of_reels, spins, game_running)

        elif user_choice == "bet":  # user typed 'bet' to set bet amount
            try:
                # get user input for bet amount
                user_choice = int(input("Set bet amount: "))
                if user_choice < 1 or user_choice > 500:
                    print(f"Invalid bet amount. Please choose between 1 and 500.")
                else:
                    bet = user_choice
                    print(f"Bet amount set to {bet}$")
            except ValueError:
                error_handling(bet)

        elif user_choice == "reels":  # user typed 'reels' to set number of reels
            try:
                # get user input for number of reels
                user_choice = int(input("Set number of reels: "))
                if user_choice < 1 or user_choice > 9:
                    print(f"Invalid number of reels. Please choose between 1 and 9.")
                else:
                    number_of_reels = user_choice
                    print(f"Number of reels set to {number_of_reels}")
            except ValueError:
                error_handling(number_of_reels)

        elif user_choice == "stats":  # user typed 'stats' to view their stats
            stats(wallet, spins, money_earned, money_spent)

        elif user_choice == "restart":  # user typed 'restart' to restart the game
            wallet = initial_wallet
            spins = 0
            money_earned = 0
            money_spent = 0
            number_of_reels = initial_number_of_reels
            print("Game restarted!")

        elif user_choice == "add":  # user typed 'add' to add money to their wallet

            # get user input for amount to add
            user_choice = input("Amount to add: ")

            # validate user input for amount to add
            if user_choice == "max": # adds maximum amount of 10,000$
                wallet += 10000
                print("Added 10000$")
            else: # if user doesn't type 'max'
                try:
                    wallet_added_amount = int(user_choice) # converts users input into an int

                    if wallet_added_amount <= 0: # checks if its less than 0
                        print("Amount must be greater than 0")
                    elif wallet_added_amount > 10000: # or if its greater than 10,000
                        print("Amount cannot exceed 10,000$")
                        print(f"Added {wallet_added_amount}$")
                    else:
                        wallet += wallet_added_amount
                        print(f"Added {wallet_added_amount}$ to wallet. New wallet balance: {wallet}$")
                except ValueError:
                    print("Value must be a number between 1-10000.")

        elif user_choice == "wallet":  # user typed 'wallet' to view their wallet balance
            print(f"Wallet balance: {wallet}$")

        elif user_choice == "subtract":  # user typed 'subtract' to subtract money from their wallet
            try:
                # get user input for amount to subtract
                user_choice = int(input("Amount to subtract: "))
                if user_choice <= 0:
                    print("Amount must be greater than 0")
                elif user_choice > wallet:
                    print("Amount cannot exceed wallet balance.")
                else:
                    wallet -= user_choice
                    print(f"Subtracted {user_choice}$ from wallet. New wallet balance: {wallet}$")
            except ValueError:
                print("Value must be a number.")

        elif user_choice == "store":
            wallet, slots_and_values, money_spent = unlockable_slots(wallet, slots_and_values, money_spent)

        elif user_choice == "slots":
            print(f"Available slots: {slots_and_values}")

        elif user_choice == "profit":
            profit = money_earned - money_spent
            if profit >= 0:
                print(f"Total Profit: +{profit}$")
            else:
                print(f"Total Profit: {profit}$")

        elif user_choice == "options":
            print("No options available yet.")

        elif user_choice == "quit" or "exit":  # user typed 'quit' to exit the game
            print("")
            stats(wallet, spins, money_earned, money_spent)
            if wallet > initial_wallet:
                print(f"You made a profit of {wallet - initial_wallet}$!")
            elif wallet < initial_wallet:
                print(f"You lost {initial_wallet - wallet}$")
            print("Thanks for playing!")
            break  # exit the game loop

        elif user_choice == "help" or "commands":  # user typed 'help' to get a list of commands
            print("""
Commands:
store - Open the store to buy slot packs 
slots - lists available slots
reels - Set number of reels
stats - View player stats
restart - Restart the game
add - Add money to wallet (type 'max' for maximum amount)
wallet - View wallet balance
quit - Quit the game         
help - View this help message
profit - view total profit made or loss
""")

        else:  # unknown input
            error_handling(user_choice)
            continue


game_logic(slots_and_values, initial_wallet, bet_amount)
