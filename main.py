import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_win(columns, lines, bet, values):
    for line in range(lines):
        break

def gsm_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_sm(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | " )
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("\nDeposit Amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Choose a number that is bigger than 0.\n")
        else:
            print("Please enter a number!\n")

    return amount

def nb_lines():
    while True:
        lines = input("How many lines would like to play (1-" + str(MAX_LINES) + ") : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Choose a valid number of lines!.\n")
        else:
            print("Please enter a number!\n")

    return lines


def gbet():
    while True:
        amount = input("Bet Amount: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Choose a number that is between ${MIN_BET} - ${MAX_BET}.\n")
        else:
            print("Please enter a number!\n")
    return amount


def main():
    balance = deposit()
    lines = nb_lines()
    while True:
        bet = gbet()
        tbet = bet * lines

        if tbet >= balance:
            print(f"Not enough money! Balance: + ${balance}")
        else:
            break
    
    
    print(f"Bet Amount: ${bet} on {lines} lines, your total bet is: ${tbet}")


    slots = gsm_spin(ROWS, COLS, symbol_count)
    print_sm(slots)



main()