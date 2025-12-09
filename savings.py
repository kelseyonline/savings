import sys

# Initialize any constants
# Average retirement age in the US
RETIREMENT_AGE = 65

# Initialize smaller functions 
def get_age():
    age = int(input("How old are you? "))

    # Give warning to older folks
    if age >= RETIREMENT_AGE:
        print("A little late to be thinking about retirement, isn't it?")
        sys.exit()
    else: 
        return age

def time_horizon(age):
    ...
    
def invested(age, amount):
    ...


# Initialize main function 
def main():
    # Ask user for age 
    age = get_age()

    # Ask user for how much they spent 
    # Produce estimated investment profit 

main()