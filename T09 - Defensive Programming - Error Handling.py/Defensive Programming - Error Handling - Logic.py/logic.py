
while True:
 # Request user inputs days after invoice due date

 #days_after_due_date=input("\nPlease insert payment days after invoice due date:\n ")

 # Logical error! 
 # Please use int(input("")) to convert a variable to an integer [whole number]
 try:
  days_after_due_date=int(input("\nPlease insert payment days after invoice due date:\n "))
 except ValueError:
  print("Invalid value entered :(")
  print("Please try again :)")
 else:
  break

 # Variables with their assigned values
 not_due = "Current!"
 thirty_to_sixty_days = "31 - 60 days"
 sixty_one_to_ninty_days = "61 - 90 days"
 ninty_one_to_one_hundred_and_eighty_days = "91 - 180 days"
 plus_three_hundred_and_sixty_five_days = "+ 365 days"

 # More than or equal to 0 or less than or equal to 30
if (days_after_due_date>=0) and (days_after_due_date<=30):
    print(f"Wow! Thank you!\nYou paid {days_after_due_date} day(s) after the invoice due date!.\nThe invoice was listed as {not_due}.")

 # More than or equal to 31 or less than or equal to 60
elif (days_after_due_date>=31) and (days_after_due_date<=60):
      print(f"Awesome! Thank you!\nYou paid {days_after_due_date} day(s) after the invoice due date!.\nThe invoice was listed as {thirty_to_sixty_days}.")

 # More than or equal to 61 or less than or equal to 90
elif (days_after_due_date>=61) and (days_after_due_date<=90):
     print(f" Great! Thank you!\nYou paid {days_after_due_date} day(s) after the invoice due date!.\nThe invoice was listed as {sixty_one_to_ninty_days}.")

 # More than or equal to 91 or less than or equal to 180
elif (days_after_due_date>=91) and (days_after_due_date<=180):
     print(f" Phew! Thank you!\nYou paid {days_after_due_date} day(s) after the invoice due date!.\nThe invoice was listed as {ninty_one_to_one_hundred_and_eighty_days}.")

 # More than 365
elif (days_after_due_date>365):
     print(f"Oh dear!.\nThis is a very late payment:(.\nPlease pay sooner next time.\nYou paid {days_after_due_date} days(s) after the invoice due date!.\nThe invoice was listed as {plus_three_hundred_and_sixty_five_days}.")

else:
     print("Please follow instructions!")


