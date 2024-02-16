#Instruction: Save The!quick!brown!fox!jumps!over!the!lazy!dog. as a single string

single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."
# Create an simple string name such as single_string

#Instruction: Reprint this sentence as “Thequickbrownfoxjumpsoverthelazydog.“

Answer1=single_string.replace("!"," ")
print(Answer1)
# print(Answer1) will give us the result when we implement .replace function to replace "!" with empty space " " in our single_string

#Instruction: Reprint that sentence as:“THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.”
Answer2=Answer1.upper()
print(Answer2)
# print(Answer2) will give us the result when we implement .upper function to Answer1

# Instruction: Print the sentence in reverse
Answer3=Answer2[::-1]
print(Answer3)

# print(Answer3) will give us the result when we implement [::-1] where we ignore both beginning and include step ( which is -1 = backwards)