import sys

# This module allows color output in the terminal
from colorama import Fore, Style

# Initialize any constants
# Average retirement age in the US
RETIREMENT_AGE = 65

# Average rate of return (100 year average)
# Based on annualized average ROR on the S&P 500
OPTIMIST_ROR = 0.10

# More conservative rate of return (industry suggestion)
PESSIMIST_ROR = 0.06


# Initialize smaller functions
def get_age():
    while True:
        try:
            age = int(input("How old are you? "))

            # Give warning to older folks and exit program
            if age >= RETIREMENT_AGE:
                print(
                    "\n"
                    + f"{Fore.BLUE}A little late to be thinking about retirement, isn't it?{Style.RESET_ALL}"
                    + "\n"
                )
                sys.exit()

            # Checks for negative number
            if age < 0:
                print(
                    "\n"
                    + f"{Fore.RED}You can't be a negative age! Try again.{Style.RESET_ALL}"
                    + "\n"
                )
                continue

            return age

        # Checks for non-float
        except ValueError:
            print(
                "\n"
                + f"{Fore.RED}Please input a monetary value{Style.RESET_ALL}"
                + "\n"
            )


# Time horizon refers to length of time between now and typical retirement
def time_horizon(age):
    return RETIREMENT_AGE - age


# Get purchase and do error handling
def get_purchase():
    # Ask user for how much they spent
    # Using float since it's a monetary value
    while True:
        try:
            spent = float(input("How much money did you just spend? $"))

            # Checks for negative number
            if spent < 0:
                print(
                    "\n"
                    + f"{Fore.RED}Please input a positive monetary value{Style.RESET_ALL}"
                    + "\n"
                )
                continue

            return spent
        # Checks for non-float
        except ValueError:
            print(
                "\n"
                + f"{Fore.RED}Please input a monetary value{Style.RESET_ALL}"
                + "\n"
            )


# Use Future Value Formula to estimate future value after investing
def future_value(thz, spent):
    pessimist_value = spent * ((1 + PESSIMIST_ROR) ** thz)

    optimist_value = spent * ((1 + OPTIMIST_ROR) ** thz)

    return pessimist_value, optimist_value


# Stores purchases during this session
# Calculates the sum of those purchases
def add_purchase(purchases, spent):
    purchases.append(spent)

    total_purchases = sum(purchases)

    return total_purchases


# Gets the user's next action
def next_action():
    while True:
        next = input("Do you have another purchase to add? (y/n) ")

        print("\n")

        if next == "y":
            return
        elif next == "n":
            sys.exit()


# Initialize main function
def main():
    # Print new line for prettiness
    print("\n")

    # Ask user for age, calculate time horizon
    age = get_age()

    thz = time_horizon(age)

    # Initialize purchase list
    purchases = []

    print(
        "\n"
        + f"Your estimated retirement is {Fore.BLUE}{thz}{Style.RESET_ALL} years away"
        + "\n"
    )

    # This reprompts the user until user is finished
    while True:

        # Ask user for how much they spent
        # Using float since it's a monetary value
        spent = get_purchase()

        # Produce estimated investment profit
        # I have to unpack the tuple here
        pessimist_value, optimist_value = future_value(thz, spent)

        # The ,.2f formats the string as currency
        print(
            "\n"
            + f"""In a bad case scenario (6% average rate of return)
    you would have {Fore.GREEN}${pessimist_value:,.2f}{Style.RESET_ALL} if you had invested
    this money instead"""
            + "\n"
        )

        print(
            f"""In a good case scenario (10% average rate of return, which
    is the historical average), you would have {Fore.GREEN}${optimist_value:,.2f}{Style.RESET_ALL}
    if you had invested this money instead"""
            + "\n"
        )

        # Add this purchase to the running total of purchases during this session
        total_purchases = add_purchase(purchases, spent)

        _, total_loss = future_value(thz, total_purchases)

        print(
            f"""You have missed out on {Fore.RED}${total_loss:,.2f}{Style.RESET_ALL} of future retirement money so far,
    based on an optimistic 10% rate of return :("""
            + "\n"
        )

        next_action()


main()
