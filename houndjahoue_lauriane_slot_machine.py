"""
Description: text-based slot machine. User deposits money and we are going 
to allow them to bet on 1,2, or 3 lines of the slot machine. And then we're going
decide if they won and give an updated balance when neccessary.

Author: Lauriane Houndjahoue
"""
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [symbol for symbol, symbol_count in symbols.items() for _ in range(symbol_count)]

    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            separator = " | " if i != len(columns) - 1 else ""
            print(column[row], end=separator)
        print()


def deposit():
    while True:
        amount = input("Enter the amount to be deposited: $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        else:
            print("Please enter a valid amount (greater than 0).")


def number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you wish to bet on (1-{MAX_LINES}): ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        else:
            print(f"Please enter a valid number of lines (1-{MAX_LINES}).")


def get_bet():
    while True:
        amount = input(f"Enter the amount to bet on each line (between {MIN_BET}-{MAX_BET}): $")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        else:
            print(f"Please enter a valid bet amount (between {MIN_BET}-{MAX_BET}).")


def spin(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient funds. Your current balance is ${balance}")
        else:
            break

    print(f"You're betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    if winnings > 0:
        print(f"Congratulations! You've won ${winnings}.")
        print(f"You've won on lines:", *winning_lines)
    else:
        print("Sorry, you didn't win this time.")

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        choice = input("Press enter to play (q to quit): ").strip().lower()
        if choice == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")


main()
