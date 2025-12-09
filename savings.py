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
    age = int(input("How old are you? "))

    # Give warning to older folks
    if age >= RETIREMENT_AGE:
        print("\n" + "A little late to be thinking about retirement, isn't it?" + "\n")
        sys.exit()
    else:
        return age


# Time horizon refers to length of time between now and typical retirement
def time_horizon(age):
    return RETIREMENT_AGE - age


# Use Future Value Formula to estimate future value after investing
def future_value(thz, spent):
    pessimist_value = spent * ((1 + PESSIMIST_ROR) ** thz)

    optimist_value = spent * ((1 + OPTIMIST_ROR) ** thz)

    return pessimist_value, optimist_value


# Initialize main function
def main():
    # Print new line for prettiness
    print("\n")

    # Ask user for age, calculate time horizon
    age = get_age()

    thz = time_horizon(age)

    print("\n" + f"Your estimated retirement is {thz} years away" + "\n")

    # Ask user for how much they spent
    # Using float since it's a monetary value
    spent = float(input("How much money did you just spend? $"))

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


main()
