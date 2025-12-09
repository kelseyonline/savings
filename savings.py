import sys

# Initialize any constants
# Average retirement age in the US
RETIREMENT_AGE = 65

# Average rate of return (100 year average)
OPTIMIST_ROR = 0.10

# More conservative rate of return (industry suggestion)
PESSIMIST_ROR = 0.60


# Initialize smaller functions
def get_age():
    age = int(input("How old are you? "))

    # Give warning to older folks
    if age >= RETIREMENT_AGE:
        print("A little late to be thinking about retirement, isn't it?")
        sys.exit()
    else:
        return age


# Time horizon refers to length of time between now and typical retirement
def time_horizon(age):
    return RETIREMENT_AGE - age


def invested(thz, spent):
    ...


# Initialize main function
def main():
    # Ask user for age, calculate time horizon
    age = get_age()

    thz = time_horizon(age)

    print(age, thz)

    # Ask user for how much they spent
    # Using float since it's a monetary value
    spent = float(input("How much money did you just spend? $"))

    # Produce estimated investment profit


main()
