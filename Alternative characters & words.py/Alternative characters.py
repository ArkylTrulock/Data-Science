# ALTERNATIVE CHARACTERS

# We request user input a word/words for our string
user_input = input("Please enter word for alterntative character analysis:\n") # \n For new line or \t for tab
# Split parameter should be inside the function 'user_input'. 
# String-we-are-splitting.split(" gap ") To split our string and creates an element for each word['X','X','X']
split_input = user_input.split(" ")
# Declare an empty string where our end result will be appended/added
new_list = [ ]



# 'word' is our dummy variable in a [for loop]. This can be any letter and MUST be used in our indented code below.
# We use 'len' because anything inside 'in range' [in this case - 'split_input'] should be interpreted as an integer.
# for 'word' in 'range' 
for word in range(len(split_input)):
    
    # If our variable in the range is even. 
    if word % 2 == 0:
        
        
        # print(split_input[word].upper()). # Outputs each word in a new line
        # Below outputs each word in one line
        new_list.append(split_input[word].upper())

    # If the first condition 'word' is evaluated to be 'FALSE' /  If our variable in the range is odd
    else:
          new_list.append(split_input[word].lower())

'print(new_list)' # Does not print our words into a sentence. ['X','X','X']

#  " ".join to print our words as a sentence. [ X X X X X]
print(" ".join(new_list))