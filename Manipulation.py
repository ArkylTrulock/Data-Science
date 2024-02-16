str_manip = input("Please enter a sentence: ")
# Ask the user to enter a sentence

display_the_length=len(str_manip)
# display_the_length will provide length of the input
print(display_the_length)

last_3_letters=str_manip [-3:]
# [-3:] is select three letters from the left
print(last_3_letters)

replace_last_letter_with_at=last_3_letters.replace("n","@")
# Replace last letter n with @
print(replace_last_letter_with_at)

last_3_letters_backwards=str_manip[:-4:-1]
print(last_3_letters_backwards)
# [ignore:-4(last 3 letters):-1(backwards)]

first_3_letters = str_manip[0:3]
print(first_3_letters)
# [0:3] = include first to third letter
last_2_letters = str_manip[-2:]
print(last_2_letters)
# [-2:]  = last two letters

print(first_3_letters + last_2_letters)
#  Concat first three letters and last two letters