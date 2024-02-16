# Alternative charaters
# We request user input a word/words for our string
message1 = input("Please enter word for alterntative character analysis:\n") # \n For new line or \t for tab

# Empty string is declared/initialized
message2 = "" # Or message2 = []

# For loop is used to iterate through the loop along with the length of the string input
for z in range(len(message1)):
   if z % 2 == 0:
     
     # If the index of the character is even, it returns the string in lowercase
      message2 += message1[z].lower()

   else:
     # If the index of the character is odd, it returns the string in uppercase
      message2 += message1[z].upper()

    # The alternate characters are printed
print(f"The alternative character(s) is/are:\t{message2}")

######################################################################################################

# Alternative words
# We request user input a word/words for our string
message3 = input("Please enter word for alternative word analysis:\n") # \n For new line or \t for tab

# Breakdown the string into a list of smaller pieces e.g. ["","","",""]
message3 = message3.split()

# Whether its result = 0 or result = [] etc, these variables are usually created as placeholders in a function so that you can later append values to them as needed.
result = []

# For loop is used to iterate through the loop along with the length of the string input
for i in range(len(message3)):
    
    if i % 2 == 0:
        # If the index of the character is even, it returns the string in lowercase
         result.append(message3[i].upper())

    else:
        # If the index of the character is even, it returns the string in uppercase
        result.append(message3[i].lower())
    break
        # Join our string and output the alternate words
print("".join(f"The alternative word(s) are/is:\t{result}"))
print("Please run programm again")

   

  

