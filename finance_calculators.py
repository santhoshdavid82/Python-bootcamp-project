import math

# A program that allows the user to access two different financial calculators: 
# An Investment Calculator and a Home Loan Repayment Calculator.

print("Welcome to the Finance Calculator program!")
print("Please select an option:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# If the user selects ‘investment’.
if option == "investment":
    print("\nYou have selected investment.\n")
    deposit = float(input("How much money are you depositing? "))
    interest_rate = float(input("What is the interest rate (as a percentage)? "))
    years = int(input("How many years do you plan to invest for? "))

    # Ask the user to input if they want 'simple' or 'compound' interest.
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()

    if interest == "simple":
        A = deposit * (1 + (interest_rate/100) * years)  # Interest formula
        print(f"\nThe total amount you will have after {years} years is {A}")

    elif interest == "compound":
        A = deposit * math.pow((1 + interest_rate/100), years)  # Interest formula
        print(f"\nThe total amount you will have after {years} years is {A : .2f}")
    else:
        print("Invalid interest type entered. Please try again.")
        exit()

# If the user selects ‘bond’.
elif option == "bond":
    print("\nYou have selected bond.\n")
    present_value = float(input("What is the present value of the house? "))
    interest_rate = float(input("What is the interest rate (as a percentage)? "))
    months = int(input("How many months do you plan to take to repay the bond? "))

    i = (interest_rate/100)/12  # ‘i’ is the monthly interest rate.

    repayment = (i * present_value) / (1 - math.pow((1 + i), -months))  # Bond repayment formula.

    print(f"\nYour monthly bond repayment will be {repayment : .2f}")
else:
    print("\nInvalid option selected. Please try again.")
    exit()
