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
print("Run programme again")

