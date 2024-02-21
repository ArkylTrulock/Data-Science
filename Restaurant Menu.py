import time

restaurant_dictionary = {"fried rice":5,
                         "shrimp fried rice":8,
                         "special fried rice":9,
                         "sweet and sour pork":13,
                         "lemon chicken":14,
                         "pork in black bean sauce":15,
                         }

for order in restaurant_dictionary:
  # Print the restaurant menu
  print(order)

# Initialise total_price to 0
total_price = 0

while True:
    try:
        order = input("\nAre you ready to order?: Yes/No\t").lower()
        if order == "yes":
         # If the first condition is evaluated to be TRUE the block of code below is executed. The total_price program is activated.
         place_order = input("\nIf a single item is ordered no comma is needed. If several items are ordered please ensure they are comma separated with no spaces.\nWhat would you like to order?: ").lower()
         item_list = place_order.split(",")

         for item in item_list:     
           # for loop is used to iterate over our iterable object in this case 'item_list' variable containing the elements/values which are the same as 'key' names in
           # restaurant_dictionary dictionary. The dummy variable 'item' in the for loop can be any letter that MUST be used in our indented code below
           # We calculate the final 'total_price' by adding the initialised 'total_price' [0.00] + 'restaurant_dictionary'[item]
           total_price = total_price + restaurant_dictionary[item]
           print(f"The price of the ordered {" + ".join(item_list)} is {total_price} total_price")
           print("Thank you for you business!")
         #break # Exit the loop.
         #continue
         
        elif order =="no":
         # If the first condition is evaluated to be FALSE the 2nd condition is evaluated to be TRUE the block of code below is executed.
         print("No problem, please take your time. I'll be back very shortly to take your order.")
         #break # Exit the loop.
         #continue
         time.sleep(1)
          
        else:
          # If the first and second conditions are evaluated to be FALSE the block of code below is executed.
         print("Invalid input! Please type Yes or No to proceed.")
         #break # Exit the loop.
         #continue
        time.sleep(1)
             
    except KeyError:
       # If the incorrect key is typed the block of code below is executed.
       print("\nInvalid input! Please enter the item as listed in the menu to proceed.")
       print("If you have any questions or suggestions please email: vernyuyyenwomolo@gmail.com")
       #break # Exit the loop.
       #continue
       time.sleep(1)
    

    
    
