#Program to access two different financial calculators
import math


print("Choose either 'investment' or bond' from the menu below to proceed: ")

print("\ninvestment\t - to calculate the amount of interest you'll earn on interest \nbond\t\t - to calculate the amount you'll have to pay on a home loan")

#User inputs type of calculator they want
calculator = input("\nEnter the type of calculator you wish to use: ")

#Based on type of calculator user inputs answers to questions needed to calculate simple or compound interest
if calculator =="investment" or calculator =="Investment" or calculator =="INVESTMENT":
    money = float(input("\nEnter the amount of money you will be depositing: R "))
    interest_rate = int(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan to invest for: "))
    interest = input("\nDo you want 'simple' or 'compound' interest? ")
#Formulae to calculate simple or compund interest
    simple_interest = money*(1 + interest_rate/100 * years)
    rounded_simple_interest = round(simple_interest, 2)
    compound_interest = money * math.pow((1 + interest_rate/100),years)
    rounded_compound_interest = round(compound_interest)
    if interest =="simple" or interest =="Simple" or interest =="SIMPLE":
            print(f"\nThe simple interest you will earn on your investment after {years} years with an interest rate of {interest_rate}% is R{rounded_simple_interest} ")
    else:
            print(f"\nThe compound interest you will earn on your investment after {years} years with an interest rate of {interest_rate}% is R{rounded_compound_interest} ")

#Based on type of calculator user inputs answers to questions needed to home repayment
elif calculator =="bond" or calculator =="Bond" or calculator =="BOND":
    house = float(input("\nEnter the present value of the house: R "))
    house_rate = int(input("Enter the interest rate: "))
    months = int(input("Enter the number of months you will take to repay the bond: "))
#Formula to calculate loan repayment
    repayment = (house_rate/12 * house)/(1 -(1 + house_rate/12)**(-months))
    rounded_repayment = round(repayment,2)
    print(f"\nYou will need to repay R{rounded_repayment} each month ")

#Should the user enter the incorrect value an error message will appear
else:
    print("\nYour entry is incorrect. Please note the entries are case sensitive. Re-enter the correct calculator." )
