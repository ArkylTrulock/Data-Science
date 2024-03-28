# Request the user inputs the name of their favourite restaurant & number.

string_fav = input("Please enter the name of your favourite restaurant: ")
int_fav = int(input("Please enter your favourite number: "))

# Print both using two different statements
print(f"Your favourite restaurant is {string_fav}")
print(f"Your favourite number is {int_fav}")

#The input for string_fav cannot be cast as an integer. It has to be a full number or number with a decimal.
print(int(string_fav))