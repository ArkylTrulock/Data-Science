# Request the user to input name, age, house number and street name

name = input("Insert your name: ")
age = int(input("Insert your age: "))
house_number = int(input("Insert your House number: "))
street_name = input("Insert your Street name: ")

# Concat the tailored sentences with the inputs for name, age house, number and street name. "sentence1"+ name +"sentence2"+ age +"sentence3"+ house number +"sentence4"+ street name +"."
print(" The suspect's name is " + name + ". He is " + age  + " years of age and resides on " +  house_number + " "  +   street_name + ".")
