# Compilation errors are syntax and semantics errors which are detected by the compiler.
# They prevent the code from running when detected.
# It includes syntax errors such as missing parantheses(}) , missing of semicolon(;), printing the value of variable without declaring it, misspelling of keywords and identifiers etc.
# Semantics refer to the meaning of a statement. When a statement does not make sense and is not meaningful then it is refered to as a semantcs error.

#########################################################################################################################################################

#my_number=0              
#while my_number<100 
        #my_number+=1     
        #if my_number>23:
            #continue     
        #printmy_number
    
my_number=0        
# Compilation error 1 - Syntax error corrected with addition of expected missing colon  : , [This wll help specify when our condition ends].    
while my_number<100:     
        my_number+=1     
        if my_number>23:
            continue     
        # Compilation error 2 - Syntax error corrected with addition of expected missing parantheses () , [The block of code in [continue] is executed].
        print(my_number) 

############################################################################################################################################################

# Runtime errors occur during program execution(run-time) after successful compilation. One of the most common run-time error is division by zero also known as Division error.

#x = float(input("Please enter a number: \n"))
#y = float(input("Please enter a number: \n"))
# The actual output will be incorrect. This because we add the value of variable x to value of variable y and divide by 0.
#z = (x + y)/0
#print(f'The result is: {z}')

x = float(input("Please enter a number: \n"))
y = float(input("Please enter a number: \n"))
# The actual output is correct. This because add the value of variable x to value of variable then divide by 2 NOT 0.
z = (x + y)/2
print(f'The result is: {z}')

##############################################################################################################################################################

# Logical errors occur when the code runs without any syntax or runtime errors but produces incorrect results due to flawed logic in the code.

n = 5
game_changer = 1
for i in range(1, n):
 game_changer =  game_changer * i #[game_change* = i]

print(game_changer)

n = 5
game_changer = 1
# The for loop was iterating from 1 to n-1 instead of from 1 to n. This resulted in the incorrectly calculated factorial or 24 instead of 120. 
# To fix the logical error, we change the range of the for loop to include n.
for i in range(1, n+1):
 game_changer =  game_changer * i #[game_change* = i]

print(game_changer)
