
user_choice = input("Choose either 1 for 'investment' or 2 for 'bond': \n")
t = int(input("Enter the time period in years: \n"))
i = float(input("Enter your interest rate: \n"))
P1 = int(input("Enter the principle amount for your bond or investment: \n"))

# Naming the variables
r_rate = (i/100)
n = (t*12)
A1 = (P1 * t * i) / 100
A2 = (P1 * ((1 + r_rate)**t-1))
x = (P1 * t * i)/100
y_bond = (x + P1)/12
total_a1 = float(A1 + P1)
total_a2 = float(A2 + P1)
user1 = ("2")
user2 = ("1")
# Choosing between 1 or 2 for user will narrow inputs and typing errors.

# The if statements calculating the repayment depending on whether the user chose Bond or Investment option:

if user1 == user_choice:
    print("You have chosen a Bond! Now let's calculate your repayment: \n")
    x = (P1 * t * i)/100
    print(f"Your Bond interest repayment will be R {x} ")
    print(f"Your monthly Bond repayment will be R{y_bond} ")
elif user2 == user_choice:
    print("Your choice is investment! Now let's calculate your interest payment: \n")
    A1 = float(P1 * t * i)/100
    print(f"Your Simple Interest repayment will be R {A1}  ")
    A2 = float(P1 * ((1 + r_rate)**t-1))
    print(f"Your Compound Interest repayment will be R {A2} ")
    total_a1 = float(A1 + P1)
    total_a2 = float(A2 + P1)
    print(f"With Simple interest your total amount is: R{total_a1}")
    print(f"With Compound interest your total amount is: R{total_a2}")

else:
    print("Enter a valid option: ")

# Thus depending on the choice of the user 1 for investment option or 2 for bond option
# The program calculates for investment the interest on interest earned plus the total amount earned
# for the whole investment period.  For bond the program calculates interest payed on the bond and also
# the monthly R value the user must pay on his/her bond.

