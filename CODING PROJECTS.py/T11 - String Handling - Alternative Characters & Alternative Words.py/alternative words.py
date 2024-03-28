# Alternative words
# We request user input a word/words for our string
message1 = input("Please enter word for alternative word analysis:\n") # \n For new line or \t for tab

# Breakdown the string into a list of smaller pieces e.g. ["","","",""]
message1 = message1.split()

# Whether its result = 0 or result = [] etc, these variables are usually created as placeholders in a function so that you can later append values to them as needed.
result = []

# For loop is used to iterate through the loop along with the length of the string input
for i in range(len(message1)):
    
    if i % 2 == 0:
        # If the index of the character is even, it returns the string in lowercase
         result.append(message1[i].upper())

    else:
        # If the index of the character is even, it returns the string in uppercase
        result.append(message1[i].lower())

        # Join our string and output the alternate words
print("".join(f"The alternative word(s) are/is:\t{result}"))
print("Please run programme again")

   

  

