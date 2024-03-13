import time

# Initialise the sum of the input values to 0.
total = 0

# Initialise count of the input values to 0.
count = 0

# Initialise average of the input values to 0.
average = 0

while True:
      
      try:
         # Instruct the user to enter a numerical value that is not -1 to proceed.
         value = int(input("\nPlease enter a numberical value that is not -1 to proceed: \t"))

         # Looping will persist when -1 is NOT entered.
         while value!=-1:
             
             # Add the value entered by the user to the total.
             total += value
     
             # Increment the count.
             count+=1

             # Instructs the user to add more numbers (as the loop continues).
             value = int(input("Please add number: "))
             time.sleep(1)

         # if the first condition is evaluated to be TRUE (the count of the values entered by the user is more than 0) the block of code below will be executed.
             if count > 0:

            # The average is calculated as shown below:
              average = total / count

         # if the condition is evaluated to be TRUE the block of code below is executed.
        
         else:
             # if our first condition is evaluated to be TRUE is evaluated to be TRUE the block of code below is executed.
            print("Incorrect numerical value has been entered!") 
            print(".............Processing................. ")
            time.sleep(1)
            print(f"The count of the values entered is: \t{count}\nThe sum of values entered is: \t{total}\nThe average of the values entered is: {average}\t")
            print("Thank you for your input!")
            print("----------------------------------------------------------------------------------------------")
            time.sleep(1)        
             
      except ValueError:
          # If a non numerical value is entered the block of code below will be executed.
          print("Please enter numberical value to proceed!")
          time.sleep(1)

    


   
       






    
