#print "Welcome to the error program"
    #print "\n"

# Missing parantheses error
# Print "welcome to the error program" as ("welcome to the error program")
print ("Welcome to the error program")  
# Print "\n" in () with Align (print "\n") with print ("Welcome to error programm")
print ("\n")

#################################################################

 #age_Str == "24 years old" 
    #age = int(age_Str) 
    #print("I'm" + age + "years old.")

# Syntax error
# The variable is NOT equal to the value. The variable's role is to store the value. variable = "value"  not variable == "value" 
# Use age_Str =  "24 years old". Remove "years old" as this is already added in the final string.
age_Str = "24" 
# int converts variable age_str to an integer
age = int(age_Str) 
# str converts variable age to a string
print("I'm " + str(age) + " years old.")
# Align both variables including print() to above

##################################################################

#years_from_now = "3"
    #total_years = age + years_from_now

# Logical error
# int converts variable years_from_now to a string
years_from_now = "3"
total_years = age + int(years_from_now)

#print "The total number of years:" + "answer_years"

# Logical, spelling and missing parantheses error. 
# Delete '+' as it is incorrect and variable "answer_years" does not exist/is not defined.
# present variable total_years as {total_years}
# print(f-string "Sentence: {total_years}" as below
print(f"The total number of years: {total_years}")
# Align both variables including print() to above

####################################################################

#total_months = total * 12
#print "In 3 years and 6 months, I'll be " + total_months + " months old"

# Logical, missing number and missing parantheses errors. 
# total_years * 12 [number of years] plus 6 [number representing number of months] to get total of 330 months.
total_months = total_years * 12 + 6
# Missing parantheses.
# present variable total_months as {total_months}
# print(f-string "Sentence 1: {total_months} + "Sentence 2") as below
print (f"In 3 years and 6 months, I'll be: {total_months} months old")
# Align variable and print() to above
