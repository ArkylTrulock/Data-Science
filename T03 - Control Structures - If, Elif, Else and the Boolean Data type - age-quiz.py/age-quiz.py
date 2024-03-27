age=int(input("Please enter your age: "))

# If you are between 40 and 99, you are over the hill.
if age>=40 and age<=64:
    print("You're over the hill.")

# If you are between 65 and 99, enjoy yor retirement!.
elif age>=65 and age<=99:
    print("Enjoy your retirement.")

# If you are 100 and older, Sorry you're dead.
elif age>=100:
    print("Sorry, you're dead.")

# If you are under 13, you qualify for the kiddie discount.
elif age<13:
    print("You qualify for the kiddie discount.")

# If you are 21, congrats on your 21st!.
elif age==21:
    print("Congrats on your 21st!.")

# Any other age, Age is but a number.
else:
    print("Age is but a number.")