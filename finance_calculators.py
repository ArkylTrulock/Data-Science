# Include the math function import math.
import math

print("\nInvestment - To calculate the amount of interest you will earn on your investment.\nBond - To calculate how much you will have to pay on a home loan.")

# To proceed request user enter either 'investment with compound interest', 'investment with compound interest' or 'bond'.
finance = input("\nPlease enter 'investment' or 'bond' from the menu above before proceeding:\n ") #\n Create space under input request line.
 
finance = finance.lower()
finance = finance.strip()
finance = finance.strip("?")
 
if (finance == "investment"):
  print("Investment option has been selected: \n")
  # If the user selects 'investment' request they provide the inputs below.
  present_investment = float(input("Please enter deposit:\n£ "))
  annual_interest = float(input("Please enter annual interest rate:\n% "))
  number_of_years_invested = int(input("Please enter amount of years invested:\n "))
  confirm_interest=input("Please enter 'simple interest' or 'compound interest':\n ").lower()

  if (confirm_interest == "simple interest"):
   print("Simple interest option has been selected: \n")
  # If the user selects 'simple interest' after selecting 'investment' our background calculator does the calculations
   simple_interest = present_investment*(1+(annual_interest/100)*number_of_years_invested)
   si = round(simple_interest,1)
  # All the requested inputs including the SIMPLE INTEREST are finally displayed in full to the user.
   print(f"Present Investment: £ {present_investment}\nAnnual Interest: % {annual_interest}\nNumber Of Years Invested: {number_of_years_invested} year(s)\nSimple Interest: £ {si} ")
  #If the user selects 'compound interest'  our background calculator does the calculations
   
  elif confirm_interest==("compound interest"):
   print("Compound interest option has been selected: \n")
   # If the user selects 'compound interest' after selecting 'investment' our background calculator does the calculations
   present_investment = float(input("Please enter deposit:\n£ "))
   annual_interest = float(input("Please enter annual interest rate:\n% "))
   number_of_years_invested = int(input("Please enter amount of years invested:\n "))
   # Background calculator does the calculations
   compound_interest = present_investment*math.pow((1+(annual_interest/100)),number_of_years_invested)
   ci = round(compound_interest,1)
   # All the requested inputs including the COMPOUND INTEREST are displayed in full to the user.
   print(f"Present Investment: £ {present_investment}\nAnnual Interest: % {annual_interest}\nNumber Of Years Invested: {number_of_years_invested} year(s)\nCompound Interest: £ {ci} ")
  else:
   print("The valid option has not been selected.\nPlease ensure to enter 'simple interest or compound interest to proceed.")

elif (finance == "bond"):
  print("Bond option selected: \n")
  # If the user selects 'bond', request they provide the inputs so we can calculate the MONTHLY BOND REPAYMENT.
  present_house_value = float(input("Please enter the present value of your home:\n£ "))
  interest_rate = float(input("Please enter interest rate:\n% "))
  monthly_interest_rate = ((interest_rate/100)/12)
  number_of_years_to_repay = int(input("Please enter the number of years you plan to repay the bond:\n "))
  # Our background calculator does the calculations
  monthy_bond_repayment = (monthly_interest_rate*present_house_value)/(1-(1+monthly_interest_rate)**(-number_of_years_to_repay))
  mbr = round(monthy_bond_repayment,1)
  # All the requested inputs including the MONTHLY BOND REPAYMENT are displayed in full to the user.
  print(f"Present House Value: £ {present_house_value}\nInterest Rate: % {interest_rate}\nMonthly Interest Rate: % {monthly_interest_rate}\nNumber Of Years To Repay: {number_of_years_to_repay} year(s)\nMonthly Bond Repayment: £ {mbr} ")
else:
  print("The valid option has not been selected.\nPlease ensure to enter 'investment' or 'bond' to proceed.")


 



